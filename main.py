"""The Long Roast entry: the smart-home devotee, roasted at length."""

import os

TEXT = (
    "She runs a smart home with forty connected devices and three apps "
    "to dim one lamp, yet she still walks into the kitchen and forgets "
    "why, because no sensor ever made can notify a person of their own "
    "intentions."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
