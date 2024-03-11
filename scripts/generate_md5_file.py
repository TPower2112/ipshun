# Import the hashlib module
import hashlib

# Define the name and the original hash of the text file
filename = "ipshun.txt"
original_hash = "6ee6e0077f085e4d02ea20b06f0f2d40"

# Define a function to check the MD5 hash of a file
def check_md5(filename, original_hash):
    # Open the file in binary mode and read its contents
    with open(filename, "rb") as f:
        data = f.read()
    # Calculate the MD5 hash of the data
    md5_hash = hashlib.md5(data).hexdigest()
    # Compare the hash with the original or expected value
    return md5_hash == original_hash

# Call the function and print the result
result = check_md5(filename, original_hash)
# True or False
print(result)

# Define a function to export the MD5 hash of a file
def export_md5(filename):
     # Open the file in binary mode and read its contents
     with open(filename, "rb") as f:
         data = f.read()
     # Calculate the MD5 hash of the data
     md5_hash = hashlib.md5(data).hexdigest()
     print(md5_hash)
     # Create a new file with the .md5 extension
     with open(filename + ".md5", "w") as f:
         # Write the hash to the new file
         f.write(md5_hash)
     # Return the hash value
     return md5_hash
result = export_md5(filename)

# import hashlib

# def generate_md5_checksum(file_path):
#     """Generate an MD5 checksum for the given file and save it to a .md5 file."""
#     hash_md5 = hashlib.md5()
#     with open(file_path, "rb") as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             hash_md5.update(chunk)
#     return hash_md5.hexdigest()

# # Specify the path to the FMC Customer Security Intelligence Feed
# file_path = 'ipshun.txt'

# # Generate MD5 checksum
# md5_checksum = generate_md5_checksum(file_path)

# # Save the MD5 checksum to a .md5 file
# md5_file_path = file_path + '.md5'
# with open(md5_file_path, 'w') as f:
#     f.write(md5_checksum)

# print(f'MD5 checksum saved to {md5_file_path}')
