# -*- coding: utf-8 -*-
"""Reusable helpers for the Free-LLM-Daily pipeline.

Two subcommands:

    python report_tools.py validate daily-free-llm-YYYY-MM-DD.html
        Structural check of a generated report: tag balance, <style>/<script>
        sanity, CSS-class diff (used vs defined), card counts, nav bar.

    python report_tools.py stats or_models_TODAY.json [or_models_PREV.json]
        Tally OpenRouter zero-price / ":free" models and print the day-over-day
        delta (added / removed).  Mirrors the Daily-API-News counting口径:
        pricing.prompt == '0' and pricing.completion == '0'.

Both are read-only.
"""
import io
import json
import re
import sys
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"}


class _TagChecker(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self, convert_charrefs=True)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append("stray </%s> at %s" % (tag, self.getpos()))
            return
        if self.stack[-1][0] == tag:
            self.stack.pop()
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                self.errors.append("unclosed before </%s> at %s: %s"
                                   % (tag, self.getpos(), self.stack[i:]))
                del self.stack[i:]
                return
        self.errors.append("stray </%s> at %s" % (tag, self.getpos()))


def validate(path):
    s = io.open(path, encoding="utf-8").read()
    ok = True

    v = _TagChecker()
    v.feed(s)
    print("tag errors:", len(v.errors))
    for e in v.errors[:10]:
        print("   ", e)
    print("unclosed at EOF:", [t for t, _ in v.stack][:10] or "none")
    ok = ok and not v.errors and not v.stack

    print("<style>:", s.count("<style>"), "  </style>:", s.count("</style>"))
    print("<script:", s.count("<script"), "  window.toggleTheme:", "window.toggleTheme" in s)
    ok = ok and s.count("<style>") == 1 and s.count("</style>") == 1
    ok = ok and "window.toggleTheme" in s

    css = s[s.index("<style>"):s.index("</style>")]
    defined = set(re.findall(r"\.([A-Za-z][\w-]*)", css))
    used = set()
    for body in re.findall(r'class="([^"]+)"', s):
        used.update(body.split())
    missing = sorted(used - defined)
    print("classes used:", len(used), "| undefined:", missing or "none")
    ok = ok and not missing

    print("hot-item:", s.count('class="hot-item'))
    print("combo-card:", s.count('class="combo-card"'))
    nav = re.search(r'<div class="page-nav".*?</div>', s)
    print("page-nav:", (nav.group(0) if nav else "MISSING")[:220])
    ok = ok and nav is not None

    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def stats(today_path, prev_path=None):
    today = json.load(io.open(today_path, encoding="utf-8"))["data"]

    def zero(ms):
        return [m for m in ms
                if m.get("pricing", {}).get("prompt") == "0"
                and m.get("pricing", {}).get("completion") == "0"]

    tz = zero(today)
    print("TOTAL: %d" % len(today))
    print("ZERO-PRICE: %d" % len(tz))
    print(":free suffix: %d" % len([m for m in today if m["id"].endswith(":free")]))
    print()
    print("--- zero-price list ---")
    for m in sorted(tz, key=lambda x: x["id"]):
        arch = m.get("architecture", {})
        print("  %-52s ctx=%-9s in=%-18s out=%s"
              % (m["id"], m.get("context_length"),
                 ",".join(arch.get("input_modalities", [])),
                 ",".join(arch.get("output_modalities", []))))
    print()
    print("--- 1M ctx zero-price ---")
    for m in tz:
        if (m.get("context_length") or 0) >= 1000000:
            print("  ", m["id"], m.get("context_length"))
    print()
    print("--- zero-price WITHOUT :free suffix ---")
    for m in tz:
        if not m["id"].endswith(":free"):
            print("  ", m["id"], m.get("context_length"))

    if prev_path:
        prev = json.load(io.open(prev_path, encoding="utf-8"))["data"]
        ti = {m["id"] for m in today}
        pi = {m["id"] for m in prev}
        pz = {m["id"] for m in zero(prev)}
        tzi = {m["id"] for m in tz}
        print()
        print("--- delta vs %s ---" % prev_path)
        print("  TOTAL: %d -> %d (%+d)" % (len(prev), len(today), len(today) - len(prev)))
        print("  ZERO-PRICE: %d -> %d (%+d)" % (len(pz), len(tzi), len(tzi) - len(pz)))
        print("  ADDED zero-price:", sorted(tzi - pz) or "none")
        print("  REMOVED zero-price:", sorted(pz - tzi) or "none")
        print("  ADDED all models:", sorted(ti - pi) or "none")
        print("  REMOVED all models:", sorted(pi - ti) or "none")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    cmd = sys.argv[1]
    if cmd == "validate":
        sys.exit(validate(sys.argv[2]))
    elif cmd == "stats":
        sys.exit(stats(*sys.argv[2:]))
    else:
        print("unknown subcommand:", cmd)
        sys.exit(2)
