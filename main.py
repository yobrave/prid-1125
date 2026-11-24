"""prid-1125: one line of earned pride, gate 1..240."""

import json
import os

SPAN = 240


def earn(folder):
    trophy = os.path.join(folder, "entry.txt")
    raw = open(trophy, "rb").read()
    line = raw.decode("utf-8").strip()
    if not 1 <= len(line) <= SPAN:
        raise SystemExit("the moment measures %d chars; shelf allows 1..%d" % (len(line), SPAN))
    return line


def display(folder, line):
    cabinet = os.environ.get("MAKEFUN_OUTPUT_DIR") or folder
    os.makedirs(cabinet, exist_ok=True)
    plaque = os.path.join(cabinet, "entry.txt")
    with open(plaque, "w", encoding="utf-8", newline="\n") as engraver:
        engraver.write(line + "\n")
    return plaque


room = os.path.dirname(os.path.abspath(__file__))
line = earn(room)
print(json.dumps({"pride": line[:46], "etched": len(line), "quiet": True, "plaque": display(room, line)}))
