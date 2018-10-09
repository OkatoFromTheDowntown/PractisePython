# Number, String, Tuple, Frozenset
# Dictionary, Set, List
# boolen: False == 0, True == 1, type(False/True):bool

# print strings without ¥r¥n
print('This file is used for testing .py', end='')
print()

# use globle value
GLOBAL_VALUE = 'globle value'


def print_global_value():
    print(GLOBAL_VALUE, type(GLOBAL_VALUE))


def change_print_global_value():
    global GLOBAL_VALUE
    GLOBAL_VALUE += ' is Changed.'
    print(GLOBAL_VALUE, type(GLOBAL_VALUE))


print_global_value()
change_print_global_value()
print_global_value()


def update_list(x):
    # x = [3,4,5,6]
    x += [3, 4, 5, 6, 7]
    return x


x = [1, 2]
print(x)  # [1,2]
print(update_list(x))  # [3,4,5,6]
print(x)  # [1,2]


# multiple arguments
def type_all(arg, *tupleArgs, **dictArgs):
    print(arg, type(arg))
    print(tupleArgs, [type(x) for x in tupleArgs])
    print(dictArgs, [type(dictArgs[key]) for key in dictArgs])


a = b = c = 123
d, e, f = 'DE', 3.14, False
print(a, b, c, d, e, f)
type_all(set({}), a, b, c, d, e, f, x=1, y=3)

print(sum(x**2 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if x % 2 == 0))
print([type(x) for x in (1, 2, False, 4, '5', 6.2)])

print(dict([('a', 1), ('b', 2), ('c', 3)]))
print(dict({('a', 1), ('b', 2), ('c', 3)}))
print(dict((('a', 1), ('b', 2), ('c', 3))))
print(dict([['a', 1], ['b', 2], ['c', 3]]))


def fun_args(arg, *args, **kwargs):
    print('arg: {0}'.format(arg))
    for i in args:
        print('*args: {0}'.format(i))
    for j in kwargs:
        print('**kwargs: {0}->{1}'.format(j, kwargs[j]))


fun_args(1, [11, 22, 33, 44], a=1, b=2)
args1 = (1, 3, 54, 23)
args2 = {'a': 3, 'b': 5}
fun_args(2, *args1, **args2)

# base function programming test


def lazy_add(a):
    def arg(b):
        return a + b
    return arg


add1 = lazy_add(1)
print(add1(10), add1(100))


def lazy_print(*str):
    return lambda x: str[x % len(str)]


print1 = lazy_print(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(print1(0))  # 1
print(print1(3))  # 4
print(print1(14))  # 5
