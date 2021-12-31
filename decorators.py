# for adding new feature for the existing function
def div(a, b):
    print(a/b)   # existing function,which we can not change


def updated_dev(func):

    def new_func(p, q):             # we want to make numerator bigger than denominator
        if p < q:
            p, q = q, p
        return func(p, q)
    return new_func


div = updated_dev(div)
div(2, 4)
