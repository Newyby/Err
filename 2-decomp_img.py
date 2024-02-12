"""Decompress images in the image compression algorithm"""
# Compress the image
image = Image.open("image.jpg")
compressed_image = image.copy()
compressed_image.save("compressed_image.jpg", optimize=True, quality=50)

# Decompress the image
decompressed_image = decompress_image("compressed_image.jpg")

# Write the decompressed image to disk
decompressed_image.save("decompressed_image.jpg")
