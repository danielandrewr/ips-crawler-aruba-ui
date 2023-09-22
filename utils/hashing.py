import hashlib


def create_hash(data):
    """
    Create a SHA-256 hash value for the given data.

    This function takes input data and returns its SHA-256 hash value in hexadecimal format.
    The input data can be of any type; it will be converted to bytes before hashing.

    Args:
        data (bytes, str, int, float, etc.): The input data to be hashed.

    Returns:
        str: The SHA-256 hash value of the input data in hexadecimal format.
    """
    # Convert the data to bytes if it's not already in bytes
    if not isinstance(data, bytes):
        data = str(data).encode()

    # Create a hash object using SHA-256 algorithm
    hash_object = hashlib.sha256()

    # Update the hash object with the data
    hash_object.update(data)

    # Get the hexadecimal representation of the hash
    hash_value = hash_object.hexdigest()

    return hash_value
