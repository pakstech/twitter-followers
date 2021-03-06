#!/bin/bash

DIR=$(dirname "$0")

cd "${DIR}" || exit 1
if [[ ! -d "bin" ]]; then
    python3 -m venv .
    . bin/activate
    python3 -m pip install -r requirements.txt
fi

. bin/activate

python3 followers.py "$@"
