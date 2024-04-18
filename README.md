# Senior-Design-Testing-Folder

## Links
- Edging PC 1: TBD
- Edging PC 2: http://134.68.225.201:8123
- Username is 'admin2' password is 'admin'

## Things to add to the final readme
- Current DockerHub link. Should probably make an official IAC account at some point
- Command to run in order to build the image
- Command to run in order to create a container that will work with the system 


### Raspberry Pi SSH Login
- admin@134.68.225.201
- password = admin
- On windows powershell, use this command to reset the host ssh connection: ssh-keygen -R 134.68.225.201
- https://www.raspberrypi-spy.co.uk/2014/08/how-to-reset-a-forgotten-raspberry-pi-password/ <-- how to fix pi password error by fucking w/ the SD card

### A note on python
- To run in the background and save stdout to a file, run 'nohup python3 script.py &'
- this will save stdout to a file called nohup.out

### Link to UI to Database
- https://in-engr-cymanii.engr.iupui.edu/TestEnvFlask/login
- Username = SystemAdmin
- Password = SystemAdmin

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
- Figure out platform error: "WARNING: The requested image's platform (linux/arm64/v8) does not match the detected host platform (linux/amd64/v3) and no specific platform was requested"
- Show the system writing to the database and toggling actuators (ask Liya about this Monday)

#Info for EdgingPC1
- IP Address: 134.68.225.200
- Home Assistant Login
- - Username: SystemAdmin
- - Password: SystemAdmin
