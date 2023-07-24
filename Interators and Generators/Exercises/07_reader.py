def read_next(*args):
    for arg in args:
        yield from arg
        # index = 0
        # while index < len(arg):
        #     yield arg[index]
        #     index += 1

        # for sub_el in arg:
        #     yield sub_el


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

print()
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)