#!/bin/bash

# Home Assistant API endpoint for getting the configuration
#HA_ENDPOINT="http://homeassistant.local:8123/api/config"
#HA_ENDPOINT="http://134.68.225.201:8123/api/config"
HA_ENDPOINT="http://localhost:8123/api/config" # can use localhost, which will work regardless of internet connection 
SENSOR_ENDPOINT="http://localhost:8123/api/states/" # ./states gives statuses/readings from sensors in the network 
TOGGLE_ENDPOINT="http://localhost:8123/api/services/switch/toggle" # ./services/switch/toggle sends an actual toggle request to some switch in the network

# Your Long-Lived Access Token
ACCESS_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0NDc4M2I2NGY0NGQ0YzhiODQ4OTkwNmE4NmEzMTY3NCIsImlhdCI6MTcxMDc4NTYzMSwiZXhwIjoyMDI2MTQ1NjMxfQ.svQMfjToDbpfI2wXrld6jdKx_nb62x3rJYj5Ebmy65E"
# Function to test connectivity to the Home Assistant API
test_api_connectivity() {
    response=$(curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer ${ACCESS_TOKEN}" \
              -H "Content-Type: application/json" \
              "${HA_ENDPOINT}")

    if [ "$response" -eq 200 ]; then
        echo "Success: Connected to the Home Assistant API."
    else
        echo "Error: Failed to connect to the Home Assistant API. HTTP Status Code: ${response}"
    fi
}


# read a sensor's data using the api
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
toggle_switch(){
	SWITCH_ENTITY_ID="$1"
	# Assuming ACCESS_TOKEN is already set in your environment
	response=$(curl -s -X POST -H "Authorization: Bearer ${ACCESS_TOKEN}" \
	                     -H "Content-Type: application/json" \
	                     -d "{\"entity_id\": \"${SWITCH_ENTITY_ID}\"}" \
	                     http://localhost:8123/api/services/switch/toggle)

	if echo "$response" | grep -q "id"; then
		echo "Success: The switch has been toggled."
	else
		echo "Didn't toggle any switch"
	fi
}


# Main script execution
test_api_connectivity

# echo "Input the entity id: "
# read entity
# SENSOR_CURL="$SENSOR_ENDPOINT$entity"
# echo "URL: $SENSOR_CURL" 
# read_sensor_data $SENSOR_CURL
# toggle_switch $entity

# toggle_switch "switch.mini_smart_plug_2"


# 
#