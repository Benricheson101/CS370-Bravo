import pygame
import numpy as np
import time
import random
import threading

class SoundEffects:
    def __init__(self):
        pygame.mixer.init()
        self.current_sound = None
        
    def sound(self, frequency, duration=0.02):
        """Play sound."""
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)
        audio_data = (audio_data * 32767).astype(np.int16)
        
        # Create stereo audio data by duplicating the mono data
        stereo_audio_data = np.column_stack((audio_data, audio_data))
        
        # Create a sound object
        sound = pygame.sndarray.make_sound(stereo_audio_data)
        sound.play()
        self.current_sound = sound
        return sound
        
    def nosound(self):
        """Stop all sounds."""
        pygame.mixer.stop()
        
    def delay(self, milliseconds):
        """Delay for a given time in milliseconds."""
        pygame.time.wait(milliseconds)
    
    def safe_delay(self, milliseconds):
        """Non-blocking delay using time.sleep."""
        time.sleep(milliseconds / 1000.0)
        
    def play(self, frequency1, frequency2, delay_length):
        """Play a range of frequencies with a delay."""
        try:
            if frequency1 <= frequency2:
                for x in range(frequency1, frequency2 + 1):
                    self.sound(x, 0.1)
                    self.delay(delay_length)
                    self.nosound()  # Stop previous sound before playing new one
            else:
                for x in range(frequency1, frequency2 - 1, -1):
                    self.sound(x, 0.1)
                    self.delay(delay_length)
                    self.nosound()  # Stop previous sound before playing new one
        except Exception as e:
            print(f"Error in play method: {e}")
            self.nosound()
            
    def FootStep(self, FastPC):
        """Generate footstep sound effect."""
        try:
            # Calculate number of steps for FastPC (fast PC) or not
            steps1 = int(FastPC) * 50 + int(not FastPC) * 23
            steps2 = int(FastPC) * 60 + int(not FastPC) * 30
            

            for _ in range(steps1):
                self.sound(random.randint(350, 899), 0.002)  
            self.nosound()
            self.delay(120)  
            
            for _ in range(steps2):
                self.sound(random.randint(150, 199), 0.002)  
            
            self.nosound()
        except Exception as e:
            print(f"FootStep error: {e}")
            self.nosound()
            
    def GrabSound(self, FastPC):
        """Generate grab sound effects."""
        try:
            steps = int(FastPC)*50+int(not FastPC)*23
            for x in range(1, steps):
                #self.sound(random.randint(0, 1000) + 1000, 0.01)
                self.sound(random.randint(1000, 1999), 0.01)
                self.delay(3)
                self.nosound()
        except Exception as e:
            print(f"Error in GrabSound method: {e}")
            self.nosound()
            
    def BlockSound(self, FastPC):
        """Generate block sound effects."""
        try:
            for x in range(60, 30, -1):
                self.sound(x, 0.01)
                self.delay(1 + int(FastPC) * 2)
                self.nosound()
        except Exception as e:
            print(f"Error in BlockSound method: {e}")
            self.nosound()
            
    def NoneSound(self):
        """Generate 'none' sound effect."""
        try:
            for x in range(1, 5):
                self.sound(400, 0.1)
                self.delay(5)
                self.nosound()
            self.delay(5)
            self.sound(700, 0.1)
            self.delay(5)
            self.nosound()
            self.delay(5)
        except Exception as e:
            print(f"Error in NoneSound method: {e}")
            self.nosound()
            
            
    def Static(self):
        """Generate static sound effect."""
        try:
            # Play some random frequencies with occasional silence
            for _ in range(15):
                self.sound(random.randint(0, 15)) 
                self.nosound()
                
            self.sound(4, 0.02)  
            
            for _ in range(33):
                # Randomly decide whether to play a tone or remain silent
                if random.choice([0, 1]) == 0:
                    # Play random tones with varying frequencies
                    for _ in range(random.randint(10, 70)):
                        self.sound(random.randint(3000, 7000), 0.02)
                else:
                    self.nosound()
                    self.delay(random.randint(0, 30))  # Random delay before next sound
            
            self.nosound()
        except Exception as e:
            print(f"Error in Static method: {e}")
            self.nosound()

    def play_in_thread(self, sound_method, *args):
        """Plays any sound method in a separate thread."""
        print(f"Starting thread for {sound_method.__name__}")
        thread = threading.Thread(target=sound_method, args=args)
        thread.daemon = True
        thread.start()
        return thread