def fibonacci():
    seq = [0, 1]
    index = 0
    while True:
        yield seq[index]
        index += 1
        seq.append(seq[index - 1] + seq[index])


generator = fibonacci()
for i in range(1):
    print(next(generator))

# def fibonacci():
#     n1, n2 = 0, 1
#
#     while True:
#         yield n1
#
#         n1, n2, = n2, n1 + n2