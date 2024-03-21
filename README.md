# Senior-Design-Testing-Folder
### Raspberry Pi SSH Login
- admin@134.68.225.201
- password = admin
- On windows powershell, use this command to reset the host ssh connection: ssh-keygen -R 134.68.225.201
- https://www.raspberrypi-spy.co.uk/2014/08/how-to-reset-a-forgotten-raspberry-pi-password/ <-- how to fix pi password error by fucking w/ the SD card

### A note on python
- To run in the background and save stdout to a file, run 'nohup python3 script.py &'
- this will save stdout to a file called nohup.out


### Some Docker Notes
- Docker initially requires sudo access
- To allow a user to run docker commands w/o sudo: sudo usermod -aG docker username
- Home assistant is on the host network, so can make http requests to http://localhost:8123
- Should be able to set the IP address just to 'localhost'
- /etc/systemd/resolved.conf needs to have 'NS=8.8.8.8 8.8.4.4' added to it in order to use the ping command 

### Raspberry Pi Directory Structure 
- Everything will be based in the admin's home directory (just input 'cd' to get here once logged in)

### Successful HASAPI http request:
- http://localhost:8123/api/states/sensor.multisensor_6_air_temperature
- <entity_id> = sensor.multisensor_6_air_temperature
- This is for a sensor not an actuator

### Home Assistant API Token:
-eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0NDc4M2I2NGY0NGQ0YzhiODQ4OTkwNmE4NmEzMTY3NCIsImlhdCI6MTcxMDc4NTYzMSwiZXhwIjoyMDI2MTQ1NjMxfQ.svQMfjToDbpfI2wXrld6jdKx_nb62x3rJYj5Ebmy65E

### Note on DNS
- Home assistant is using it's own network called 'host', which doesn't have a DNS setup
- This means we won't be able to use the local DNS and will have to make sure that the IP address resolution constantly occurs 

# Todo List:
- Once Docker Image is available, make sure that it can connect to the database consistently, and test adding sensors in the configuration file (Alyssa)
- Start long-term monitoring of running system (Everyone)
- Make sure Home Assistant Supervised restarts when the pi is turned off
- Figure out platform error: "WARNING: The requested image's platform (linux/arm64/v8) does not match the detected host platform (linux/amd64/v3) and no specific platform was requested"
- Note on platform error: the container still ran and gathered data, but I don't know what trouble the error could end up causing later down the line
- Figure out docker network (name is host) and how to add DNS resolution (Grant)
- Show the system writing to the database and toggling actuators (ask Liya about this Monday)


  

