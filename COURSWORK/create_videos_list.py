import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class CreateVideosList:
    def __init__(self, window):
        self.playlist = []  
        window.geometry("400x300")
        window.title("Create Videos List")

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=4)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        add_btn = tk.Button(window, text="Add", command=self.add_clicked)
        add_btn.grid(row=0, column=2, padx=10, pady=10)

        reset_btn = tk.Button(window, text="Reset", command=self.reset_clicked)
        reset_btn.grid(row=0, column=3, padx=10, pady=10)

        play_btn = tk.Button(window, text="Play", command=self.play_clicked)
        play_btn.grid(row=0, column=4, padx=10, pady=10)

        self.video_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.video_txt.grid(row=1, column=0, columnspan=5, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Arial", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=5, sticky="W", padx=10, pady=10)

    def reset_clicked(self):
        self.video_txt.delete("1.0", tk.END)  
        self.input_txt.delete(0, tk.END)  
        self.playlist.clear()  
        self.status_lbl.configure(text="Playlist has been reset!")

    def play_clicked(self):
        if not self.playlist:
            self.status_lbl.configure(text="Please add videos to the playlist before playing.")
            return
        
        for key in self.playlist:
            lib.increment_play_count(key)
        
        self.status_lbl.configure(text="Playlist is being played!")

    def list_all(self):
        output = ""
        for key in self.playlist:
            name = lib.get_name(key)
            output += f"{name}\n"
        set_text(self.video_txt, output)

    def add_clicked(self):  
        key = self.input_txt.get()
        if not key:
            self.status_lbl.configure(text="Please enter a video number")
            return
        
        if key.isdigit():  
            name = lib.get_name(key)
            if name is not None:
                if key not in self.playlist:
                    self.playlist.append(key)
                    self.list_all()
                    self.status_lbl.configure(text=f"Video {key} added to playlist!")
                else:
                    self.status_lbl.configure(text=f"Video {key} is already in the playlist!")
            else:
                self.status_lbl.configure(text=f"Video {key} not found")
        else:
            self.status_lbl.configure(text="Please enter a valid number")

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateVideosList(window)
    window.mainloop()
