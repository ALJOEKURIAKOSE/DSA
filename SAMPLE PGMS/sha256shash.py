import hashlib

def generate_sha256_hash(input_string):
    # Encode the input string
    encoded_input = input_string.encode()
    
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    
    # Update the hash object with the encoded input
    sha256_hash.update(encoded_input)
    
    # Retrieve the hexadecimal representation of the hash
    hex_digest = sha256_hash.hexdigest()
    
    return hex_digest

# Example usage
input_string = "aljoe"
hash_value = generate_sha256_hash(input_string)
print(f"SHA-256 hash of '{input_string}': {hash_value}")
