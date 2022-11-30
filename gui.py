import os
import tkinter
from tkinter import *
from main import image_list
from PIL import Image, ImageTk
from main import PATH
window = Tk()

# Position text in frame
Label(window, text ='Position image on button', font =('Helvetica', 12)).pack(side = TOP, padx = 0, pady = 0)

# Create a photoimage object of the image in the path
for files in os.listdir(PATH):
    im = Image.open('{0}/{1}'.format(PATH, files))
    photo = tkinter.Image(files)
    photo.show()

# Resize image to fit on button
photoimage = photo.subsample(1, 1)

# Position image on button
Button(window, image = photoimage, ).pack(side = LEFT, pady = 0)
Button(window, image = photoimage, ).pack(side = LEFT, pady = 0)
Button(window, image = photoimage, ).pack(side = LEFT, pady = 0)

mainloop()
