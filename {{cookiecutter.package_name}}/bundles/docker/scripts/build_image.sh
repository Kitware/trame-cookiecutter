#!/usr/bin/env bash
CURRENT_DIR=`dirname "$0"`

cd $CURRENT_DIR
BASE_PATH="$PWD"

. ./build_server.sh

cd "$BASE_PATH/.."
docker build -t {{cookiecutter.entry_point}} .
