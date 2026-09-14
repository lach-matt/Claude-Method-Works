#!/usr/bin/env python3
"""Splice a freshly generated DATA.json into master-lattice.html's DATA block.

    python3 gendata2.py > DATA2.json      # refusal / warp / obstruction half
    python3 gendata.py  > DATA.json       # the lattice half, reads DATA2.json
    python3 splice.py                     # rewrite the page's const DATA = {...}

THIS EXISTS BECAUSE THE LAST RENDER'S GENERATOR DID NOT. DATA2.json was written
once by hand and no program survived to reproduce it, so seating a tenth index
meant re-deriving figures whose definitions had to be guessed. Nothing here is
transcribed from a previous render; every value is measured by the two
generators above, and the page is the only hand-written part.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "master-lattice.html")
DATA = os.path.join(HERE, "DATA.json")


def main():
    h = open(PAGE).read()
    i = h.index("const DATA = {")
    j = i + len("const DATA = ")
    depth = 0
    for k in range(j, len(h)):
        if h[k] == "{":
            depth += 1
        elif h[k] == "}":
            depth -= 1
            if depth == 0:
                break
    else:
        print("unbalanced DATA block", file=sys.stderr)
        return 1
    new = open(DATA).read().rstrip()
    open(PAGE, "w").write(h[:j] + new + h[k + 1:])
    print("spliced %d bytes of DATA into %s" % (len(new), os.path.basename(PAGE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
