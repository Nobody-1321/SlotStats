import time
import pygame 

def lg_initialize_sound(path, volume=0.5, loop=0):
    """Initialize the sound system."""
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(volume)  # Set the volume (0.0 to 1.0)
    pygame.mixer.music.play(loop)  # Play the music, loop=0 means play once

def lg_stop_sound(delay=0):
    """Stop the sound system."""
    time.sleep(delay)  # Wait for the specified delay
    pygame.mixer.music.stop()  # Stop the  music
    pygame.mixer.quit()  # Quit the mixer
    