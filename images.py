from PIL import Image, ImageFilter


def set_blur():
    img = Image.open('./images/pikachu.jpg')

    filtered_img = img.filter(ImageFilter.BLUR)

    filtered_img.save("blur.png", "png")


def convert_gray():
    img = Image.open('./images/pikachu.jpg')

    filtered_img = img.convert('L')

    filtered_img.save("grey.png", "png")


def show_img():
    img = Image.open('./images/pikachu.jpg')
    img.show()


def rotate_img():
    img = Image.open('./images/bulbasaur.jpg')
    filtered_img = img.rotate(90)

    filtered_img.save("rotate.png", "png")


def create_thumbnail():
    img = Image.open('./images/astro.jpg')

    img.thumbnail((400, 400))
    img.save('thumbnail.jpg')


if __name__ == '__main__':
    set_blur()
    convert_gray()
    # show_img()
    rotate_img()

    create_thumbnail()
