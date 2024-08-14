import tkinter as tk
import font_manager as fonts
from check_videos import CheckVideos
from create_videos_list import CreateVideosList
from update_videos import UpdateVideos  

def check_videos_clicked():
    status_lbl.config(text="Check Videos button was clicked!")
    CheckVideos(tk.Toplevel(window))

def create_videos_list():
    status_lbl.config(text="Create Videos playlist button was clicked!")
    CreateVideosList(tk.Toplevel(window))

def update_videos_clicked():
    status_lbl.config(text="Update Videos button was clicked!")
    UpdateVideos(tk.Toplevel(window))

window = tk.Tk()
window.geometry("370x120")
window.title("Video Player")

fonts.configure()  # Apply the font settings

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

create_videos_list_btn = tk.Button(window, text="Create Videos List", command=create_videos_list)
create_videos_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_videos_btn = tk.Button(window, text="Update Videos", command=update_videos_clicked)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, text="")
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
