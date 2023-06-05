#!/usr/bin/env bash
CURRENT_DIR=`dirname "$0"`

cd $CURRENT_DIR/..
DEPLOY_DIR="$PWD"

docker run -it --rm \
    -p 8080:80 \
    -v "$DEPLOY_DIR:/deploy" \
    kitware/trame
