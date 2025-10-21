# Given a video size, a unit for the video size, a hard drive capacity, and a unit for the hard drive, return the number of videos the hard drive can store using the following constraints:

# The unit for the video size can be kilobytes ("KB"), megabytes ("MB"), or gigabytes ("GB").
# If not given one of the video units above, return "Invalid video unit".
# The unit of the hard drive capacity can be gigabytes ("GB") or terabytes ("TB").
# If not given one of the hard drive units above, return "Invalid drive unit".
# Return the number of whole videos the drive can fit.
# Use the following conversions:
# Unit	Equivalent
# 1 B	1 B
# 1 KB	1000 B
# 1 MB	1000 KB
# 1 GB	1000 MB
# 1 TB	1000 GB
# For example, given 500, "MB", 100, and "GB as arguments, determine how many 500 MB videos can fit on a 100 GB hard drive.

import math 

def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    # Validate input - disallow if lower?
    # added it to the match, although this means you might compute changes
    # then find issue and so fail early might be better?

    # Convert all to B
    match video_unit:
        case "KB":
            video_size = video_size*1000
        case "MB":
            video_size = video_size*1000000
        case "GB":
            video_size = video_size*1000000000
        case _:
            return "Invalid video unit"
    
    match drive_unit:
        case "GB":
            drive_size = drive_size*1000000000
        case "TB":
            drive_size = drive_size*1000000000000
        case _:
            return "Invalid drive unit"
    
    return math.floor(drive_size/video_size)