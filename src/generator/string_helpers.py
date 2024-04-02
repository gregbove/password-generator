import hashlib

def calculate_hash(string: str) -> str:
    """
    Returns SHA-256 value of a string.
    """
    # Hash the string using SHA-256
    hashed_string = hashlib.sha256(string.encode()).hexdigest()
    
    return hashed_string

def get_first_x(string: str, n: int) -> str:
    """
    Returns the first N characters of a given string.
    """

    return string[:n]