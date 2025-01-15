#!/bin/bash

docker build --platform linux/arm64 -t python-selenium .
# --rm removes the container when it finishes running, freeing up resources
docker run --platform linux/arm64 --rm python-selenium
