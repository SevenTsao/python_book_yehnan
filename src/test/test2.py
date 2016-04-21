"""
http://code.tutsplus.com/tutorials/python-3-function-annotations--cms-25689
"""


def foo(a, b: 'annotation b', c:int) -> float:
    print(a + b + c)

foo('Hello', ',', 'World!')

foo(1, 2, 3)


def foo(x: 'an argument that defaults to 5' = 5):
    print(x)


def bar(*args, **kwargs: 'the keyword arguments dict'):
    print(kwargs['return'])

d = {'return': 4}


def foo2(a, b: 'annotating b', c: int) -> float:
    print(a + b + c)

print(foo2.__annotations__)


def foo3(*args: 'list of unnamed arguments', **kwargs: 'dict of named arguments'):
    print(args, kwargs)


def div(a, b):
    """Divide a by b
    args:
        a - the dividend
        b - the divisor (must be different than 0)
    return:
        the result of dividing a by b
    """
    return a / b

def div_convert(a: 'the dividend', b: 'the divisor (must be different than 0)') -> 'the result of dividing a by b':
    """Divide a by b"""
    return a / b


def div3(a: dict(type=float, help='the divided'),
         b: dict(type=float, help='the divisor (must be different than 0)')
         ) -> dict(type=float, help='the result of dividing a by b'):
    """Divide a by b"""
    return a / b


def check_range(f):
    def decorated(*args, **kwargs):
        for name, range in f.__annotations__.items():
            min_value, max_value = range
            if not (min_value <= kwargs[name] <= max_value):
                msg = 'argument {} is out of range [{} - {}]'
                raise ValueError(msg.format(name, min_value, max_value))
        return f(*args, **kwargs)
    return decorated

@check_range
def foo(a: (0, 8), b: (5, 9), c: (10, 20)):
    return a * b - c


print(foo(a=5, b=5, c=11))


def add(a, b) -> 0:
    result = a + b
    add.__annotations__['return'] += result
    return result

print(add.__annotations__['return'])
0

add(3, 4)
7

print(add.__annotations__['return'])
7

add(5, 5)
10

print(add.__annotations__['return'])
17
# TODO: 中文測試