# Caesar Cipher

This is a simple Python script that implements the Caesar Cipher. The Caesar Cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down the alphabet. 

## Usage

The program first prints a logo and then prompts the user to choose between encoding (encrypting) or decoding (decrypting) a message. 

The user is then asked to input the message they would like to encode or decode, followed by the shift number. The shift number represents the number of positions each letter of the message will be moved in the alphabet.

If the user chooses to encode, the `encrypt` function is called, which shifts each letter in the message by the shift number to the right in the alphabet, wrapping around to the beginning of the alphabet if necessary. Any characters in the message that are not in the alphabet are left unchanged.

If the user chooses to decode, the `decrypt` function is called, which shifts each letter in the message by the shift number to the left in the alphabet, wrapping around to the end of the alphabet if necessary. Again, any characters in the message that are not in the alphabet are left unchanged.

After encoding or decoding the message, the user is asked if they would like to go again. If they choose 'no', the program ends.

## Dependencies

This script depends on the `art` Python package for the logo. You can install it using pip:

```
pip install art
```

## Example

Here's an example of how to use the script:

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
3
The encoded text is khoor
Type 'yes' if you want to go again. Otherwise type 'no'
no
Goodbye
```
