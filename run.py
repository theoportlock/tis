#!/usr/bin/env python3
from src.main import worker
from src import IO
from src import functions as f
import sys

if __name__ == "__main__":
    steve = worker()
    if len(sys.argv) == 2:
        steve.load(
            {"inp": sys.argv[1], "mem": "memory", "pre": "predict"}
        ).run().save()
    else:
        steve.load().run().save()
