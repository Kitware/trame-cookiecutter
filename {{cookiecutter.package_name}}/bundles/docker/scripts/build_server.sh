#!/usr/bin/env bash
CURRENT_DIR=`dirname "$0"`
DEPLOY_DIR=`realpath $CURRENT_DIR/..`
ROOT_DIR=`realpath $CURRENT_DIR/../../..`

docker run -it --rm         \
    -e TRAME_BUILD_ONLY=1 \
    -v "$DEPLOY_DIR:/deploy" \
    -v "$ROOT_DIR:/local-app"  \
    kitware/trame
