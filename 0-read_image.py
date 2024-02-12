"""Read images from disk or from memory in the image compression algorithm"""

# Read image from disk
image = read_image(file_path="image.jpg")

# Read image from memory
with open("image.jpg", "rb") as f:
        image_data = f.read()
        image = read_image(image_data=image_data)
