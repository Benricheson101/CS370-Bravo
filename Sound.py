import numpy as np
import sounddevice as sd
import random
import time

# Sound settings
SAMPLE_RATE = 44100  
FastPC = True  # Toggle FastPC behavior

def generate_tone(frequency, duration):
    """Generates a sine wave tone."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Sine wave
    return wave

def play_sound(frequency, duration):
    """Plays a generated sound using sounddevice."""
    wave = generate_tone(frequency, duration)
    sd.play(wave, samplerate=SAMPLE_RATE)
    sd.wait()

def GrabSound():
    """GrabSound effect with high-pitched random tones."""
    count = 160 if FastPC else 65
    for _ in range(count):
        play_sound(random.randint(1000, 2000), 0.01)

def BlockSound():
    """BlockSound effect with descending tones."""
    for x in range(60, 29, -1):
        play_sound(x, 0.001 + (0.002 if FastPC else 0))

def NoneSound():
    for _ in range(5):
        play_sound(400, 0.01)
        time.sleep(0.01)
        play_sound(700, 0.01)
        time.sleep(0.01)

def FootStep():
    """Simulates a footstep sound with two different tones."""
    step1_count = 50 if FastPC else 23
    step2_count = 60 if FastPC else 30

    for _ in range(step1_count):
        play_sound(random.randint(350, 900), 0.05)

    time.sleep(0.12)

    for _ in range(step2_count):
        play_sound(random.randint(150, 200), 0.05)

# Test the sounds
print("Playing GrabSound...")
GrabSound()
time.sleep(1)

print("Playing BlockSound...")
BlockSound()
time.sleep(1)

print("Playing NoneSound...")
NoneSound()
time.sleep(1)

print("Playing FootStep...")
FootStep()