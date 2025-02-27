import numpy as np
import sounddevice as sd
#----------------------------------------TESTING PURPOSE ONLY-----------------------------------------------------------#
def play_sound(frequency=440, duration=1.0, sample_rate=44100):
    """Generate and play a sine wave in real-time without saving a file."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * frequency * t)  # Sine wave
    
    sd.play(wave, samplerate=sample_rate)
    sd.wait()

# Example: Play a beep at 800 Hz duration how long it plays for 
play_sound(frequency=800, duration=0.3)
