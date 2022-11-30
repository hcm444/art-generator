import tkinter
from tkinter import *
from PIL import Image, ImageTk

window = Tk()

# Position text in frame
Label(window, text ='Position image on button', font =('Helvetica', 12)).pack(side = TOP, padx = 0, pady = 0)

# Create a photoimage object of the image in the path
photo = PhotoImage(file ="Output/111125_white_alert_pursed_crooked_hell_hair.png")

# Resize image to fit on button
photoimage = photo.subsample(1, 1)

# Position image on button
Button(window, image = photoimage, ).pack(side = LEFT, pady = 0)
Button(window, image = photoimage, ).pack(side = LEFT, pady = 0)
Button(window, image = photoimage, ).pack(side = LEFT, pady = 0)

mainloop()
