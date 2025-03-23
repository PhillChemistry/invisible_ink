import invisible_ink.helpers.vigenere as v
import pytest

TEST_KEY = 'bread'
TEST_MSG = 'he was really craving gummy bears'

@pytest.fixture
def create_vigenere():
    '''create Vigenere object'''
    return v.VigenereEncoder(TEST_KEY, TEST_MSG)


def test_vigenere_init(create_vigenere):
    assert isinstance(create_vigenere, v.VigenereEncoder)
