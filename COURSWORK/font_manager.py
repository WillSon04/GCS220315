import tkinter.font as tkfont

def configure():
    # Define the font settings
    font_family = "Arial"
    font_size = 10
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(family=font_family, size=font_size)
    text_font = tkfont.nametofont("TkTextFont")
    text_font.configure(family=font_family, size=font_size)
    fixed_font = tkfont.nametofont("TkFixedFont")
    fixed_font.configure(family=font_family, size=font_size)
