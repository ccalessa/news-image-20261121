# A judged-artifact entry for make.fun bounty news-image-20261121.
#
# The program is a Node-free Python 3.13 program that writes one image summing
# up the world's news of Saturday 21 November 2026 to /output/entry.png.
# It renders nothing at grading time: the image is pre-rendered at build time
# (render.py) and committed to the repository. This program simply copies it.
#
# Runs with no network, standard library only. Two runs write identical bytes.
#
# Outside the grader's container:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT, "entry.png"))
