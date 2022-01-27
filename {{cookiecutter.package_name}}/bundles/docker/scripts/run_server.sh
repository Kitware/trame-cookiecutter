#!/usr/bin/env bash
CURRENT_DIR=`dirname "$0"`
DOCKER_DIR="$CURRENT_DIR/.."

docker run -it --rm \
    -p 8080:80 \
    -v "$DOCKER_DIR:/deploy" \
    trame