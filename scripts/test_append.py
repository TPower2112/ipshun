import csv
from datetime import datetime

def main(input):
    # Get the current date in YYYY-MM-DD format
    entry_date = datetime.now().strftime('%Y-%m-%d')

    # Open the file in append mode
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)

        # Write the IP address and entry date to the CSV
        writer.writerow([ip_address, entry_date])
    return {"result": 'The ip address submitted was: '+ ip_address}
# Example usage:
main(input)
