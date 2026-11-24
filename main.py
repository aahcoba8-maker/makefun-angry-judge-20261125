"""Angry Judge: The Short Rant Contest.

Writes one short rant about a small everyday annoyance to entry.txt.
"""
import os

TEXT = (
    "Self-checkout accused me of stealing my own bananas. "
    "'Unexpected item in the bagging area.' Unexpected? I scanned them. "
    "I bagged them. It watched me do it - then called the attendant "
    "like I'd robbed the place. "
    "I came in for milk and left a suspect."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
