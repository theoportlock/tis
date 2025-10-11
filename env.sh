#!/usr/bin/env bash
# Environment setup for tis

# Code path
export PATH=$PATH:src/
export PATH=$PATH:experiments/

# Activate Python virtual environment
if [ -f venv/bin/activate ]; then
    . venv/bin/activate
else
    echo "No venv found at venv/bin/activate"
fi

