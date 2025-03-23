import invisible_ink.helpers.vigenere as v
import pytest

TEST_KEY = 'bead'
TEST_MSG = 'he was really craving gummy bears'

@pytest.fixture
def create_vigenere():
    '''create Vigenere object'''
    return v.VigenereEncoder(TEST_KEY, TEST_MSG)


def test_vigenere_init(create_vigenere):
    '''VigenereEncoder creates correct object'''
    assert isinstance(create_vigenere, v.VigenereEncoder)


def test_vigenere_table_trivial(create_vigenere):
    '''tests for a'''
    assert (create_vigenere.table['a']['a'] == 'a' 
            and create_vigenere.table['a']['b'] == 'b')


def test_vigenere_table(create_vigenere):
    '''tests that the vigenere table works properly'''
    vig_obj = create_vigenere
    assert vig_obj.table['b']['c'] == 'd' and vig_obj.table['e']['c'] == 'g'


def test_encode_vigenere_common_use_case(create_vigenere):
    '''test with a simple use case'''
    vig_obj = create_vigenere
    assert 'iiwdt' in vig_obj.encode_vigenere()

def test_decode_vigenere_creates_correct_length(create_vigenere):
    '''checks that the encoded cipher has the correct length'''
    vig_obj = create_vigenere
    vig_obj.encode_vigenere()
    assert len(vig_obj.clear_txt_msg.replace(' ','')) == \
        len(vig_obj.encoded_cipher)


def test_decode_vigenere_common_use_case(create_vigenere):
    '''test that the encoeded vigenere can also be decoded'''
    vig_obj = create_vigenere
    vig_obj.encode_vigenere()
    decoded_msg = vig_obj.decode_vigenere()
    assert decoded_msg == 'hewasreallycravinggummybears'