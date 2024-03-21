import sys
import os 
import subprocess

def runCommand(command, printOutput=None):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error:\n", result.stderr)
    if printOutput is not None:
        print("Output:\n", result.stdout)
    return result.stdout

# Make sure docker installed 
docker_status = runCommand("docker --version")
docker_status = docker_status.split()
if docker_status[0] == "Docker" and docker_status[1] == "version":
    pass
else:
    print("Docker not installed. Install it before continuing \nTerminating program")
    sys.exit()



print("Your PWD and it's subdirectories:\n")
runCommand("pwd", "yes")
runCommand("ls", "yes")
print("\n\n")

print("Image names/tags can't have spaces")
image_name = input("Enter the image name: ")
image_name = image_name.replace(" ", "-")

image_tag = input("Enter the image tag: ")
image_tag = image_tag.replace(" ", "-")
print("\n\n")

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
print("\n\n")
build = input("To build your image press enter, or enter exit to quit:")
while True:
    if build == "":
        build_command = "docker build -t " + image_name + ":" + image_tag + " " + build_directory
        runCommand(build_command, "yes")
        break
    elif build == "exit":
        print("Terminating program")
        sys.exit()










