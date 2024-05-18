#!/usr/bin/env bash
export SRC_PATH="$(dirname "${BASH_SOURCE[0]}")"
export $(cat $SRC_PATH/.env | xargs)