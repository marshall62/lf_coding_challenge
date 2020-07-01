from CipherInterface import CipherInterface

class ShiftCipher (CipherInterface):

    def __init__ (self, shift: int):
        self.shift = shift

    # coding challenge shift cipher was very underspecified in terms of what characters to shift
    # but it does want ' ' preserved and doesn't mention how characters shift beyond the character set
    # so I'm going to wrap lower case letters, wrap upper case letters and preserve all others.
    def shift_str (self, message: str, shift: int) -> str:
        res = []
        for c in message:
            if c.isupper():
                res.append( chr(ord('A') + ((ord(c) + shift - ord('A')) % 26)))
            elif c.islower():
                res.append( chr(ord('a') + ((ord(c) + shift - ord('a')) % 26)))
            else:
                res.append(c)
        return ''.join(res)

    def encode (self, message: str) -> str:
        '''Encodes the message by shifting its characters to the right using a Caesar cipher.  Characters will wrap around if they overflow.'''
        return self.shift_str(message, self.shift)

    def decode (self, encrypted_message: str) -> str:
        '''Decodes an encrypted string'''
        return self.shift_str(encrypted_message, -1 * self.shift)