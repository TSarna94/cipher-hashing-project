def decode_message(message):
    """
    Decodes a message that was encoded with a Caesar cipher shift of 15.
    """
    decoded = ""
    for char in message:
        decoded += unshift_char(char)
    return decoded

def shift_char(char):
    """
    Shifts a single character by 15 positions using a Caesar cipher.
    Letters are shifted within their case (uppercase/lowercase).
    Non-letter characters are returned unchanged.
    """
    # If it's not a letter (space, punctuation, number), return it unchanged
    if not char.isalpha():
        return char

    # Determine ASCII base depending on case
    # 'a' = 97 for lowercase, 'A' = 65 for uppercase
    if char.islower():
        base = ord('a')
    else:
        base = ord('A')

    # Convert letter to 0–25 range
    position = ord(char) - base

    # Shift by 15 positions and wrap around using modulus
    new_position = (position + 15) % 26

    # Convert back to ASCII
    new_char = chr(base + new_position)
    return new_char

def unshift_char(char):
    """
    Reverses the Caesar cipher shift of 15.
    Letters are shifted backward within their case.
    Non-letter characters are returned unchanged.
    """
    if not char.isalpha():
        return char

    if char.islower():
        base = ord('a')
    else:
        base = ord('A')

    position = ord(char) - base

    # Reverse the shift
    new_position = (position - 15) % 26

    return chr(base + new_position)

def encode_message(message): 
    """
    Encodes an entire message using the Caesar cipher shift of 15.
    Loops through each character and applies shift_char().
    """
    encoded = ""
    for char in message:

        encoded += shift_char(char)
    return encoded

# --- Program Start ---
print("\n=== Caesar Cipher Tool ===")

while True:
    print("\nChoose an option:")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        user_message = input("\nEnter a message to encode: ")
        encoded = encode_message(user_message)
        print("\nEncoded message:", encoded)

    elif choice == "2":
        user_message = input("\nEnter a message to decode: ")
        decoded = decode_message(user_message)
        print("\nDecoded message:", decoded)

    elif choice == "3":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")
