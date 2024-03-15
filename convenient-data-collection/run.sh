#!/bin/bash

# Build and run the container. Use the host network for easier communication with homeassistant container 
docker build -t test:test .
docker run --name test --network host -v /home/admin/senior-design-testing-folder/local-volume:/usr/src/app/BackupData -it test:test /bin/bash


# Path to the 'cleaned' file
cleaned_file="cleaned"

# Check if the 'cleaned' file does not exist, is empty, or contains "True"
if [ ! -f "$cleaned_file" ] || [ ! -s "$cleaned_file" ] || [ "$(cat $cleaned_file)" = "True" ]; then
    # If the file doesn't exist, is empty, or contains "True", set it to "False"
    echo "False" > "$cleaned_file"
    echo "'cleaned' was not set to 'False', now set to 'False'"
else
    # If none of the above conditions are met, it implies the file exists, is not empty, and does not contain "True"
    echo "The 'cleaned' file was already set and does not contain 'True'."
fi





# # Build and run the container
# docker build -t test:test .
# docker run --name test -v /home/admin/senior-design-testing-folder/local-volume:/usr/src/app/BackupData -it test:test /bin/bash

# # Check if cleaned is not set or is empty
# if [ -z "$cleaned" ]; then
#   # cleaned is not set or is empty, define and export it
#     cleaned="False"
#     export cleaned # make variable available to clean.sh
#     echo "cleaned was not set, now set to 'False'"
# else
#   # cleaned was already set, so just ensure it's set to false 
#     export cleaned = "False"
# fi

# # --network=host    <-- The network used by home assistant 