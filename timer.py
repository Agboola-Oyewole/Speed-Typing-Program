import time

one_min = 59
while one_min > 0:
    if one_min < 10:
        print(f'00:0{one_min}')
    else:
        print(f'00:{one_min}')
    time.sleep(1)
    one_min -= 1

