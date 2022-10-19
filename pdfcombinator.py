from PyPDF2 import PdfFileMerger
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import tempfile

FILES = []
LABELS = []

def select_files():
  global FILES, LABELS
  files = filedialog.askopenfilenames(initialdir = "~",
                                      title = "Choose PDF Files",
                                      filetypes = [("PDF Files", "*.pdf")])
  for file in files:
    FILES.append(file)

  # Create a label for each chosen pdf file
  i = 1
  for file in FILES:
    label = Label(root, relief=RAISED, text=file.split("/")[-1])
    label.grid(row=i, column=0, columnspan=3, padx=5, sticky=W+E+N+S)
    LABELS.append(label)
    i += 1

def clear_files():
  global FILES, LABELS
  FILES = []
  for label in LABELS:
    label.destroy()

def merge_files():
  global FILES
  if FILES != []:
    merger = PdfFileMerger()
    for pdf in FILES:
      merger.append(pdf, import_outline=False)
    location = filedialog.asksaveasfile(initialdir = "~", 
                                      title = "Combine Files", 
                                      filetypes = [("PDF", "*.pdf")],
                                      defaultextension=".pdf")
    if location != None:
      merger.write(location.name)
      merger.close()


if __name__ == '__main__':

  #Icon
  root = tk.Tk()
ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)
root.iconbitmap(default=ICON_PATH)

  # Title
root.title("PDF Combinator")
root.resizable(0,0)


  # Buttons and entry
open = Button(root, text="Select files", command=select_files,
  font=('bold'), activeforeground='green', fg='green', 
  height = 0, width = 0)


combine = Button(root, text="Combine files", command=merge_files, 
  font=('bold'))


clear = Button(root, text="Delete files", command=clear_files, 
  font=('bold'), activeforeground='red', fg='red', 
  height = 0, width = 0)

  # Buttons position
open.grid(row=0, column=0, padx=10, pady=10, sticky=W+E+N+S)
combine.grid(row=0, column=1, padx=10, pady=10, sticky=W+E+N+S)
clear.grid(row=0, column=2, padx=10, pady=10, sticky=W+E+N+S)

  # Cursor
root.config(cursor="arrow")


  # Center window
root.eval('tk::PlaceWindow . center')

root.mainloop()
