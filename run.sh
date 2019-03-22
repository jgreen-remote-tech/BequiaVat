#!/bin/bash

set -e

docker build -t bequiavat.local .
docker run -it --rm \
    bequiavat.local "$@"

