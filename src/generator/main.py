import argparse
import pyperclip
from auth import get_universal_password
from engine import generate_platform_password

def main():
    """
    Generate hashed passwords for different platforms based on a single known password 
    """

    parser = argparse.ArgumentParser(description='Generate hashed passwords for different platforms.')
    parser.add_argument('platform_name', type=str, help='Platform name')
    
    args = parser.parse_args()

    universal_password = get_universal_password()

    platform_password = generate_platform_password(universal_password, args.platform_name)

    # Copy the password to the clipboard
    pyperclip.copy(platform_password)
    print("Hashed password copied to clipboard.")

if __name__ == "__main__":
    main()