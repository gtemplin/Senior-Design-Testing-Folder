import json  # interact with json 
import sys, os  # interact with the operating system 
import requests  # used to make http requests or interact with   
import configparser # handle configuration files to store preferences 
import asyncio  # helps manage multiple IO related tasks 
import urllib3  # used for making requests to web servers through http 


Curpath = os.getenv('CURPATH', '/usr/src/app')
print(f'Current path for Sensing.py: {Curpath}')

debug = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# format a message and send to database
# the asyncio loop lets this wait until complete w/o bottlenecking the whole program  
def send_to_database(address, msg):
    try:
        if msg!='':
            url=address.format(msg[0: 1], msg[2:])
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(sendData(url))
    except ConnectionError as c:
        return False
    except Exception as c:
        print(c)
        return False

# uses an http get request to send the data 
async def sendData(url):
    print(url)
    response= requests.get(url, verify=False)
    return bool(int(response.status_code)==200)


# uses python's file management function to append 
def write_to_backup(backup, data):
    with open(backup, "a") as _:
        _.write(data)
        return True
    return False


def delete_from_file(file_name, part_to_delete):
    file = open(file_name, "w+")
    file_contents = file.read()
    file_contents = remove_prefix(file_contents, part_to_delete)
    file.truncate()
    file.write(file_contents)
    file.close()


def remove_prefix(input_string, prefix):
    if prefix and input_string.startswith(prefix):
        return input_string[len(prefix):]
    return input_string

# Get webserver addtess
def json_to_dict(filename):
    fp = open(filename, 'r')
    data = json.load(fp)
    fp.close()
    return data


#####################################################
############# SETUP PORTION BELOW ###################
#####################################################   ggb

# the web server for a particular customer is extracted from a json file 
config_file_path = os.path.join(Curpath, "ConfigurationFiles", "configCustomer.json")
config = json_to_dict(config_file_path)
webserver_address = config['WebserverAddress']

# Create path to backup text file 
text_files_folder_path = os.path.join(Curpath, "TextFiles")
backup_file_path = os.path.join(text_files_folder_path, "BackupData.txt")
# Create the backup text file 
if not os.path.isfile(backup_file_path):
    # Create the file if it does not exist
    with open(backup_file_path, "x") as f:
        # File is created, 'f.close()' is called automatically
        print("Backup text file created in 'TextFiles' folder")





#####################################################
############# LOOPING PORTION BELOW #################
#####################################################

# If either of the flags are set, store the data from the file associated with it, then clear that file so that it can be used again later. 
# Once it sees that a flag is set for communication, it formats it and sends it to the database 
while True:
    communication_flag_path = os.path.join(Curpath, "CommunicationFlag.txt")
    communication_flag_actuator_path = os.path.join(Curpath, "CommunicationFlagActuator.txt")

    # Create fresh files to send, and reset flags 
    if os.path.isfile(communication_flag_path) or os.path.isfile(communication_flag_actuator_path):
        fileContents = ""
        if os.path.isfile(communication_flag_path):
            try:
                os.remove(communication_flag_path)
            except Exception:
                print("CommunicationFlag is not deleted")
                pass
            formatted_system_data_path = os.path.join(Curpath, "FormattedSystemData.txt")
            with open(formatted_system_data_path, "r+") as file:
                fileContents = file.read()
                file.seek(0)  # Move to the start of the file before truncating
                file.truncate()

        fileContentsActuator = ""
        if os.path.isfile(communication_flag_actuator_path):
            try:
                os.remove(communication_flag_actuator_path)
            except Exception:
                print("CommunicationFlagActuator is not deleted")
                pass
            formatted_system_data_actuator_path = os.path.join(Curpath, "FormattedSystemDataActuator.txt")
            with open(formatted_system_data_actuator_path, "r+") as file2:
                fileContentsActuator = file2.read()
                file2.seek(0)  # Move to the start of the file before truncating
                file2.truncate()

        fileContents= fileContents + fileContentsActuator

        if debug:
            print("FILE CONTENTS: {}".format(fileContents))


# Parse through the file contents until you get to the delimiter ($)
# After this you can send the stored message to the database 
        start_index = 0
        successfulSend=False
        for i in range(0, len(fileContents), 1):
            if fileContents[i] == "$":
                msg = fileContents[start_index: i] ## TRY DIFFERENT SUBSTRING METHOD
                if debug:
                    print("sending: {}".format(msg))
                successfulSend = send_to_database(webserver_address, msg)
                start_index = i+1
                

# This portion backs up the data if it wasn't successful and sends any data in the backup text file to the database
        if not successfulSend:
            print("CONNECTION IS DOWN--BACKING UP DATA")
            write_to_backup(backup_file_path, fileContents)
        else:
            backup = open(backup_file_path)
            backupContents = backup.read()
            start_index = 0
            for i in range(0, len(backupContents), 1):
                if backupContents[i] == "$":
                    msg = backupContents[start_index: i]
                    successfulSend = send_to_database(webserver_address, msg)
                    start_index = i + 1
                    if successfulSend:
                        delete_from_file(backup_file_path, msg)
