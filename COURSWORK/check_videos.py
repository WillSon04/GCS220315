import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class CheckVideos:
    def __init__(self, window):
        window.geometry("580x300")
        window.title("Check Videos")

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Arial", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.video_details_frame = tk.Frame(window)
        self.video_details_frame.grid(row=1, column=3, columnspan=2, sticky="NW", padx=10, pady=10)

        self.video_txt = tk.Text(self.video_details_frame, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.list_videos_clicked()

    def check_video_clicked(self):
        key = self.input_txt.get()
        
        if not key:
            self.status_lbl.configure(text="Please enter a video number.")
            set_text(self.video_txt, "")
            return
        if not key.isdigit():
            self.status_lbl.configure(text="Please enter a valid number.")
            set_text(self.video_txt, "")
            return
        
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = (f"Name: {name}\n"
                             f"Director: {director}\n"
                             f"Rating: {rating}\n"
                             f"Play Count: {play_count}")
            set_text(self.video_txt, video_details)
            self.status_lbl.configure(text="Video details displayed.")
        else:
            set_text(self.video_txt, "")
            self.status_lbl.configure(text=f"Video {key} not found!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CheckVideos(window)
    window.mainloop()
