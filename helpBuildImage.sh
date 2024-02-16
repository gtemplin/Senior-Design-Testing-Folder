#!/bin/bash

echo "Local docker images: "
docker images 
echo " "
echo "Build template:"
echo "docker build -t {image name}:{image tag} {directory}"
echo "Note: to use your pwd, directory = . "
echo " "
echo "Enter your desired image name, image tag, and directory with dockerfile (in that order)"
read name tag directory

echo "Build command: docker build -t $name:$tag $directory"
isRun = ""

# Use a loop to keep asking until 'y' or 'n' is entered
while [[ $isRun != "y" && $isRun != "n" ]]
do
    # Prompt the user for input
    read -p "Do you want to run the command? (y/n): " isRun

    # Check if the input is 'y'
    if [ "$isRun" == "y" ]; then
        echo "Running the command..."
        docker build -t $name:$tag $directory

    # Check if the input is 'n'
    elif [ "$isRun" == "n" ]; then
        echo "Abandoning the operation."
        exit 0

    # Handle invalid input
    else
        echo "Invalid input. Please enter 'y' for yes or 'n' for no."
    fi
done
