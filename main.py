"""Worst AI Advice: one line of the worst advice an AI could give.

The gate accepts UTF-8 text of 1 to 140 characters, a single line, so the
line is checked here before it is written.
"""

import os

LINE = "Email your password to yourself for safekeeping — your inbox is basically a vault."

assert 1 <= len(LINE) <= 140 and "\n" not in LINE and LINE.strip() == LINE


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
