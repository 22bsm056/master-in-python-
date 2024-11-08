import random

# Define random characters pool
rand = "abcdefghijklmnopqrstuvwxyz"

# Function for encoding
def encode(word):
    if len(word) < 3:
        # If the word has fewer than 3 characters, simply reverse it
        return word[::-1]
    else:
        # Remove the first letter, append it to the end
        word = word[1:] + word[0]
        # Generate 3 random characters for the beginning and end
        random_chars_start = ''.join(random.sample(rand, 3))
        random_chars_end = ''.join(random.sample(rand, 3))
        # Return the encoded word
        return random_chars_start + word + random_chars_end

# Function for decoding
def decode(word):
    if len(word) < 3:
        # If the word has fewer than 3 characters, simply reverse it
        return word[::-1]
    else:
        # Remove the first 3 and last 3 characters
        word = word[3:-3]
        # Move the last character to the beginning
        return word[-1] + word[:-1]

# Main function to handle user input
def main():
    choice = input("Do you want to encode or decode the message? (e/d): ").lower()
    message = input("Enter the message for secure chat: ")
    
    # Split the message into words
    words = message.split()
    result = []
    
    if choice == 'e':
        # Encode each word
        for word in words:
            result.append(encode(word))
    elif choice == 'd':
        # Decode each word
        for word in words:
            result.append(decode(word))
    else:
        print("Invalid choice. Please choose 'e' to encode or 'd' to decode.")
        return

    # Join and display the result
    print("Result:", ' '.join(result))

# Run the main function
if __name__ == "__main__":
    main()
import math