#!/bin/bash

echo y | docker system prune

docker rmi test:test
