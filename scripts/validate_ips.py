import ipaddress

def verify_and_write_ipv4(file_path, output_file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(output_file_path, 'w') as output_file:
        for line in lines:
            line = line.strip()  # Remove any leading/trailing whitespace
            try:
                # This will raise a ValueError if the address is not a valid IPv4 address
                ipaddress.IPv4Address(line)
                output_file.write(line + '\n')  # Write the valid IP to the output file
            except ValueError:
                continue  # Skip the line if it's not a valid IPv4 address

# Usage
input_file_path = 'cleaned_ips.txt'
output_file_path = 'valid_ips.txt'
verify_and_write_ipv4(input_file_path, output_file_path)
