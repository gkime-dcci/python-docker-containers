#!/bin/bash

docker build -t python-selenium .
# --rm removes the container when it finishes running, freeing up resources
docker run --rm python-selenium
