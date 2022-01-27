#!/usr/bin/env bash
CURRENT_DIR=`dirname "$0"`
ROOT_DIR=$CURRENT_DIR/../../..

docker run -it --rm         \
    --env TRAME_BUILD_ONLY=1 \
    -v "$CURRENT_DIR:/deploy" \
    -v "$ROOT_DIR:/local-app"  \
    trame