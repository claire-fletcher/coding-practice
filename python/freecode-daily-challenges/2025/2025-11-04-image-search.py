def image_search(images, term):

    return [image for image in images if term.lower() in image.lower()]