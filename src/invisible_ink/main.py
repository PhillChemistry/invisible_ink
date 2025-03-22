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
