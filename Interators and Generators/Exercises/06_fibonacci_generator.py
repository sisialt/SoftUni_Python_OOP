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

