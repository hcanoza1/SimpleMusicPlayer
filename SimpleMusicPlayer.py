from tkinter import filedialog, Label, Tk
from tkinter import Button
from pygame import mixer

current_volume = float(0.1)


def select_song():

    filename = filedialog.askopenfilename(initialdir="C:/") #initialdir means it starts opening C:/
    current_song = filename
    song_title = filename.split("/") #it will ignore all "/" and only display the file name
    song_title = song_title[-1]

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.play()
        mixer.music.set_volume(current_volume)
        current_song_title_label.config(fg="green",text="Now playing:" + str(song_title))
    except Exception as e:
        print(e)
        current_song_title_label.config(fg="red", text="Error playing track")
        mixer.music.unload()

def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        current_song_title_label.config(fg="red", text="track not selected")
def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        current_song_title_label.config(fg="red", text="track not selected")

def volume_add():
    try:
        global current_volume
        if current_volume >= 1:
            volume_label.config(fg="green", text="Volume: Max")
            return

        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume: " + str(current_volume))
    except Exception as e:
        print(e)
        current_song_title_label.config(fg='red', text="track not selected")


def volume_minus():
    
    try:
        global current_volume
        # <= 0 because the lowest volume in module pygame is -1 which means muted
        if current_volume <= 0:
            volume_label.config(fg="red", text="Volume: Muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume: " + str(current_volume))
    except Exception as e:
        print(e)
        current_song_title_label.config(fg='red', text="track not selected")

#STOPS THE MUSIC
def stop():
    try:
        mixer.music.stop()
    except Exception as e:
        print(e)
        current_song_title_label.config(fg="red", text="track not selected")

#Play the music when STOPPED
def play():
        try:
            mixer.music.play()
        except Exception as e:
            print(e)
            current_song_title_label.config(fg="red", text="track not selected")



#Initiate the GUI of the music player
master = Tk()
master.title('Music player')


Label(master, text="Play a song", font=("Calibri",12),fg="red").grid(row=1,sticky="N", padx=100)

selectButton = Button(master, text="SELECT A SONG", padx=10,
                       pady=5, fg="black", bg="gray",command=select_song).grid(row=2, sticky="N")
pauseButton = Button(master, text="PAUSE", padx=10,
                       pady=5, fg="black", bg="gray",command=pause).grid(row=3, sticky="E")
resumeButton = Button(master, text="RESUME", padx=10,
                       pady=5, fg="black", bg="gray", command=resume).grid(row=3, sticky="W")

current_song_title_label = Label(master, text="Song Title", anchor= "s", fg= "Blue", font="Calibri")
current_song_title_label.grid(row=5, sticky="N")

volume_add = Button(master, text="+", fg= "black", font="Calibri",command=volume_add).grid(row=6, sticky="E")


volume_minus = Button(master, text="-", fg= "black", font="Calibri",command=volume_minus).grid(row=6, sticky="W")


volume_label = Label(master, text="VOLUME", anchor= "s", fg= "green", font="Calibri")
volume_label.grid(row=7, sticky="S")

stopButton = Button(master, text="STOP", padx=10,
                       pady=5, fg="black", bg="gray",command=stop).grid(row=3, sticky="N")

playButton = Button(master, text="PLAY", padx=10,
                       pady=5, fg="black", bg="gray",command=play).grid(row=4, sticky="N")

#master.mainloop so that the GUI will continue on display (should always be on your code)
master.mainloop()