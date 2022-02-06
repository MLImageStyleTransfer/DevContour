from PIL import Image, ImageEnhance

def grayscale_transform(coloured_image_path: str = '../../assets/demo.png') -> None:
    coloured_img = Image.open(coloured_image_path)
    filter = ImageEnhance.Color(coloured_img)
    grayscaled_img = filter.enhance(0)
    grayscaled_img.save('../../assets/res.png', 'PNG')

if __name__ == '__main__':
    grayscale_transform()