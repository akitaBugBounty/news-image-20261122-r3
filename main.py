#!/usr/bin/env python3
"""Entry point: render the 22 November 2026 news image to /output/entry.png."""

import hashlib
import os

from render_entry import render


def main():
    out = "/output/entry.png"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    render(out)
    with open(out, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    print("wrote /output/entry.png")
    print("sha256", digest)


if __name__ == "__main__":
    main()
