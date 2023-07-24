def solution():
    def integers():
        start = 1
        while True:
            yield start
            start += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]  # for _ in range(n): yield next(seq)

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))  # print(list(take(5, halves())))
