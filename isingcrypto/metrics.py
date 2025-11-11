def tts(seconds, success_prob):
    return seconds / max(success_prob, 1e-12)
