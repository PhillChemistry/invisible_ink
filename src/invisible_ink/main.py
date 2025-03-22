'''program to create an email as a .docx file.
   all paragraphs within the mail are new-line separated.
   the new-line of each paragrpah, a code is written in  "invisible ink",
   meaning that the color of the text is the same (white) as the background.
   the code contains bidding information for an undisclosed cartel deal 
   and is encoded as a vigenere cipher: encoding word: RANDOM
   
   R A N D O M R A N D O M R A N D O M R A N
   t h i s i s t h e c l e a r t e x t m s g

   encrypted via the following matrix:
    A  B C D E F ...
    -----------
    a| b c d e f ...
    b| c d e f g ...
    c| d e f g h ...
    d| e f g h i ...
    e| f g h i j ...
    ...
    ===> first line gives the letter of the encoding word;
         first line of the following row gives the letter in the code
         the encoding is the cross section between both
   '''

import docx
from invisible_ink.helpers import impexp as ie
from invisible_ink.helpers import vigenere as v

# =========================================================================
#                             USER INPUT:
# =========================================================================

CLEAR_TEXT_MSG = 'hello, my name is Phillip'
ENCODING_WORD = 'random'
MAIL_HEADER = 'Regarding the agreed-upon deal'


# =========================================================================
#                             FUNCTIONS:
# =========================================================================

def split_along_paragraphs(msg: str) -> list[str]:
    '''splits a txt in a list of strings, with paragraph changes (\n\n)
       as separator'''
    return msg.split(sep='\n\n')

# =========================================================================
#                             DRIVER CODE:
# =========================================================================

def main():
    '''main code'''
    encoder = v.VigenereEncoder(ENCODING_WORD, CLEAR_TEXT_MSG)
    encoded_msg = encoder.encode_vigenere()
    mail_msg = ie.import_txt('mail_text.txt')
    

if __name__ == '__main__':
    main()