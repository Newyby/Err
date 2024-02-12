"""Create a class for  compression algorithm. This class should contain methods for compressing and decompressing images, also include methods for setting compression parameters"""

from PIL import Image

class ImageCompressor:
        def __init__(self, quality=50):
            self.quality = quality
                        
        def set_quality(self, quality):
            self.quality = quality
                                            
        def compress_image(self, image_path):
            # Open the image
            image = Image.open(image_path)
            # Compress the image
            compressed_image = image.copy()
            compressed_image.save("compressed_image.jpg", optimize=True, quality=self.quality)
                                                                                                            
            return compressed_image
                                                                                                                    
        def decompress_image(self, compressed_image_path):
                                                                                                                                    # Open the compressed image
            compressed_image = Image.open(compressed_image_path)
                                                                                                                                                
                                                                                                                                    # Decompress the image
                                                                                                                                    decompressed_image = compressed_image.copy()  
                                                                                                                                    return decompressed_image
