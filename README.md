# Senior-Design-Testing-Folder
### Raspberry Pi SSH Login
- admin@134.68.225.201
- password = admin

### Raspberry Pi Directory Structure 
- Everything will be based in the admin's home directory (just input 'cd' to get here once logged in)

### Home Assistant API Token:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxZDRjOGEzZDcwOTY0ZjBhOTc0OTU4Y2I0YzgyODA4OSIsImlhdCI6MTcwODA0Nzc0NSwiZXhwIjoyMDIzNDA3NzQ1fQ.YMImMN9S4cxT56mFCtK4cRmQT-8ohM7sk4V2EFjno1Q

### Note on DNS
- Home assistant is using it's own network called 'host', which doesn't have a DNS setup
- This means we won't be able to use the local DNS and will have to make sure that the IP address resolution constantly occurs 

# Todo List:
- Make Raspberry Pi Temp/Memory(RAM & Disk)monitoring script (plot w/ matlibplot)(Andrew) https://modberry.techbase.eu/raspberry-pi/how-to-check-raspberry-pi-memory-usage-in-4-easy-steps/
Find a way for us to remotely monitor the historical values.
- Once Docker Image is available, make sure that it can connect to the database consistently, and test adding sensors in the configuration file (Alyssa)
- Start long-term monitoring of running system (Everyone)
- Make sure Home Assistant Supervised restarts when the pi is turned off
- Figure out platform error: "WARNING: The requested image's platform (linux/arm64/v8) does not match the detected host platform (linux/amd64/v3) and no specific platform was requested"
- Note on platform error: the container still ran and gathered data, but I don't know what trouble the error could end up causing later down the line
- Figure out docker network (name is host) and how to add DNS resolution (Grant)
- Show the system writing to the database and toggling actuators (ask Liya about this Monday)
- Make sure that commonly created/deleted files (flag .txt files) aren't written to SD card, and are stored in RAM (Grant)
- Remote operation? I am not quite sure what he means by this. From Chien: **"The Raspberry Pi will be installed remotely in real applications. We need to be able to operate it remotely through the internet. We cannot use the default port provided by the home assistant. How to ensure the access is secure (like needing a password on the edge computer)"**
- See about changing any commonly created text files to go to the /tmp directory instead, which will ensure that nothing is written to the SD card. Make this the volume location. (Grant) 
  

