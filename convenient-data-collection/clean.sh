#!/bin/bash

echo y | docker system prune -a

docker rmi test:test
