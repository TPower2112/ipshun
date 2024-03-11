import os

# Specify the path to the file you want to delete
file_path = 'tinesip.txt'

# Check if the file exists
if os.path.exists(file_path):
    # Delete the file
    os.remove(file_path)
    print(f"The file {file_path} has been deleted.")
else:
    print(f"The file {file_path} does not exist.")

