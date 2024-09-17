#Music Player
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        pygame.mixer.init()
        self.create_widgets()
        self.current_track = None
        
    def create_widgets(self):
        self.heading = tk.Label(self.root, text="Music Player", font=("Algerian", 20, "bold"))
        self.heading.pack(pady=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music, state=tk.DISABLED)
        self.play_button.pack(pady=5)
        
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music, state=tk.DISABLED)
        self.pause_button.pack(pady=5)
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music, state=tk.DISABLED)
        self.stop_button.pack(pady=5)
        
        self.open_button = tk.Button(self.root, text="Open File", command=self.open_file)
        self.open_button.pack(pady=5)
    
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.current_track = file_path
            pygame.mixer.music.load(self.current_track)
            self.play_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
    
    def play_music(self):
        if self.current_track:
            pygame.mixer.music.play()
            self.play_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
    
    def pause_music(self):
        pygame.mixer.music.pause()
        self.pause_button.config(state=tk.DISABLED)
        self.play_button.config(state=tk.NORMAL)
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
