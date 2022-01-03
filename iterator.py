class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):          # give the obj of iterator
        return self

    def __next__(self):          # give the next obj
        if self.num <= 10:       # to get value up to 10
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration   # stop the for loop


values = TopTen()
# print(values.__next__())         # for print one value
print(next(values))                # same of line 19
for i in values:
    print(i)



