#!/bin/bash

output=$(docker login 2>&1)

# Check if the last line of the output is "Login Succeeded"
if [[ "$(echo "$output" | tail -n1)" == "Login Succeeded" ]]; then
    echo "Login successful."
else
    echo "Login failed. Terminating the script."
    exit 1
fi

repository="iac_convenient_data_collection"

docker images

echo "Enter image to push, the associated tag, your DockerHub username, and the dockerhub tag you want to use (in that order)"
read image imagetag username hubtab

docker tag $image:$imagetag $username/$repository:$hubtab
docker push $username/$repository:$hubtab