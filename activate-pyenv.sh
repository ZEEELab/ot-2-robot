#!/usr/bin/env bash

PYENV_ACT=pyenv/bin/activate
if ! [[ -f "$PYENV_ACT" ]]; then
  # Create a new python environment.
  python3 -m venv pyenv
  # Activate
  source ${PYENV_ACT}
  # Install requirements
  pip install -r requirements.txt
else
  # Just activating is fine
  source ${PYENV_ACT}
fi

