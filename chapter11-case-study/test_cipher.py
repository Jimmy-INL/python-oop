from cipher import VigenereCipher

def pytest_funcarg__cipher(request):
    return VigenereCipher("TRAIN")

def test_encode(cipher):
    encoded = cipher.encode("ENCODEDINPYTHON")
    assert encoded == "XECWQXUIVCRKHWA"

def test_encode_character(cipher):
    encoded = cipher.encode("E")
    assert encoded == "X"

def test_encode_spaces(cipher):
    encoded = cipher.encode("ENCODED IN PYTHON")
    assert encoded == "XECWQXUIVCRKHWA"

def test_encode_lowercase(cipher):
    encoded = cipher.encode("encoded in Python")
    assert encoded == "XECWQXUIVCRKHWA"

def test_encode_letter(cipher):
    assert cipher._encode_letter("E", "T") == "X"
    assert cipher._encode_letter("N", "N") == "A"

def test_decode(cipher):
    decoded = cipher.decode("XECWQXUIVCRKHWA")
    assert decoded == "ENCODEDINPYTHON"

def test_decode_letter(cipher):
    assert cipher._decode_letter("A", "N") == "N"
    assert cipher._decode_letter("X", "T") == "E"