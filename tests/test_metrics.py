from isingcrypto.metrics import tts

def test_tts():
    assert tts(10.0, 0.5) > 0
