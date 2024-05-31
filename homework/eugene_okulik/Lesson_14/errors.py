def calc(x, y):
    try:
        x, y = int(x), int(y)
        result =  x / y
    # except ZeroDivisionError:
    #     return 'Не дели на ноль'
    # except ValueError:
    #     return 'вводите числа'
    # except (ZeroDivisionError, ValueError) as err:
    #     print(err)
    #     return 'Some error happened'
    except ZeroDivisionError as err:
        print('Упало с:', x, y)
        raise err
    except ValueError:
        return 'вводите числа'
    else:
        print('Операция выполнена')
        return result
    finally:
        print('The end')



print(calc(1, 2))
print(calc(3, 0))
print(calc('5', '7'))
print(calc('2', 'восемь'))
print(calc(3, -5))
