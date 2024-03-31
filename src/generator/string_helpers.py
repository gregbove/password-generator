import hashlib
import logging
from exception_messages import STRING_CAN_NOT_BE_NULL_OR_EMPTY


def calculate_hash(string: str) -> str:
    """
    Returns SHA-256 value of a string.
    """
    if len(string) < 1:
        raise Exception(STRING_CAN_NOT_BE_NULL_OR_EMPTY)

    # Hash the string using SHA-256
    hashed_string = hashlib.sha256(string.encode()).hexdigest()
    
    return hashed_string

def get_first_x(string: str, n: int) -> str:
    """
    Returns the first N characters of a given string.
    """
    # Log warning if string length is greater than the input
    if len(string) < n:
        logging.warning(len(string))

    return string[:n]