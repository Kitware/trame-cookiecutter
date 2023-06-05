#!/usr/bin/env bash
CURRENT_DIR=`dirname "$0"`

cd $CURRENT_DIR/..
DEPLOY_DIR="$PWD"

. scripts/build_server.sh

cd "$DEPLOY_DIR"
docker build -t {{cookiecutter.entry_point}} .
