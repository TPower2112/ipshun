# Import the csv module
import csv

# Open the text file and the CSV file
text_file = open('tines/ipshun.txt', 'r')
csv_file = open('index/index.csv', 'w', newline='')

# Create a csv.writer object
writer = csv.writer(csv_file)

# Read the text file line by line and write to the CSV file
for line in text_file:
    # Split the line by whitespace to get the fields
    fields = line.split()
    # Write the fields as a row to the CSV file
    writer.writerow(fields)

# Close the files
text_file.close()
csv_file.close()
