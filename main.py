import os
import tkinter.messagebox
import tkinter as tk
from pytube import YouTube

yt = tk.Tk()
yt.title('YouTube Downloader')
yt.resizable(None, None)
yt.geometry('450x150')

entry1 = tk.Entry(yt)
entry1.pack(pady=10, ipadx=90)


def getAudioDownload():
    x1 = entry1.get()

    def complete(n1, n2):
        tkinter.messagebox.showinfo(title='Done', message=n2[:-1]+'3')
        base = os.path.splitext(n2)[-2]
        print(base)
        os.rename(n2, base + '.mp3')
        print(n2)

    video_object = YouTube(x1, on_complete_callback=complete)

    label1 = tk.Label(yt, text='Got_it')
    label1.pack(pady=10)

    video_object.streams.get_audio_only().download()


def getHVideoDownload():

    x1 = entry1.get()

    def complete(n1, n2):
        tkinter.messagebox.showinfo(title='Done', message=n2)

    video_object = YouTube(x1,on_complete_callback=complete)

    label1 = tk.Label(yt, text=video_object.title)
    label1.pack(pady=10)

    video_object.streams.get_highest_resolution().download()


b1=tk.Button(text='Get Audio', command=getAudioDownload)
b1.pack(side=tkinter.LEFT, ipadx=50, padx=15)

b2 = tk.Button(text='Get Video', command=getHVideoDownload)
b2.pack(side=tkinter.RIGHT, ipadx=50, padx=15)

yt.mainloop()

