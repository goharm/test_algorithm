second = 50

def func01(first01):
    first = 10
    func02(first01)
    return

def func02(first01):
    first = 20
    return

if __name__ == '__main__':
    first = 30
    func01(first)
    pass