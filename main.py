#!/usr/bin/env python3
"""Publish the finished front page for the News Image 23 Nov entry.

The artwork (entry.png) sits next to this script. Running the script
copies it into the output directory the harness expects, so the entry
can be scored from a single file. Nothing is generated here; the image
is the deliverable.
"""

import os
import shutil
import sys

ARTWORK = "entry.png"


def fail(message):
    print("error: %s" % message, file=sys.stderr)
    sys.exit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, ARTWORK)
    if not os.path.isfile(source):
        fail("artwork missing: %s" % source)

    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(target_dir, exist_ok=True)
    except OSError as exc:
        fail("cannot create output directory %s: %s" % (target_dir, exc))

    target = os.path.join(target_dir, ARTWORK)
    try:
        shutil.copyfile(source, target)
    except OSError as exc:
        fail("cannot copy %s to %s: %s" % (source, target, exc))

    size = os.path.getsize(target)
    print("copied %s -> %s (%d bytes)" % (source, target, size))


if __name__ == "__main__":
    main()
