"""Write compressed images to disk or memory in the image compression algorithm"""
# Compress the image
compressed_image = image.copy()
compressed_image.save("compressed_image.jpg", optimize=True, quality=50)

# Write compressed image to disk
write_compressed_image(compressed_image, file_path="compressed_image.jpg")

# Write compressed image to memory
compressed_image_data = write_compressed_image(compressed_image, image_data=True)
