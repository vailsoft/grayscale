from PIL import Image
img = Image.open('image.jpg').convert('LA')
img.save('greyscale.png')
