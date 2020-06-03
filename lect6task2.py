def enough(cap, on, wait):
    if cap >= on + wait:
        return 0
    else:
        number = wait - (cap - on)
        return number