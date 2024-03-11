import hashlib

def get_md5_hash(file_path):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Usage
file_path = 'ipshun.txt'
md5_hash = get_md5_hash(file_path)
print(f'The MD5 hash of the file is: {md5_hash}')