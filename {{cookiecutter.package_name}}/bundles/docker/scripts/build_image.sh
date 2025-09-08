#!/usr/bin/env bash
CURRENT_DIR=`dirname "$0"`

cd $CURRENT_DIR/../../..

docker build -t {{cookiecutter.entry_point}} -f ./bundles/docker/Dockerfile .
