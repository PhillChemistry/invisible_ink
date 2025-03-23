'''helper to encode and decode vigenere cyphers 
   based upon a given encoding word'''

import string

class VigenereEncoder():
    '''class to encode and decode vigenere ciphers'''
    def __init__(self, encoding_key: str, msg_to_encode: str):
        '''takes an encoding key and a msg to encode as an optional argument'''
        self.table = self._get_vigenere_table()
        self.encoding_key = self._validate_key(encoding_key.lower().strip())
        self.clear_txt_msg = self._validate_key(
            msg_to_encode.lower(), spaces=True
            )
        self.encoded_cipher = ''


    def encode_vigenere(self) -> str:
        '''creates a vigenere encoding of clear_text_msg with code_word
        for an explanation of vigenere ciphers, see main.py docst'''
        msg = self.clear_txt_msg.replace(' ', '')
        msg_len = len(msg)
        total_key = self.encoding_key * (len(msg) // msg_len + 1)
        total_key = total_key[:msg_len]
        encoded = ''
        for key_char, msg_char in zip(total_key, msg):
            encoded += self._get_vig_char(key_char, msg_char)
        self.encoded_cipher = encoded
        return encoded


    def decode_vigenere(self) -> str:
        '''decodes vigenere cipher encoded_msg with with word.
        for an explanation of vigenere ciphers, see main.py docst'''
        # TODO: implement decoding function
        len_msg = len(self.encoded_cipher)
        len_keyword = len(self.encoding_key)
        extended_keyword = self.encoding_key * (len_msg // len_keyword)
        extended_keyword = extended_keyword[:len_msg]
        decoded_msg = ''
        for idx, char in enumerate(self.encoded_cipher):
            decoded_msg += self._get_decrypted_char(
                extended_keyword[idx], char
                )
        return decoded_msg


    def _get_vigenere_table(self) -> dict[dict[str: str]]:
        '''generates a vigenere table as a dict of dicts of strs.
        called using table[code_wrd_letter][clear_txt_letter] = encoded_letter
        '''
        char_pool = string.ascii_lowercase * 2
        vig_table = {}
        for offset, code_wrd_char in enumerate(string.ascii_lowercase):
            vig_table[code_wrd_char] = {
                msg_char: char_pool[pool_idx + offset]
                for pool_idx, msg_char in enumerate(string.ascii_lowercase)
            }
        return vig_table


    def _get_vig_char(self, code_word_char: str, msg_char: str) -> str:
        '''gets a single vigenere encoded char based upon the given table'''
        return self.table[code_word_char][msg_char]


    def _get_decrypted_char(self, key_char: str, encrypted_char: str) -> str:
        for decrypted, encrypted in self.table[key_char].items():
            if encrypted == encrypted_char:
                return decrypted
        return None


    def _validate_key(self, key_wrd: str, spaces: bool = False):
        for char in string.punctuation:
            key_wrd = key_wrd.replace(char, '')
        if not isinstance(key_wrd, str):
            print('encoding_key must be str!')
            raise ValueError
        for char in key_wrd:
            if not spaces:
                if char not in string.ascii_lowercase:
                    print('key must be singe word!' )
                    raise ValueError
            else:
                if not (char in string.ascii_lowercase or char == ' '):
                    print(f'found an issue with char {char} in {key_wrd}!')
                    raise ValueError
        return key_wrd
