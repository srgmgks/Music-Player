import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("500x200")
        self.root.config(bg="#f0f0f0")  

        pygame.init()
        pygame.mixer.init()
        self.playing = False
        self.paused = False

        self.track_var = tk.StringVar()
        self.track_var.set("No song selected")
        self.create_widgets()

    def create_widgets(self):
        track_label = tk.Label(self.root, textvariable=self.track_var, width=40, bg="#f0f0f0")
        track_label.pack(pady=10)

        select_button = tk.Button(self.root, text="Select Song", command=self.select_song, bg="#4caf50", fg="white")
        select_button.pack(pady=5)

        play_button = tk.Button(self.root, text="Play", command=self.play, bg="#2196f3", fg="white")
        play_button.pack(pady=5)

        pause_button = tk.Button(self.root, text="Pause", command=self.pause, bg="#ff9800", fg="white")
        pause_button.pack(pady=5)

        resume_button = tk.Button(self.root, text="Resume", command=self.resume, bg="#ff9800", fg="white")
        resume_button.pack(pady=5)

        stop_button = tk.Button(self.root, text="Stop", command=self.stop, bg="#f44336", fg="white")
        stop_button.pack(pady=5)

        volume_scale = tk.Scale(self.root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, label="Volume",
                                command=self.set_volume, bg="#f0f0f0")
        volume_scale.set(1.0)
        volume_scale.pack(pady=10)

    def select_song(self):
        file_path = filedialog.askopenfilename(title="Select Song", filetypes=(("MP3 Files", "*.mp3"),))
        if file_path:
            pygame.mixer.music.load(file_path)
            self.track_var.set("Playing: " + file_path)

    def play(self):
        if not self.playing:
            pygame.mixer.music.play()
            self.playing = True

    def pause(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def resume(self):
        if self.playing and self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def stop(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.track_var.set("No song selected")
            self.playing = False

    def set_volume(self, value):
        volume = float(value)
        pygame.mixer.music.set_volume(volume)

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
