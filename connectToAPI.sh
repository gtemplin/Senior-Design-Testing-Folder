#!/bin/bash

# Home Assistant API endpoints for making requests
HA_ENDPOINT="http://localhost:8123/api/config" # can use localhost, which will work regardless of internet connection 
SENSOR_ENDPOINT="http://localhost:8123/api/states/" # ./states gives statuses/readings from sensors in the network 
TOGGLE_ENDPOINT="http://localhost:8123/api/services/switch/toggle" # ./services/switch/toggle sends an actual toggle request to some switch in the network

# Your Long-Lived Access Token
ACCESS_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0NDc4M2I2NGY0NGQ0YzhiODQ4OTkwNmE4NmEzMTY3NCIsImlhdCI6MTcxMDc4NTYzMSwiZXhwIjoyMDI2MTQ1NjMxfQ.svQMfjToDbpfI2wXrld6jdKx_nb62x3rJYj5Ebmy65E"


# Function to test connectivity to the Home Assistant API
# 0 indicates success, -1 indicates failure (to connect to the API)
test_api_connectivity() {
    response=$(curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer ${ACCESS_TOKEN}" \
              -H "Content-Type: application/json" \
              "${HA_ENDPOINT}")

    if [ "$response" -eq 200 ]; then
        echo "Success: Connected to the Home Assistant API."
	return 0
    else
        echo "Error: Failed to connect to the Home Assistant API. HTTP Status Code: ${response}"
	return -1
    fi
}


# read a sensor's data using the api
# The user input is the SENSOR_ENDPOINT environment variable + the specific entity ID
read_sensor_data(){
	USER_IN="$1"
	response=$(curl -s -H "Authorization: Bearer ${ACCESS_TOKEN}" \
                     -H "Content-Type: application/json" \
                     "${USER_IN}")

	if [ -n "$response" ]; then
        	echo "Success: Received data from the sensor."
        	echo "Sensor Value: ${response}"
    	else
        	echo "Error: Failed to get data from the sensor."
    	fi
}


# toggle the switch
# TOGGLE_ENDPOINT is the general URL for sending toggle requests
# SWITCH_ENTITY_ID is the actual switching entity that the user will pass in 
toggle_switch(){
	SWITCH_ENTITY_ID="$1"
	# Assuming ACCESS_TOKEN is already set in your environment
	response=$(curl -s -X POST -H "Authorization: Bearer ${ACCESS_TOKEN}" \
	                     -H "Content-Type: application/json" \
	                     -d "{\"entity_id\": \"${SWITCH_ENTITY_ID}\"}" \
	                     "${TOGGLE_ENDPOINT}")

	if echo "$response" | grep -q "id"; then
		echo "Success: The switch has been toggled."
	else
		echo "Didn't toggle any switch"
	fi
}


#################### Main script execution ########################

# Determine if the API is reachable
success=$(test_api_connectivity)
status=$?

# If the API was reachable, get user input
# Starting the input with 'sensor' will go to some sensor and retrieve it's value
# Starting the input with 'switch' will toggle the switch you input 
if [ $status -eq 0 ]; then
	echo "Input the entity id: "
	read entity

	# Check if the entity is a sensor or is toggled 
	if [[ $entity == sensor* ]]; then
		# Get sensor data
    		echo "Input starts with 'sensor'"
		SENSOR_CURL="$SENSOR_ENDPOINT$entity"
		echo "URL: $SENSOR_CURL" 
		read_sensor_data $SENSOR_CURL

	elif [[ $entity == switch* ]]; then
		# Toggle a switch 
   		echo "Input starts with 'toggle'"
		SWITCH_CURL="${TOGGLE_ENDPOINT}/${entity}"
		echo "URL: $SWITCH_CURL"
		toggle_switch $entity # the switching syntax only needs to be passed the entity you are switching 

	else
    		echo "Input should start with 'sensor' or 'switch'"

	fi

else
	echo "Failed to fetch data."
fi



# toggle_switch $entity

# toggle_switch "switch.mini_smart_plug_2"


# 
#
