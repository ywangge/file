import os
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from PIL import Image,ImageTk

#新建文档
def new():
    window.title('新建文档')
    filename = None
    text.delete(1.0,END)