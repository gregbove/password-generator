import argparse
import pyperclip
from engine import generate_password

def main():
    """
    Generate hashed passwords for different platforms based on a single known password 
    """

    parser = argparse.ArgumentParser(description='Generate hashed passwords for different platforms.')
    parser.add_argument('universal_password', type=str, help='The Universal Password')
    parser.add_argument('platform_name', type=str, help='Platform name')
    
    args = parser.parse_args()
    
    password = generate_password(args.universal_password, args.platform_name)

    # Copy the password to the clipboard
    pyperclip.copy(password)
    print("Hashed password copied to clipboard.")

if __name__ == "__main__":
    main()