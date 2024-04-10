from string_helpers import calculate_hash, get_first_x
from constants import RULE_SATISFYING_STRING, get_env_var
import os

def generate_platform_password(universal_password: str, platform_name: str) -> str:
    # Calculate hash value 
    value_to_hash = universal_password + platform_name
    hash_value = calculate_hash(value_to_hash)

    # Shorten the hash so that password is not incredibly long
    password_hash_length = get_env_var('PASSWORD_HASH_LENGTH')
    hash_length = int(password_hash_length)

    shortened_hash_value = get_first_x(hash_value, hash_length)

    # Add rule satisfying string to password to ensure acceptance
    password = shortened_hash_value + RULE_SATISFYING_STRING

    return password