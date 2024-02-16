import sys
import os 
import helpers # from helpers.py which has useful functions 

# Ensure Docker is installed before doing anything 
dockerStatus = helpers.dockerInstalled()
if not dockerStatus:
    sys.exit()


# Show the user their present directory and it's subdirectories
# for copy-paste purposes
print("Your PWD and it's subdirectories:\n")
helpers.Runcommand("pwd", "yes")
helpers.Runcommand("ls", "yes")
helpers.spacing(2)


# Show images for copy-paste purposes 
helpers.Runcommand("docker images", "yes")
helpers.spacing(2)
print("Input spaces will be replaced with a dash")

# Get the image to instantiate through a container
image_name = input("Enter the image name: ")
image_name = image_name.replace(" ", "-")

# Get the container tag
image_tag = input("Enter the image tag: ")
image_tag = image_tag.replace(" ", "-")
helpers.spacing(2)



while True: 
    build_directory = input("Enter the build directory, or press enter for PWD: ")
    print(build_directory)
    if build_directory == "":
        build_directory = "."
        print("Building from PWD")
        break
    elif build_directory == "exit":
        sys.exit()
    elif not os.path.exists(build_directory):
        print("That directory doesn't exist")
    else:
        print("Building from " + build_directory)
        break
helpers.spacing(2)


build = input("To build your image press enter, or enter exit to quit:")
while True:
    if build == "":
        build_command = "docker build -t " + image_name + ":" + image_tag + " " + build_directory
        helpers.Runcommand(build_command, "yes")
        break
    elif build == "exit":
        print("Terminating program")
        sys.exit()

# Now run the container
local_volume_directory = "/home/admin/Senior-Design-Testing-Folder/LocalVolume"
container_volume_directory = "/usr/src/app"
docker_network = "hassio" # use the network created by home assistant 
helpers.runContainer(local_volume_directory, container_volume_directory, docker_network)










