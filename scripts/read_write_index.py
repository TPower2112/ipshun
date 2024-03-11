import csv
from datetime import datetime, timedelta

# Function to append data to CSV
def append_to_csv(input_file_path, csv_file_path):
    # Calculate today's date and expiry date
    today = datetime.now()
    expiry_date = today + timedelta(days=30)

    # Read IP addresses from the input text file
    with open(input_file_path, 'r') as file:
        ip_addresses = file.read().splitlines()

    # Open the CSV file in append mode
    with open(csv_file_path, 'a', newline='') as csvfile:
        # Create a CSV writer object
        csvwriter = csv.writer(csvfile)

        # Write the data rows
        for ip in ip_addresses:
            csvwriter.writerow([ip, today.strftime('%Y-%m-%d'), expiry_date.strftime('%Y-%m-%d')])

# Specify the input text file path and the CSV file path
input_file_path = 'cleaned_ips.txt'
csv_file_path = 'index/index.csv'

# Call the function with the file paths
append_to_csv(input_file_path, csv_file_path)