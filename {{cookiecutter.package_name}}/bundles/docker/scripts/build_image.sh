#!/usr/bin/env bash
CURRENT_DIR=`dirname "$0"`

cd $CURRENT_DIR
. build_server.sh
cd ..
docker build -t {{cookiecutter.entry_point}}