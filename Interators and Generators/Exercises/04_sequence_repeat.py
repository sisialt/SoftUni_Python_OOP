class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = -1
        self.iterations = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations + 1 >= self.number:
            raise StopIteration

        self.index += 1
        self.iterations += 1
        if self.iterations % (len(self.sequence)) == 0:
            self.index = 0

        return self.sequence[self.index]


# class sequence_repeat:
#     def __init__(self, sequence: str, number: int):
#         self.sequence = sequence
#         self.number = number
#         self.idx = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idx == self.number - 1:
#             raise StopIteration
#
#         self.idx += 1
#
#         return self.sequence[self.idx % len(self.sequence)]


result = sequence_repeat('abc', 10)
for item in result:
    print(item, end='')

print()
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
