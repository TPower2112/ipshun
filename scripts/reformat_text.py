# Function to clean IP addresses and write them to a new file
def clean_ip_addresses(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        # Read the contents of the file
        content = file.read()

    # Remove commas and split the content into individual IP addresses
    ip_addresses = content.replace(',', '').split()

    # Write each IP address on a single line in the output file
    with open(output_file_path, 'w') as file:
        for ip in ip_addresses:
            file.write(ip + '\n')

# Specify the input and output file paths
input_file_path = 'tinesip5.txt'
output_file_path = 'cleaned_ips.txt'

# Call the function with the file paths
clean_ip_addresses(input_file_path, output_file_path)