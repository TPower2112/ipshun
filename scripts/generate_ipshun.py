import csv
from datetime import datetime

# Function to filter and write IP addresses to a text file
def filter_ips(csv_file_path, output_file_path):
    # Get today's date
    today = datetime.now().date()

    # List to hold non-expired IP addresses
    valid_ips = []

    # Read the CSV file
    with open(csv_file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)

        # Process each row in the CSV
        for row in csvreader:
            # Parse the expiry date from the CSV
            expiry_date = datetime.strptime(row['Expiry Date'], '%Y-%m-%d').date()

            # Check if the IP address has not expired
            if expiry_date > today:
                valid_ips.append(row['IP Address'])

    # Write the non-expired IP addresses to a text file
    with open(output_file_path, 'w') as file:
        for ip in valid_ips:
            file.write(ip + '\n')

# Specify the CSV file path and the output file path
csv_file_path = 'index/index.csv'
output_file_path = 'ipshun.txt'

# Call the function with the file paths
filter_ips(csv_file_path, output_file_path)