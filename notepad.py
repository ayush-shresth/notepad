from tkinter import *
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = Tk()

main_application.geometry("1000x600+260+80")
main_application.title("text editor by ayush")

#############################################  main menu   ###############################################
main_menu = Menu()

file = Menu(main_application, tearoff=FALSE)

file.add_command(label="new", accelerator="ctrl+N")
file.add_command(label="open", accelerator="ctrl+O")
file.add_command(label="save", accelerator="ctrl+S")
file.add_command(label="save as", accelerator="ctrl+alt+S")
file.add_separator()
file.add_command(label="exit", accelerator="ctrl+Q")

edit = Menu(main_application, tearoff=FALSE)

edit.add_command(label="Find", accelerator="ctrl+F")
edit.add_command(label="Copy", accelerator="ctrl+C")
edit.add_command(label="Paste", accelerator="ctrl+V")
edit.add_command(label="Cut", accelerator="ctrl+X")
edit.add_command(label="Clear", accelerator="ctrl+alt+X")
edit.add_separator()
edit.add_command(label="Select all", accelerator="ctrl+A")

view = Menu(main_application, tearoff=FALSE)

view.add_checkbutton(label="Tool Bar")
view.add_separator()
view.add_checkbutton(label="Status Bar")

theme = Menu(main_application, tearoff=FALSE)
color_dict = {"Light": {"#474747", "#e0e0e0"},
              "Dark": {"#c4c4c4", "#2d2d2d"},
              "Red": {"#2d2d2d", "#ffe8e8"},
              "Monokai": {"#d3b774", "#474747"},
              "Default": {"#000000", "#ffffff"}}
for i in color_dict:
    theme.add_radiobutton(label=i)
    if i == "Monokai":
        theme.add_separator()

about = Menu(main_application, tearoff=FALSE)

# cascade
main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Theme", menu=theme)
main_menu.add_cascade(label="About", menu=about)

# ---------------------------------------   end of main menu  --------------------------------------------


#############################################  toolbar  ###############################################

#####font box
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=TOP, fill=X)
font_tuple = font.families()
font_family = StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state="readonly")
font_box["value"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0, column=0, padx=5)

# size box
size_var = IntVar()

# ---------------------------------------   end of tool bar  --------------------------------------------


#############################################  text editor ###############################################
# ---------------------------------------   end of text editor  --------------------------------------------


#############################################  main status bar  ###############################################
# ---------------------------------------   end of main status bar --------------------------------------------


#############################################  main menu functionality  ###############################################
# ---------------------------------------   end of main menu  functionality--------------------------------------------


main_application.config(menu=main_menu)
main_application.mainloop()
