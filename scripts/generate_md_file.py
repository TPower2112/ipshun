# # Import the hashlib module
# import hashlib

# # Define the name and the original hash of the text file
# filename = "ipshun.txt"
# original_hash = "d41d8cd98f00b204e9800998ecf8427e"

# # Define a function to check the MD5 hash of a file
# def check_md5(filename, original_hash):
#     # Open the file in binary mode and read its contents
#     with open(filename, "rb") as f:
#         data = f.read()
#     # Calculate the MD5 hash of the data
#     md5_hash = hashlib.md5(data).hexdigest()
#     # Compare the hash with the original or expected value
#     return md5_hash == original_hash

# # Call the function and print the result
# result = check_md5(filename, original_hash)
# # True or False
# print(result)

# # Define a function to export the MD5 hash of a file
# def export_md5(filename):
#      # Open the file in binary mode and read its contents
#      with open(filename, "rb") as f:
#          data = f.read()
#      # Calculate the MD5 hash of the data
#      md5_hash = hashlib.md5(data).hexdigest()
#      print(md5_hash)
#      # Create a new file with the .md5 extension
#      with open(filename + ".md5", "w") as f:
#          # Write the hash to the new file
#          f.write(md5_hash)
#      # Return the hash value
#      return md5_hash
# result = export_md5(filename)
import hashlib

f = open('ipshun.txt','rb')
m = hashlib.md5()
while True:
    ## Don't read the entire file at once...
    data = f.read(10240)
    if len(data) == 0:
        break
    m.update(data)
md5_hash = m.hexdigest()
print(md5_hash)
