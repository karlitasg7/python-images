import os
import sys

from PIL import Image

if __name__ == '__main__':
    image_folder = sys.argv[1]
    target_folder = sys.argv[2]

    # check if exists target folder, if not create it
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for filename in os.listdir(image_folder):
        img = Image.open(f'{image_folder}{filename}')

        clean_name = os.path.splitext(filename)[0]

        img.save(f'{target_folder}{clean_name}.png', 'png')

    print('Finish!!')
