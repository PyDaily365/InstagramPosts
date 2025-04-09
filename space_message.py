# Space message encoder/decoder
def encode_message(message):
    """Turn a message into secret hex code"""
    return message.encode("utf-8").hex()

def decode_message(hex_code):
    """Reveal the secret message from hex"""
    try:
        return bytes.fromhex(hex_code).decode("utf-8")
    except:
        return "Oops! Invalid hex code."

# Space-themed message
space_msg = "Mars Rover to Earth: All systems green!"

# Encode it
secret_code = encode_message(space_msg)
print("Secret Code Sent:", secret_code)

# Decode it
revealed = decode_message(secret_code)
print("Message Received:", revealed)

# Try your own!
your_msg = input("Type your space message: ")
your_code = encode_message(your_msg)
print("Your Secret Code:", your_code)
print("Decoded Back:", decode_message(your_code))