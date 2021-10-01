# This code is for CSE515 Project phase1, Prof. Candan
# This code was developed by Mohammed Albasha, Fall 21, 9/10/2021

# Here are all the neede and used packages to run this project
# If you run it for the first time and it crashes make sure that you have installed the below packes, either locally in your machine using a package manager if needed or using pip3.
import os
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog
from PIL import Image
import matplotlib
import numpy as np
from functions import *

default_path = "./input/olivetti_faces.npy"
default_target_path = "./input/olivetti_faces_target.npy"

# This func is made to ensure that the temp directory is created
def mkdir_temp():
    path = "./temp"
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

# Folder Select Function
def task1_select_folder():
    folder_path = filedialog.askopenfilename(title='Select Folder', initialdir=os.path.dirname(os.path.realpath(__file__)))
    task1_txt_folder.delete(1.0, 'end')
    task1_txt_folder.insert(1.0, folder_path)
    
# For each task there are an execution function that is made to call the appropriate functions from the functions file
# Here below are the execution handlers for each tasks
def exc_task1():

    # # Input Validation
    folder_path = task1_txt_folder.get("1.0","end")
    # img_id = task1_txt_img_id.get("1.0", "end")
    # model = task1_picker.get()
    if len(folder_path) < 2:
        folder_path = default_path

    # if len(img_id) < 2:
    #     img_id = 10
    # else:
    #     img_id = int(img_id)

    # if img_id < 1:
    #     img_id = 10

    # if len(model) < 1:
    #     model = 'HOG'

    images = np.load(folder_path.replace(" ", "").replace("\n", ""))
    process_t1(images)
    # _img_name = './temp/temp_{}_.png'.format(img_id)
    # matplotlib.image.imsave(_img_name, images[img_id], cmap="gray")
    # _img = Image.open(_img_name)

    # # Call based on selected model
    # if model == "Color Moments":
    #     display_color_moments(images, img_id)

    # if model == "ELBP":
    #     display_elbp(_img_name, img_id)

    # if model == "HOG":
    #     display_hog(_img_name, img_id, _img)

models = [ "Color Moments", "ELBP", "HOG", ]
reductions = [ "PCA", "SVD", "LDA", "k-means"]
x = [ "cc", "con", "detail", "emboss", "jitter", "neg", "noise1", "noise2", "original", "poster", "rot", "smooth", "stipple"]
font_color='#f5f5f5'
bg_color='#303030'
bg='#c4c4c4'
run="#f5f5f5"

# Main window that will contain all tasks and their required input components
mkdir_temp()
window = Tk()
window.title("Phase 1")

# Intro Lable
lbl_into = Label(window, text="CSE515 Project Phase 2 Task#1", font=("Arial Bold", 25), background=bg)
lbl_into.place(x=375, y=45, anchor="center")


# Task1 input components
task1_lbl = Label(window, text="Images Folder Path:", font=("Arial", 18), background=bg)
task1_lbl.place(x=30, y=170, anchor="w")
task1_txt_folder = Text(window, font=("Arial", 12), width=45, height=2)
task1_txt_folder.place(x=270, y=170, anchor="w")
task1_btn = Button(window, text="Select Folder", width=12, height=2, foreground=font_color, background=bg_color, command=task1_select_folder)
task1_btn.place(x=700, y=170, anchor="w")

task1_lbl_X = Label(window, text="X:", font=("Arial", 18), background=bg)
task1_lbl_X.place(x=30, y=250, anchor="w")
# task1_txt_X = Text(window, font=("Arial", 12), width=5, height=1.2)
# task1_txt_X.place(x=65, y=250, anchor="w")
task1_picker_X = StringVar()
task1_picker_X.set( "cc" )
task1_txt_X = OptionMenu(window, task1_picker_X, *x)
task1_txt_X.place(x=65, y=250, anchor="w")

task1_lbl_K = Label(window, text="K:", font=("Arial", 18), background=bg)
task1_lbl_K.place(x=170, y=250, anchor="w")
task1_txt_K = Text(window, font=("Arial", 12), width=5, height=1.2)
task1_txt_K.place(x=200, y=250, anchor="w")

task1_txt_model = Label(window, text="Model:", font=("Arial", 18), background=bg)
task1_txt_model.place(x=270, y=250, anchor="w")
task1_picker_model = StringVar()
task1_picker_model.set( "Color Moments" )
task1_txt_model = OptionMenu(window, task1_picker_model, *models)
task1_txt_model.place(x=355, y=250, anchor="w")

task1_txt_reduction = Label(window, text="Reduction:", font=("Arial", 18), background=bg)
task1_txt_reduction.place(x=490, y=250, anchor="w")
task1_picker_reduction = StringVar()
task1_picker_reduction.set( "PCA" )
task1_txt_reduction = OptionMenu(window, task1_picker_reduction, *reductions)
task1_txt_reduction.place(x=620, y=250, anchor="w")

task1_btn_run = Button(window, text="Run Task1", width=40, height=2, foreground=bg_color, background=run, command=exc_task1)
task1_btn_run.place(x=270, y=330, anchor="w")

# Setting window size
window.geometry('800x400')
window.configure(bg=bg)
window.mainloop()