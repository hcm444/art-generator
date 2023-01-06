import os
import imageio
import numpy as np

image_dir = "Output"

image_filenames = os.listdir(image_dir)

images = []
for filename in image_filenames:
  path = os.path.join(image_dir, filename)
  image = imageio.imread(path)
  images.append(image)

output_image = np.zeros((500, 500, 4), dtype=np.uint8)

for i in range(20):
  for j in range(20):
    output_image[i*25:(i+1)*25, j*25:(j+1)*25] = images[i*20+j]


imageio.imwrite("output.png", output_image)
