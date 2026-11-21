#!/usr/bin/env python3
"""Copy the finished front page into the grader's output directory.

Stdlib only: the grader runs this in a stock python:3.13 image with no
Pillow and no network. All rendering happens at build time.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
os.makedirs(out, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(out, "entry.png"))
