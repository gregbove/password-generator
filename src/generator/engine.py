from string_helpers import calculate_hash, get_first_x
from constants import PASSWORD_HASH_LENGTH, RULE_SATISFYING_STRING

def generate_password(universal_password: str, platform_name: str) -> str:
    # Calculate hash value 
    value_to_hash = universal_password + platform_name
    hash_value = calculate_hash(value_to_hash)

    # Shorten the hash so that password is not incredibly long
    shortened_hash_value = get_first_x(hash_value, PASSWORD_HASH_LENGTH)

    # Add rule satisfying string to password to ensure acceptance
    password = shortened_hash_value + RULE_SATISFYING_STRING

    return password