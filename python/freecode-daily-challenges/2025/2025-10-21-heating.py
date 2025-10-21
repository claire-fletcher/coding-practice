def adjust_thermostat(current_f, target_c):

    target_f = (target_c * 1.8) + 32
    diff_f = target_f - current_f
    diff_f = round(diff_f, 2)


    if diff_f > 0:
        return f"Heat: {diff_f} degrees Fahrenheit"

    if diff_f < 0:
        new_diff = diff_f*-1
        return f"Cool: {new_diff} degrees Fahrenheit"

    return "Hold"