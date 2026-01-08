import os
from cryptography.fernet import Fernet

def generate_key():
    """Generates a key and saves it into the 'secret.key' file."""
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("Key generated and saved to 'secret.key'.")
    else:
        print("Key already exists. Skipping generation.")

def load_key():
    """Loads the key from the 'secret.key' file."""
    if not os.path.exists("secret.key"):
        print("Error: 'secret.key' not found. Please generate a key first.")
        return None
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    """Encrypts the given file using the key."""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)
    
    # Prepend 'encrypted_' to the original filename
    dirname, basename = os.path.split(filename)
    encrypted_filename = os.path.join(dirname, "encrypted_" + basename)
    
    with open(encrypted_filename, "wb") as file:
        file.write(encrypted_data)
    
    print(f"File '{filename}' encrypted successfully to '{encrypted_filename}'.")

def decrypt_file(filename, key):
    """Decrypts the given file using the key."""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except Exception as e:
        print(f"Error decrypting file: {e}")
        return

    # Create decrypted filename. 
    # If filename starts with 'encrypted_', remove it to restore partially. 
    # But usually user asks to just decrypt back. 
    # Let's add 'decrypted_' prefix to avoid overwriting unless intended.
    dirname, basename = os.path.split(filename)
    if basename.startswith("encrypted_"):
        decrypted_basename = "decrypted_" + basename[10:] # remove 'encrypted_'
    else:
        decrypted_basename = "decrypted_" + basename
        
    decrypted_filename = os.path.join(dirname, decrypted_basename)
    
    with open(decrypted_filename, "wb") as file:
        file.write(decrypted_data)
        
    print(f"File '{filename}' decrypted successfully to '{decrypted_filename}'.")

def main():
    while True:
        print("\n--- File Encryptor/Decryptor ---")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            generate_key()
        elif choice == '2':
            key = load_key()
            if key:
                filename = input("Enter the filename to encrypt: ").strip('"') # strip quotes if user did drag-drop
                encrypt_file(filename, key)
        elif choice == '3':
            key = load_key()
            if key:
                filename = input("Enter the filename to decrypt: ").strip('"')
                decrypt_file(filename, key)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
