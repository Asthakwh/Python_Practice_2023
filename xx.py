import tkinter
import customtkinter
from pytube import YouTube

def startdownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        video.download()
        finishLable.configure(text="Downloded!")
    except:
        finishLable.configure(text="Download Error", text_color="red")
        #print("youtube link is invalid")
        
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    Percentage_of_completion = bytes_downloaded / total_size*100
    per = str(int(Percentage_of_completion))
    pPercentage.configure(text=per +'%')
    pPercentage.update()
        
#system settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

#Our app frame

app = customtkinter.CTk()
app.geometry("720*480")
app.title('Youtube Downloader')

#adding ui Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack (padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var )
link.pack()

#download
finishLable = customtkinter.CTkLabel(app, text="")
finishLable.pack()

#progress
pPercentage = customtkinter.CTkLabel

#download button

download = customtkinter.CTkButton(app, text="Download", command=startdownload)
download.pack(padx=10 , pady = 10)

#Run app
app.mainloop()
