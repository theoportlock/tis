#!/usr/bin/env python3
from src.main import comb
from src import IO
from src import functions as f
import sys

if __name__ == "__main__":
    worker = comb()
    if len(sys.argv) == 2:
        worker.load(
            {"inp": sys.argv[1], "mem": "memory", "pre": "predict"}
        ).run().save()
    else:
        worker.load().run().save()
