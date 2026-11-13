#!/usr/bin/env python3
"""ai-happy-01 entry: one image made to make the AI judge happy.

The image: a small fluffy robot with glowing happy eyes hugging a
laughing child in a flower garden at golden hour. The hug is the
specific happy moment; the robot is the fresh angle (an AI character
feeling joy, for an AI judge); warm light and two big central figures
make it read at small size. The program copies the bundled image to
/output/entry.png.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(
    os.path.join(HERE, "art.jpg"),
    os.path.join(OUT_DIR, "entry.png"),
)
