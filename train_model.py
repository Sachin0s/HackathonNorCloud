from sklearn.tree import DecisionTreeClassifier
import pandas as pd

def train_classifier():
    # Load the error data
    error_data = pd.read_csv('error_data.csv')

    # Define a function to determine the criticality based on the error code
    def determine_criticality(error_code):
        error_code_str = str(error_code)
        if error_code_str.startswith('5'):
            return 'critical'
        elif error_code_str.startswith('4'):
            return 'medium'
        else:
            return 'low'

    # Add the 'criticality' column and populate it using the determine_criticality function
    error_data['criticality'] = error_data['error_code'].astype(str).apply(determine_criticality)

    # Change the column name to 'critical'
    error_data = error_data.rename(columns={'criticality': 'critical'})

    # Save the updated DataFrame to a new CSV file
    error_data.to_csv('error_data.csv', index=False)

    # Extract features from timestamp
    error_data['timestamp'] = pd.to_datetime(error_data['timestamp'])
    error_data['hour'] = error_data['timestamp'].dt.hour
    error_data['day_of_week'] = error_data['timestamp'].dt.dayofweek

    # Map error codes to integers
    error_code_mapping = {code: i for i, code in enumerate(error_data['error_code'].unique())}
    error_data['error_code'] = error_data['error_code'].map(error_code_mapping)

    # Train the decision tree classifier
    clf = DecisionTreeClassifier()
    clf.fit(error_data[['hour', 'day_of_week', 'error_code']], error_data['critical'])

    return clf