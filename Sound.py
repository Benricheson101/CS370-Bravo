import pygame
import numpy as np
import time
import random
import threading

class SoundEffects:
    def __init__(self):
        pygame.mixer.init()
    
    def sound(self, frequency, duration=1.0):
        """Play sound indefinitely."""
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)
        audio_data = (audio_data * 32767).astype(np.int16)

        # Create stereo audio data by duplicating the mono data
        stereo_audio_data = np.column_stack((audio_data, audio_data))

        # Create a sound object
        sound = pygame.sndarray.make_sound(stereo_audio_data)
        sound.play()  # Play sound once

    def nosound(self):
        """Stop all sounds."""
        pygame.mixer.stop()

    def delay(self, milliseconds):
        """Delay for a given time in milliseconds."""
        pygame.time.wait(milliseconds)

    def play(self, frequency1, frequency2, delay_length):
        """Play a range of frequencies with a delay."""
        if frequency1 <= frequency2:
            for x in range(frequency1, frequency2 + 1):
                self.sound(x)
                self.delay(delay_length)
        else:
            for x in range(frequency1, frequency2 - 1, -1):
                self.sound(x)
                self.delay(delay_length)
            self.nosound()

    def FootStep(self, FastPC):
        """Generate footstep sounds based on CPU speed."""
        for x in range(1, int(FastPC)*50+int(not FastPC)*23):
            self.sound(random.randint(0, 550) + 350, 0.1)
            self.delay(10)  # Added delay to compensate for fast CPU
            self.nosound()
            self.delay(120)

        for x in range(1, int(FastPC)*60+int(not FastPC)*30):
            self.sound(random.randint(0, 50) + 150, 0.1)

    def GrabSound(self, FastPC):
        """Generate grab sound effects."""
        for x in range(1, int(FastPC)*160+int(not FastPC)*65):
            self.sound(random.randint(0, 1000) + 1000, 0.1)
            self.delay(10)
            self.nosound()

    def BlockSound(self, FastPC):
        """Generate block sound effects."""
        for x in range(60, 30, -1):
            self.sound(x, 0.1)
            self.delay(1 + int(FastPC) * 2)
        self.nosound()

    def NoneSound(self):
        """Generate 'none' sound effect."""
        for x in range(1, 5):
            self.sound(400, 0.1)
            self.delay(10)
            self.nosound()
            self.delay(10)
            self.sound(700, 0.1)
            self.delay(10)
            self.nosound()
            self.delay(10)
            
    def play_in_thread(self, sound_method, *args):
        """Plays any sound method in a separate thread."""
        thread = threading.Thread(target=sound_method, args=args)
        thread.daemon = True
        thread.start()