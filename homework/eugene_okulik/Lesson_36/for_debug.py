import random
# import time


def calc(n):
    return main_num / n


while True:
    main_num = 50
    num = random.randrange(0, 7)
    print(calc(num))
    finish = True if input('Finish?') == 'fin' else False
    if finish:
        break
    # else:
    #     time.sleep(1)
