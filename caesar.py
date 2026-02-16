def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():  # Encrypt only alphabet characters
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char  # Keep spaces and symbols unchanged
            
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is reverse shift


# ---- Main Program ----
print("=== Caesar Cipher Program ===")

message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))

choice = input("Type 'E' for Encryption or 'D' for Decryption: ").upper()

if choice == 'E':
    encrypted_text = encrypt(message, shift_value)
    print("Encrypted Message:", encrypted_text)

elif choice == 'D':
    decrypted_text = decrypt(message, shift_value)
    print("Decrypted Message:", decrypted_text)

else:
    print("Invalid choice! Please select E or D.")
