import subprocess

# Input a terminal command to run
# Include a second argument to see the command's standard output 
def runCommand(command, printOutput=None):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error:\n", result.stderr)
    if printOutput is not None:
        print("Output:\n", result.stdout)
    return result.stdout


# Returns True if docker is installed, False if not
def dockerInstalled():
    docker_status = runCommand("docker --version")
    docker_status = docker_status.split()
    if docker_status[0] == "Docker" and docker_status[1] == "version":
        return True
    else:
        print("Docker not installed")
        return False


# Prints out the inputted # of spaces
def spacing(num_spaces):
    for s in range(num_spaces):
        print("\n")



# Ask a question, then call this function, and it will
# make the user answer yes or no.
# Ex: answerToUse = yes_or_no()
def yes_or_no():
    truth = ""
    while truth != "yes" or truth != "no":
        if truth == "yes":
            return "yes"
        elif truth == "no":
            return "no"
        else:
            truth = str.lower(input("Enter yes or no: "))


# Run a container w/ several possible options 
def runContainer(image_name, volume_path_local=None, volume_path_container=None, network=None):
    # Start building the command with the base part
    command = "docker run"

    # Add volume if both local and container paths are provided
    if volume_path_local and volume_path_container:
        command += " -v " + volume_path_local + ":" + volume_path_container

    # Add network if provided
    if network:
        command += " --network=" + network

    # Prompt for running in detached mode
    print("Do you want to run in detached mode (container runs in the background)?")
    detached = yes_or_no()
    if detached == "yes":
        command += " -d"

    # Prompt for interactive mode
    print("Do you want to be able to interact with the container?")
    interact = yes_or_no()
    if interact == "yes":
        command += " -it"

    # Add the image name at the end of the command
    command += " " + image_name

    print("Command to run:", command)  # For demonstration, print the command instead

    runCommand(command, "yes")
    













































