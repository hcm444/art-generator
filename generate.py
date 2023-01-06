from itertools import product

from PIL import Image

PATH: str = 'Output'
ITERATION_MAX = 15624  # max permutations
IMAGE_X = 75  # image size
IMAGE_Y = 75
GEN_ARR = (list(product([1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5])))


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

