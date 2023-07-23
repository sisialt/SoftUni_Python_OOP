class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.current = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration

        self.current -= 1

        return self.current


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

print()
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")