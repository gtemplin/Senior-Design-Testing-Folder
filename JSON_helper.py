import json
import re

entity = input("Enter your entitity ID: ")
port_type = entity.split('.')[0]

entity_words = re.split('[^a-zA-Z0-9]+', entity)
print(f"Pieces of the entity: {entity_words}")
print("The first part of the words above will be your node name (where the sensor is at)")
print("The second part will be what your port is measuring")


JSON_structure = f"""
{{
      "NodeName": "first_part",
      "SensorPortLabel": "?",
      "PortType": "{port_type}",
      "PortName": "second_part",
      "SensorType": "?",
      "InputValueUnitName": "?",
      "InputValueUnitSymbol": "?",
      "BrandName": "?",
      "AssociatedRaspberryPiUnit": "?",
      "Network Source": "?"  ,
      "AttachedToEquipment": "?",
      "SensorModel": "?",
      "InputValueLowerBound": null,
      "InputValueUpperBound": null,
      "InputMeaningLowerBound": null,
      "InputMeaningUpperBound": null,
      "PollingIntervalInSeconds": null,
      "FilterMethod": 1,
      "PreviousSampleTime": 0,
      "NumValuesCollected": 0,
      "ProcessedValue": 0,
      "Calibration": 1,
      "IsDataReadyToSent": 0
}}
"""

# Note the double curly braces {{ and }} around the JSON structure.
# This is necessary because curly braces have special meaning in f-strings,
# and doubling them escapes them to be included in the string output.


print(f"Your structure \n{JSON_structure}")