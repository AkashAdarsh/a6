def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

def sort3(l):
    assert len(l) == 3
    if l[0] > l[1]: swap(l, 0, 1)
    if l[1] > l[2]: swap(l, 1, 2)
    if l[0] > l[1]: swap(l, 0, 1)

def bubble_sort(l):
    n = len(l)
    while n > 0:
        new_n = 0
        for i in range(1, n):
            if l[i-1] > l[i]:
                swap(l, i-1, i)
                new_n = i
        n = new_n