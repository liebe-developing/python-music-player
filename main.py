from tkinter import *
from tkinter import StringVar
from tkinter import filedialog, messagebox
import os
import pygame

root = Tk()
root.geometry("600x420")
root.resizable(0, 0)
root.title("Music Player")

status = StringVar()

pygame.init()
pygame.mixer.init()


# Playing song function
def playsong():
 songtrack.config(state=NORMAL)
 songtrack.delete('1.0', END)
 songtrack.insert('1.0', playlist.get(ACTIVE))
 songtrack.config(state=DISABLED)

 status.set("Playing")

 pygame.mixer.music.load(playlist.get(ACTIVE))
 pygame.mixer.music.play()


# Choosing a music folder
def choose_music_folder():
    base_music_dir = r"C:\Users\betaf\Music"
    chosen_folder = filedialog.askdirectory(initialdir=base_music_dir, title="Select a Music Folder")
    
    if chosen_folder:
        # List all files in the chosen directory
        songtracks = os.listdir(chosen_folder)
        
        # Filter the list to include only .mp3 files
        mp3_tracks = [track for track in songtracks if track.endswith('.mp3')]
        
        if mp3_tracks:
            os.chdir(chosen_folder)
            playlist.delete(0, END)  # Clear the current playlist
            
            for track in mp3_tracks:
                playlist.insert(END, track)  # Add .mp3 files to the playlist
        else:
            # Show error message if no .mp3 files are found
            messagebox.showerror("No MP3 Files", "The selected folder does not contain any .mp3 files.")
    else:
        # Show info message if no folder is selected
        messagebox.showinfo("No Folder Selected", "Please select a music folder.")

# Stopping song function
def stopsong():
 songtrack.config(state=NORMAL)
 songtrack.delete('1.0', END)
 songtrack.config(state=DISABLED)

 status.set("Stopped")

 pygame.mixer.music.stop()


# Pausing song function
def pausesong():
 status.set("Paused")
 pygame.mixer.music.pause()


# unpausing song function
def unpausesong():
 status.set("Playing")
 pygame.mixer.music.unpause()


# SongTrack
""" Song Track """
trackframe = LabelFrame(root, text="Song Track", font=("Arial", 15, "bold"), bg="#735DA5", fg="white", bd=5, relief=GROOVE)
trackframe.place(x=0, y=200, width=600, height=120)

songtrack = Text(trackframe, width=40, height=2, font=("Arial", 14), bg='#D3C5E5', fg="black", state=DISABLED)
songtrack.grid(row=0, column=0, padx=10, pady=5)

trackstatus = Label(trackframe, textvariable= status,  font=("Sans-serif", 12, 'bold'), bg="#D3C5E5", fg='#735DA5')
trackstatus.grid(row=0, column=1, padx=10, pady=5)



# ControlPanel
""" Control Panel """
buttonframe = LabelFrame(root, text='Control Panel', font=('Arial', 15, "bold"), bg="#735DA5", fg='white', bd=5,relief=GROOVE, pady=10)
buttonframe.place(x=0, y=320, width=600, height=100)

""" Play Button """
playbtn = Button(buttonframe, text='Play', width=6, height=1, font=("Arial", 16), bg='#D3C5E5', fg='black', command=playsong)
playbtn.grid(row=0, column=0, pady=5, padx=7)

""" Pause Button """
pausebtn = Button(buttonframe, text='Pause', width=6, height=1, font=("Arial", 16), bg='#D3C5E5', fg='black', command=pausesong)
pausebtn.grid(row=0, column=1, pady=5, padx=7)

""" Unpause Button """
unpausebtn = Button(buttonframe, text='Unpause', width=8, height=1, font=("Arial", 16), bg='#D3C5E5', fg='black', command=unpausesong)
unpausebtn.grid(row=0, column=2, pady=5, padx=7)

""" Stop Button """
stopbtn = Button(buttonframe, text='Stop', width=6, height=1, font=("Arial", 16), bg='#D3C5E5', fg='black', command=stopsong)
stopbtn.grid(row=0, column=3, pady=5, padx=7)

""" Select folder """
select_button = Button(buttonframe, text="Choose Folder", width=12, height=1, font=("Arial", 16), bg='#D3C5E5', fg='black', command=choose_music_folder)
select_button.grid(row=0, column=4, pady=5, padx=7)


# Songs frame
""" Songs Frame """
songsframe = LabelFrame(root, text='Songs Playlist', font=("Arial", 15, "bold"), bg="gray", fg="white", bd=5, relief=GROOVE)
songsframe.place(x=0, y=0, width=600, height=200)

""" Select Playlist """
scroll_y = Scrollbar(songsframe, orient=VERTICAL)
playlist = Listbox(songsframe, selectbackground='#735DA5', activestyle=NONE, selectmode=SINGLE, font=("Arial", 13), bg='#D3C5E5', fg='#000', bd=5, relief=GROOVE, yscrollcommand=scroll_y.set)
scroll_y.config(command=playlist.yview)
scroll_y.pack(side=RIGHT, fill=Y)
playlist.pack(fill=BOTH)


# Changing directory to the folder that music are listed!rr
os.chdir(r"C:\Users\betaf\Music")
songtracks = os.listdir()
for track in songtracks:
 if ".mp3" in track:
   playlist.insert(END, track)

root.mainloop()