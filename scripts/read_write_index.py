import csv
from datetime import datetime, timedelta

# Function to write data to CSV
def write_to_csv(file_path, ip_addresses):
    # Calculate today's date and expiry date
    today = datetime.now()
    expiry_date = today + timedelta(days=30)

    # Open the CSV file in write mode
    with open(file_path, 'w', newline='') as csvfile:
        # Create a CSV writer object
        csvwriter = csv.writer(csvfile)

        # Write the header
        csvwriter.writerow(['IP Address', 'Today\'s Date', 'Expiry Date'])

        # Write the data rows
        for ip in ip_addresses:
            csvwriter.writerow([ip, today.strftime('%Y-%m-%d'), expiry_date.strftime('%Y-%m-%d')])

# Read IP addresses from a text file
with open('tinesip5.txt', 'r') as file:
    ip_addresses = file.read().splitlines()

# Write the data to a CSV file
write_to_csv('index/index.csv', ip_addresses)