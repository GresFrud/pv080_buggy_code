

temp = 1


def foo():
    global temp
    temp += 1


def bar():
    assert temp == 1

