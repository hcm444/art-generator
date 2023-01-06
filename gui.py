
import tkinter as tk
import random
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

from generate import NFT


class NFTApp:
    def __init__(self, master):
        self.master = master
        self.master.title('NFT Generator')

        # Create the main frame for the app
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack()

        # Create the image frame and the image label
        self.image_frame = tk.Frame(self.main_frame)
        self.image_frame.pack()
        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack()

        # Create the Generate button
        self.generate_button = tk.Button(self.main_frame, text='Generate', command=self.generate_nft)
        self.generate_button.pack(side='left')

        # Create the Delete button
        self.delete_button = tk.Button(self.main_frame, text='Delete', command=self.delete_nft)
        self.delete_button.pack(side='left')

        # Create the Previous button
        self.prev_button = tk.Button(self.main_frame, text='Previous', command=self.prev_nft)
        self.prev_button.pack(side='left')

        # Create the Next button
        self.next_button = tk.Button(self.main_frame, text='Next', command=self.next_nft)
        self.next_button.pack(side='left')

        # Create the View button
        self.view_button = tk.Button(self.main_frame, text='View', command=self.view_nft)
        self.view_button.pack(side='left')

        # Initialize the list of NFT image file paths and the index
        self.nft_image_paths = []
        self.nft_image_index = 0

    def generate_nft(self):
        # Generate a new NFT object and save it to the Output directory
        attr0 = random.randint(1, 5)
        attr1 = random.randint(1, 5)
        attr2 = random.randint(1, 5)
        attr3 = random.randint(1, 5)
        attr4 = random.randint(1, 5)
        attr5 = random.randint(1, 5)
        NFT(attr0, attr1, attr2, attr3, attr4, attr5)
        self.update_image_list()

    def delete_nft(self):
        # Delete an NFT object from the Output directory
        file_path = filedialog.askopenfilename(initialdir='Output')
        if file_path:
            os.remove(file_path)
        self.update_image_list()

    def prev_nft(self):
        # Display the previous NFT image
        if self.nft_image_index > 0:
            self.nft_image_index -= 1
            self.display_nft_image()

    def next_nft(self):
        # Display the next NFT image
        if self.nft_image_index < len(self.nft_image_paths) - 1:
            self.nft_image_index += 1
            self.display_nft_image()

    def view_nft(self):
        # View an NFT object from the Output directory
        file_path = filedialog.askopenfilename(initialdir='Output')
        if file_path:
            # Update the list of NFT image file paths and the index
            self.update_image_list()
            self.nft_image_index = self.nft_image_paths.index(file_path)
            # Display the selected NFT image
            self.display_nft_image()

    def update_image_list(self):
        # Update the list of NFT image file paths
        self.nft_image_paths = [os.path.join('Output', f) for f in os.listdir('Output') if f.endswith('.png')]
        self.nft_image_index = 0
        self.display_nft_image()

    def display_nft_image(self):
        # Display the current NFT image
        image = Image.open(self.nft_image_paths[self.nft_image_index])
        image = ImageTk.PhotoImage(image)
        self.image_label.config(image=image)
        self.image_label.image = image

def main():
    root = tk.Tk()
    app = NFTApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()

