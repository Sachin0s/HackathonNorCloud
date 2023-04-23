import re
import os
import csv
from mapping import error_to_playbook_mapping



def detect_error(log_data, playbook_dir, error_to_playbook_mapping):
    errors = []
    # Define empty lists to store timestamp and error code data
    timestamp_data = []
    error_code_data = []
    # Define the regular expression pattern to match the log text
    pattern = r'^(\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}:\d{2})\s*(\w+)\s*:\.*(\w+):\s(.*)$'

    # Loop through each line in the log data
    for line in log_data.split('\n'):
        # Match the pattern against the log text
        match = re.search(pattern, line)

        # Check if a match was found
        if match:
            timestamp = match.group(1)
            log_level = match.group(2)
            error_code = match.group(3)
            error_message = match.group(4)

            if(log_level=="ERROR"):
                # Find matching playbook files in the playbook directory
                playbook_files = []
                for error_code in error_to_playbook_mapping:
                    if error_code in error_message:
                        playbook_file = os.path.join(playbook_dir, error_to_playbook_mapping[error_code])
                        playbook_files.append(playbook_file)
                        break
                 # Print the results
                print(f"Timestamp: {timestamp}")
                print(f"Log level: {log_level}")
                print(f"Error code: {error_code}")
                print(f"Error message: {error_message}")
            if("out of" in error_message):
                sql_state = error_message.split(" ")[-1]
                error_code=sql_state
                print("Found")
                # If no matching playbook files are found, skip to the next line
                # Combine the data into a list of tuples
                 # Append the timestamp and error code data to the lists
                timestamp_data.append(timestamp)
                error_code_data.append(error_code)
                data = list(zip(timestamp_data, error_code_data))

                # Write the data to a CSV file
                with open('error_data.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['timestamp', 'error_code'])  # Write header row
                    writer.writerows(data)  # Write data rows

                print("CSV file created successfully!")

                if not playbook_files:
                    continue

                # Add the error information to the list of errors
                errors.append({
                    'timestamp': timestamp,
                    'log_level': log_level,
                    'error_code': error_code,
                    'error_message': error_message,
                    'playbook_files': playbook_files
                })
    return errors