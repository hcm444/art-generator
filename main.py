from itertools import product
import random
from PIL import Image
import os
import shutil

PATH: str = 'Output'
ITERATION_MAX = 15624
IMAGE_X = 75  # cool
IMAGE_Y = 75


class NFT:
    # NFT objects
    def __init__(self, attr0, attr1, attr2, attr3, attr4, attr5):
        self.body = attr0
        self.eyes = attr1
        self.mouth = attr2
        self.nose = attr3
        self.background = attr4
        self.extra = attr5

        generate(self.body, self.eyes, self.mouth, self.nose, self.background, self.extra)

    def __str__(self):
        return f"{self.body}{self.eyes}{self.mouth}{self.nose}{self.background}{self.extra}"


def generate(attr0, attr1, attr2, attr3, attr4, attr5):
    # generates NFT art and saves in it Output file
    # if else statements below match number of image to corresponding attribute for description
    # separate methods are organized at the bottom, so it's easier to add more in the future
    body_value = ["white", "green", "yellow", "pink", "teal"][attr0 - 1]
    eyes_value = ["alert", "stoned", "sus", "tired", "sunglasses"][attr1 - 1]
    mouth_value = ["pursed", "smirk", "frown", "teeth", "smile"][attr2 - 1]
    nose_value = ["crooked", "round", "fat", "small", "big"][attr3 - 1]
    background_value = ["beach", "hell", "sunset", "snow", "morning"][attr4 - 1]
    extra_value = ["adam", "ear", "beard", "chest", "hair"][attr5 - 1]
    # numer array and description array
    num_array = [attr0, attr1, attr2, attr3, attr4, attr5]
    desc_array = [body_value, eyes_value, mouth_value, nose_value, background_value, extra_value]
    # print both arrays to console
    print(str(desc_array))
    print(num_array)
    # Open the images including the body
    attr0 = Image.open('assets/Body/{0}.png'.format(str(attr0)))
    attr1 = Image.open('assets/Eyes/{0}.png'.format(str(attr1)))
    attr2 = Image.open('assets/Mouth/{0}.png'.format(str(attr2)))
    attr3 = Image.open('assets/Nose/{0}.png'.format(str(attr3)))
    attr4 = Image.open('assets/Background/{0}.png'.format(str(attr4)))
    attr5 = Image.open('assets/Extra/{0}.png'.format(str(attr5)))
    # Paste/Merge Required images, everything pasted on body
    attr0.paste(attr1, (0, 0), attr1)
    attr0.paste(attr2, (0, 0), attr2)
    attr0.paste(attr3, (0, 0), attr3)
    attr0.paste(attr4, (0, 0), attr4)
    attr0.paste(attr5, (0, 0), attr5)
    # Resize image
    resized_img = attr0.resize((IMAGE_X, IMAGE_Y), Image.NEAREST)  # instagram size
    # save name as attributes number _ properties.png, so I can easily perform data analysis.
    resized_img.save(
        'Output/{0}{1}{2}{3}{4}{5}_{6}_{7}_{8}_{9}_{10}_{11}.png'.format(str(num_array[0]), str(num_array[1]),
                                                                         str(num_array[2]), str(num_array[3]),
                                                                         str(num_array[4]), str(num_array[5]),
                                                                         body_value,
                                                                         eyes_value, mouth_value, nose_value,
                                                                         background_value, extra_value), "PNG")

    return


def generate_all():
    # five arrays for every attribute
    generation_arr = (list(product([1, 2, 3, 4, 5],
                                   [1, 2, 3, 4, 5],
                                   [1, 2, 3, 4, 5],
                                   [1, 2, 3, 4, 5],
                                   [1, 2, 3, 4, 5],
                                   [1, 2, 3, 4, 5])))
    # M is a list of every possible tuple
    for counter in range(generation_arr.__len__()):
        # parse through these tuples
        # save every respective place of the tuple for generate()
        NFT(generation_arr[counter][0], generation_arr[counter][1], generation_arr[counter][2],
            generation_arr[counter][3], generation_arr[counter][4], generation_arr[counter][5])
        # remember how many permutations you have! ex: 5x5x5x5x5 = 3125 files!


def generate_random(generation_val):
    # five arrays for every attribute
    generation_arr = (list(product([1, 2, 3, 4, 5],
                                   [1, 2, 3, 4, 5],
                                   [1, 2, 3, 4, 5],
                                   [1, 2, 3, 4, 5],
                                   [1, 2, 3, 4, 5],
                                   [1, 2, 3, 4, 5])))
    # M is a list of every possible tuple
    for counter in range(generation_val):
        # generate a number of random NFTs
        counter = random.randint(0, ITERATION_MAX)
        # random integer from beginning to end of possible iterations
        # parse through these tuples
        # save every respective place of the tuple for generate()
        NFT(generation_arr[counter][0], generation_arr[counter][1], generation_arr[counter][2],
            generation_arr[counter][3], generation_arr[counter][4], generation_arr[counter][5])
        # remember how many permutations you have! ex: 5x5x5x5x5 = 3125 files!


def find(attribute):
    # search by attribute
    result = []
    for files in os.listdir(PATH):
        if attribute in files:
            result.append(os.path.join(PATH, files))
    print(result)


def delete(attribute):
    # deletes by specific attribute "white", "21333", "fat", etc
    for files in os.listdir(PATH):
        if attribute in files:
            file_path = os.path.join(PATH, files)
            os.remove(file_path)
            # it works don't change this method


def clear():
    # deletes all files in NFT/Output
    for filename in os.listdir(PATH):
        file_path = os.path.join(PATH, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


clear()
generate_random(1)
