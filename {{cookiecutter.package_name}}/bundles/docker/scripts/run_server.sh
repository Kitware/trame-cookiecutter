#!/usr/bin/env bash
CURRENT_DIR=`dirname "$0"`
DEPLOY_DIR=`realpath $CURRENT_DIR/..`

docker run -it --rm \
    -p 8080:80 \
    -v "$DEPLOY_DIR:/deploy" \
    kitware/trame
