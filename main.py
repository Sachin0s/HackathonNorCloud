import os
import csv
from fetch_log import fetch_log_data
from detect_error import detect_error
from call_ansible import call_ansible
from train_model import train_classifier
from anomaly_detection import detect_anomalies
from mapping import error_to_playbook_mapping



# Define the paths to the log file and playbook directory
file_path = "/home/anitek/anomaly_detection/ErrorLog_DB.txt"
playbook_dir = "/home/anitek/anomaly_detection"



# Step 1: Load the log data
print("Step 1: Reading the log file")
log_data = fetch_log_data(file_path)
print("The latest log file was loaded")





# Step 2: Detect errors in the log data and trigger the corresponding Ansible playbooks
print("Step 2: Errors are being detected")
errors = detect_error(log_data, playbook_dir, error_to_playbook_mapping)
#if errors:
for error in errors:





#Step 3: Ansible Playbook Triggerred for corrective action
    print("Step 3: Ansible Playbook Triggerred for corrective actions")

    call_ansible(playbook_dir, error["error_code"])

    print("Corrective Actions taken")




# Step 4: Train the ML classifier on the log data


print("Step 4: Model Training initiated")
clf = train_classifier()
print("Model Training Completed")




# Step 5: Predict anomalies in the log data using the trained model


print("Step 5: ML Based Suggestive Actions Module Initiated")
#detect_anomalies()

print("Actions Suggested:")



print("Process Completed Successfully")