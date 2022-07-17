from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""


def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if len(Folder_Name) > 1:
        Path_Error.config(text=Folder_Name, fg='white')

    else:
        Path_Error.config(text="Please choose folder!", fg='red')


def DownloadVideo():
    global select
    choice = Video_Quality_Choice.get()
    url = Link_entry_box.get()
    if len(url) > 1:
        Link_Wrong_Error.config(text="")
        yt = YouTube(url)

        if choice == choices[0]:
            select = yt.streams.filter(progressive=True).get_by_itag(22)
        # elif(choice==choice[1]):
        #     select = yt.streams.filter(progressive=True).last()
        elif choice == choices[1]:
            select = yt.streams.filter(only_audio=True).first()
        else:
            Link_Wrong_Error.config(text="please put link again", fg="red")

    select.download(Folder_Name)
    Link_Wrong_Error.config(text="Download completed!", fg="white")


root = Tk()
root.title('YouTube Video Downloader by Tahir')
root.geometry("620x600")
root['bg'] = "#17202A"
root.columnconfigure(0, weight=1)

Main_label_heading = Label(root, text="\n\n<YouTube Video Downloader>\n", font=("Helvetica", 30, 'bold'), fg="white",
                           bg="#17202A")
Main_label_heading.grid()

Link_label_heading = Label(root, text="Enter YouTube Video Link Here!", font=("Helvetica", 15), fg="white",
                           bg="#17202A")
Link_label_heading.grid()

Link_entry_box_var = StringVar()
Link_entry_box = Entry(root, width=50, textvariable=Link_entry_box_var)
Link_entry_box.grid()

Link_Wrong_Error = Label(root, text=" ", fg="red", font=("Helvetica", 10), bg="#17202A")
Link_Wrong_Error.grid()

Save_Video = Label(root, text="Select Folder", font=("Helvetica", 15), fg="white", bg="#17202A")
Save_Video.grid()

Save_Video_path_button = Button(root, text="Choose Path", bg="#45b6fe", fg="black", command=openLocation)
Save_Video_path_button.grid()

Path_Error = Label(root, text="", fg="red", bg="#17202A", font=("Helvetica", 10))
Path_Error.grid()

Video_Quality = Label(root, text="Choose the video Quality", font=("Helvetica", 15), fg="white", bg="#17202A")
Video_Quality.grid()

choices = ["Video", "Audio"]
Video_Quality_Choice = ttk.Combobox(root, values=choices)
Video_Quality_Choice.grid()

blank_line = Label(root, text="\n", fg="red", bg="#17202A", font=("Helvetica", 10))
blank_line.grid()

Download_button = Button(root, text="Download", bg="#950101", fg="white", command=DownloadVideo)
Download_button.grid()

blank_line2 = Label(root, text="", fg="red", bg="#17202A", font=("Helvetica", 10))
blank_line2.grid()

Exit_button = Button(root, text="Exit", bg="#950101", fg="white", command=root.quit)
Exit_button.grid()

Developer_branding_lable = Label(root, text="\n\n Made By Tahir Habib", font=("Comic Sans MS", 10, 'bold'), fg="white",
                                 bg="#17202A")
Developer_branding_lable.grid()

root.mainloop()
