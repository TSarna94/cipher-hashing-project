# Caesar Cipher Encryption Tool

## Overview

This project is a Python-based command-line application that demonstrates basic encryption and decryption using a Caesar Cipher. The program allows users to encode and decode messages by shifting alphabetic characters 15 positions through the alphabet while preserving uppercase and lowercase letters.

The project was completed as part of my cybersecurity studies to strengthen my understanding of encryption concepts, character manipulation, and Python programming fundamentals.

## Features

- Encrypts messages using a Caesar Cipher with a shift value of 15
- Decrypts previously encrypted messages
- Preserves uppercase and lowercase letters
- Leaves numbers, spaces, and punctuation unchanged
- Interactive command-line menu
- Input validation for menu selections

## Technologies Used

- Python 3

## How It Works

The program uses the Caesar Cipher technique, a classical substitution cipher that shifts each letter in a message by a fixed number of positions.

Example:

Original Message:
```

HELLO WORLD

```

Encoded Message:
```

WTAAD LDGAS

```

The program can then decode the encrypted message back to its original text.

## Example Usage

### Main Menu

```

=== Caesar Cipher Tool ===

Choose an option:
1. Encode a message
2. Decode a message
3. Exit

```

### Encoding a Message

```

Enter a message to encode: HELLO

Encoded message: WTAAD

```

### Decoding a Message

```

Enter a message to decode: WTAAD

Decoded message: HELLO

```

## Skills Demonstrated

- Python functions
- String manipulation
- ASCII character conversion
- Modular programming
- Encryption fundamentals
- Input validation
- Command-line application development

## What I Learned

Through this project, I gained practical experience working with:

- Character encoding and decoding
- Caesar Cipher encryption techniques
- ASCII values using `ord()` and `chr()`
- Modular arithmetic for alphabet wrapping
- Building interactive command-line tools

## Future Improvements

- Allow users to choose custom shift values
- Support additional cipher algorithms
- Add file encryption functionality
- Create a graphical user interface (GUI)
- Implement stronger modern encryption methods for comparison

## Author

Tony Sarna

Aspiring Cybersecurity Professional | Python Developer
