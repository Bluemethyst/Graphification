from PIL import Image
from io import BytesIO


# chatgpt go brrr
def stack_images(image1_bytesio, image2_bytesio, image3_bytesio):
    # Open the images from BytesIO
    image1 = Image.open(image1_bytesio).convert('RGBA')
    image2 = Image.open(image2_bytesio).convert('RGBA')
    image3 = Image.open(image3_bytesio).convert('RGBA')

    # Get the dimensions of the images
    width, height = image1.size

    # Create a new blank image with triple the height and RGBA mode
    combined_image = Image.new('RGBA', (width, height * 3))

    # Paste the images onto the blank image
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, height))
    combined_image.paste(image3, (0, height * 2))

    # Save the combined image to BytesIO
    combined_image_bytesio = BytesIO()
    combined_image.save(combined_image_bytesio, format='PNG')
    combined_image_bytesio.seek(0)

    return combined_image_bytesio


def scale_image(image_bytesio, scale_factor):
    # Open the image from BytesIO
    image = Image.open(image_bytesio)

    # Calculate the new size based on the scale factor
    new_size = (int(image.width * scale_factor), int(image.height * scale_factor))

    # Resize the image
    scaled_image = image.resize(new_size)

    # Save the scaled image to BytesIO
    scaled_image_bytesio = BytesIO()
    scaled_image.save(scaled_image_bytesio, format='PNG')
    scaled_image_bytesio.seek(0)

    return scaled_image_bytesio
