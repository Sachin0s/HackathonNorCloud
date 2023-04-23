import os

def fetch_log_data(file_path):
    with open(file_path, 'r') as logfile:
        log_data = logfile.read()
    return log_data
    print("The latest data have been fetched from the log file")
    