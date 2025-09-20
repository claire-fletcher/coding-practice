import math

def number_of_photos(photo_size_mb, drive_size_gb):

    return math.floor((drive_size_gb*1000)/photo_size_mb)