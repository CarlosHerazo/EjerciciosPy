class EmptyListError(Exception):
    pass


def average(numbers):
    if not numbers:
        raise EmptyListError("LA LISTA QUE ME PASASTE ESTA VACIA")

    return sum(numbers) / len(numbers)


try:
    num = []
    print(average(num))
except EmptyListError as e:
    print(e)
