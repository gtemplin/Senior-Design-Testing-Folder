import os
import sys
import helpers 


spacesize = 2

# make sure docker is installed
docker_status = helpers.runCommand("docker --version")
docker_status = docker_status.split()
if docker_status[0] == "Docker" and docker_status[1] == "version":
    pass
else:
    print("Docker not installed. Install it before continuing \nTerminating program")
    sys.exit()



print("Your PWD and it's subdirectories:")
helpers.runCommand("pwd", "yes")
helpers.runCommand("ls", "yes")


while True: 
    # Get the volume path from the user
    volumePath = input("Enter the path on your machine where the volume should be stored: ")
    volumePath = volumePath.replace(" ", "")
    # Terminate the program if the user says exit
    if volumePath == "exit":
        print("Setup script terminated")
        sys.exit()
    if os.path.exists(volumePath):
        print("Shared volume path: " + volumePath)
        break
    else:
        print("That directory doesn't exist.")

helpers.spacing(spacesize)

# Show the user all of the currently existing networks 
networks = helpers.runCommand("docker network ls")
network_list = networks.split("\n")
network_names = ["Existing Network Names:"]
for item in network_list[1:]:
    name = item.split()
    if len(name) > 1:
        network_names.append(name[1])
for network in network_names:
    print(network)

helpers.spacing(spacesize)

# Get user network input
while True:
    network = input("Enter the network to use: ")
    if network in network_names:
        print("Using " + network + " as the network")
        break
    elif network == "exit":
        print("Setup script terminated")
        sys.exit()
    else:
        print(network + " is not an existing network")

helpers.spacing(spacesize)

# Get the image
print("Note: spaces will be converted to dashes")
container_name = input("Enter the container name: ")
container_name = container_name.replace(" ", "-")

helpers.spacing(spacesize)

# Show the user all of the currently existing images 
images = helpers.runCommand("docker images")
image_list = images.split("\n")
image_names = []
image_tags = []

print("Existing image names + their tags")
for item in image_list:
    image_row = item.split()
    if len(image_row) > 1:
        image_names.append(image_row[0])
        image_tags.append(image_row[1])

index = range(len(image_names))
for i in index:
    print(image_names[i] + " : " + image_tags[i])
while True:
    image = input("Enter the image to use: ")
    if image in image_names:
        print("Using " + image + " as the base image")
        break
    elif image == "exit":
        print("Setup script terminated")
        sys.exit()
    else:
        print(image + " is not an existing image")

while True:
    tag = input("Enter the image tag to use: ")
    if tag in image_tags:
        print("Using " + tag + " as the image tag")
        break
    elif tag == "exit":
        print("Setup script terminated")
        sys.exit()
    else:
        print(tag + " is not a tag for your image")

helpers.spacing(spacesize + 1)
print("Generating the run command: ")

# Generate the run command
C1 = "docker run -it "
C2 = "-v " + volumePath + ":/usr/src/app/BackupData "
C3 = "--network " + network + " "
C4 = "--name " + container_name + " "
C5 = image + ":" + tag
run = C1 + C2 + C3 + C4 + C5 
print("Copy and paste the command to run your container. It will also be stored in the RUNCONTAINER environment variable")
os.environ['RUNCONTAINER'] = run
print("Your run command: ")
print(run)


















