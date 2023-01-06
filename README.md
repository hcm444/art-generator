## art

NFT artwork generation.

This code is generating NFT art by combining different images and then saving them in the 'Output' directory. The images are combined using the Pillow library's paste function and resized using the resize function. The resulting image is saved in the 'Output' directory with the file name being a concatenation of the attribute values.

The code creates a class called NFT which takes in six attributes, attr0 through attr5, in its initialization. The NFT class has a __str__ method which returns the string representation of the object, which is the concatenation of the six attributes. The NFT object also calls the generate function, which generates and saves the NFT art by combining and resizing the images and saving them to the 'Output' directory.

The generate function first maps the values of the attributes to corresponding descriptions using lists. It then opens the images corresponding to the attribute values using the Pillow library's open function and combines them using the paste function. The resulting image is then resized using the resize function and saved to the 'Output' directory.

The ITERATION_MAX variable is set to 15624, which is the maximum number of permutations of the six attributes, which are all 5-element lists. The GEN_ARR list is created as the list of all permutations of the six attributes. The main function generates NFT objects for all the permutations in GEN_ARR.

## generate(1,2,3,4,3,1)

Generates a specific image.

![123431_white_stoned_frown_small_sunset_adam](https://user-images.githubusercontent.com/32826270/204912590-5eef9865-fb71-4470-9175-fbe0217f3ba8.png)

## generate_random(4)

Generates 4 random images and saves them in /Output.

![145145_white_tired_smile_crooked_snow_hair](https://user-images.githubusercontent.com/32826270/204912407-94c5d820-617e-4ccc-96e8-f97bc090bcdf.png)
![233415_green_sus_frown_small_beach_hair](https://user-images.githubusercontent.com/32826270/204912409-16fad186-a2ff-498c-a62d-9653d3bd2f78.png)
![242154_green_tired_smirk_crooked_morning_chest](https://user-images.githubusercontent.com/32826270/204912411-6a3d769b-cfb2-44e7-9c44-595815e85e18.png)
![255222_green_sunglasses_smile_round_hell_ear](https://user-images.githubusercontent.com/32826270/204912413-d33a54f9-8ad4-4838-8292-dd6a4fcbdd78.png)

## generate_all()

Generates all permutations of images and saves them in /Output.

## clear

Deletes all files in /Output.

## output()

Prints the names of .png files in /Output.
```
/usr/local/bin/python3.10 /Users/hcm444/PycharmProjects/art/main.py 
242154_green_tired_smirk_crooked_morning_chest.png
233415_green_sus_frown_small_beach_hair.png
145145_white_tired_smile_crooked_snow_hair.png
255222_green_sunglasses_smile_round_hell_ear.png

Process finished with exit code 0

```

## find(attribute)

Search by attribute.

## delete(attribute)

Delete by attribute.

## show()

Display images in /Output.
