class Add:
    def __call__(self, li):
        return sum(li)

add = Add()

sum = add([1, 2, 3, 4, 5, 6])
print("Total sum:", sum)
