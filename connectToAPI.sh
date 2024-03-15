#!/bin/bash

# Home Assistant API endpoint for getting the configuration
#HA_ENDPOINT="http://homeassistant.local:8123/api/config"
#HA_ENDPOINT="http://134.68.225.201:8123/api/config"
HA_ENDPOINT="http://localhost:8123/api/config"

# Your Long-Lived Access Token
ACCESS_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI5ZTQyN2FkMWM0Zjc0ODVlYWY0NDQyMGQxOGZlNTU5YiIsImlhdCI6MTcxMDUyNTg4NCwiZXhwIjoyMDI1ODg1ODg0fQ.2r0fsMJor0xTm0rleNAi1A-JvtDhIOmiG_5lCdqElmY"

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

# Main script execution
test_api_connectivity





