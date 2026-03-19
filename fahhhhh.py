import multiprocessing
import threading
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from tkinter import *

def window_process():
    def play_audio():
        pygame.mixer.init()
        pygame.mixer.music.load("fahhhhh.mp3")
        pygame.mixer.music.play(loops=-1)
    
    threading.Thread(target=play_audio, daemon=True).start()

    Window = Tk()
    Window.title("hello")
    Window.geometry("400x300")
    icon = PhotoImage(file="cpu_heart.png")
    Window.iconphoto(True, icon)
    Window.config(bg="black")
    Window.mainloop()

if __name__ == "__main__":
    while True:
        child = multiprocessing.Process(target=window_process)
        child.start()
        child.join()
        print("Window closed. Respawning in 3 seconds...")
        time.sleep(3)