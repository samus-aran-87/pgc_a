def basic_coro():
    summ = 0
    while True:
        data = yield summ
        summ += data