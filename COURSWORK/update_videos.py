import tkinter as tk
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class UpdateVideos:
    def __init__(self, window):
        window.geometry("370x300")  
        window.title("Update Videos")

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=4)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        self.input_rating_txt = tk.Entry(window, width=4)
        self.input_rating_txt.grid(row=0, column=2, padx=10, pady=10)

        update_btn = tk.Button(window, text="Update Rating", command=self.update_video_clicked)
        update_btn.grid(row=0, column=3, padx=10, pady=10)

        self.video_txt = tk.Text(window, width=50, height=12)  
        self.video_txt.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Arial", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    def update_video_clicked(self):
        key = self.input_txt.get()
        rating_input = self.input_rating_txt.get()

        if not key:
            self.status_lbl.configure(text="Please enter a video number")
            return
        if not key.isdigit():  
            self.status_lbl.configure(text="Please enter a valid video number")
            return
        if not rating_input:
            self.status_lbl.configure(text="Please enter a rating")
            return
        
        name = lib.get_name(key)

        if name is not None:
            if rating_input.isdigit():
                try:
                    newrating = int(rating_input)
                    if 1 <= newrating <= 5:
                        lib.set_rating(key, newrating)
                        director = lib.get_director(key)  
                        play_count = lib.get_play_count(key)  
                        video_details = (f"Name: {name}\n"
                                         f"Director: {director}\n"
                                         f"Rating: {newrating}\n"
                                         f"Play Count: {play_count}")
                        set_text(self.video_txt, video_details)
                        self.status_lbl.configure(text="Rating updated successfully!")
                    else:
                        self.status_lbl.configure(text="Invalid rating input! Rating should be between 1 and 5.")
                except ValueError:
                    self.status_lbl.configure(text="Invalid input! Please enter a number between 1 and 5.")
            else:
                self.status_lbl.configure(text="Please enter a valid number for rating")
        else:
            self.status_lbl.configure(text=f"Video {key} not found!")
            self.video_txt.delete("1.0", tk.END)

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    UpdateVideos(window)
    window.mainloop()
