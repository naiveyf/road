from PIL import Image
Image.MAX_IMAGE_PIXELS = None
img = Image.open("dataset/origin/382_label.png")
print(img.size)
cropped = img.crop((10000, 10000, 25000, 25000))  # (left, upper, right, lower)
cropped.save("dataset/origin/383_label.png")