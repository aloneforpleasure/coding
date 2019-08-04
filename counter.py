def counter(start, end, step=0):
    from time import sleep
    if end > start:
        step = abs(step)
    else:
        if step > 0:
            step *= -1
    if step == 0:
        if end > start:
            step = 1
            end += 1
        else:
            step = -1
            end -= 1
    for index in range(start, end, step):
        print(index, flush=True)
        sleep(0.3)
        
