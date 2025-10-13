def to_12(time):
    h = int(time[:2])
    m = time[2:4]

    # Set the time of day
    if h < 12:
        time_of_day = "AM"
    else:
        time_of_day = "PM"

    # Convert to hours, leaves out 12 which will stay the same
    if h == 0:
        h = "12"
    elif h > 12:
        h = h - 12

    return f"{h}:{m} {time_of_day}"