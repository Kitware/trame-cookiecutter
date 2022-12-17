#!/usr/bin/env bash
CURRENT_DIR=`dirname "$0"`

# Since Mac doesn't come with realpath by default, let's set the full
# paths using PWD.
pushd . > /dev/null
cd $CURRENT_DIR/..
DEPLOY_DIR=$PWD
cd $CURRENT_DIR/../../..
ROOT_DIR=$PWD
popd > /dev/null

docker run --rm          \
    -v "$DEPLOY_DIR:/deploy" \
    -v "$ROOT_DIR:/local-app"  \
    kitware/trame build
