from typing import List


def flattenList(li: List) -> None:
    for i in li:
        if type(i) == list:
            flattenList(i)
        else:
            newLi.append(i)


if __name__ == "__main__":
    newLi = []
    li = [1, 2, 3, 4, [5, 6, [7, 8]], 9, 10]
    flattenList(li)
    print(newLi)
