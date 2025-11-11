from isingcrypto.encode import encode_message_to_ising
from isingcrypto.decode import decode_low_energy_to_message

def test_encode_decode_stub():
    model, key = encode_message_to_ising("hi")
    msg = decode_low_energy_to_message(model, key)
    assert isinstance(msg, str)
