def insertion_sort(lst):
    comparisons = 0
    swaps = 0
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            swap(lst, j, j-1)
            j -= 1
            swaps += 1
            comparisons += 1
        comparisons += 1
    return comparisons, swaps

def selection_sort(lst):
    comparisons = 0
    swaps = 0
    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
            comparisons += 1
        if min_idx != i:
            swap(lst, i, min_idx)
            swaps += 1
        comparisons += 1
    return comparisons, swaps

def quicksort(lst):
    comparisons = 0
    swaps = 0
    def _quicksort(lst, left, right):
        if left >= right:
            return
        pivot_idx = partition(lst, left, right)
        _quicksort(lst, left, pivot_idx-1)
        _quicksort(lst, pivot_idx+1, right)
    _quicksort(lst, 0, len(lst)-1)
    return comparisons, swaps

def merge_sort(lst):
    comparisons = 0
    swaps = 0
    def _merge_sort(lst, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        _merge_sort(lst, left, mid)
        _merge_sort(lst, mid+1, right)
        merge(lst, left, mid, right)
    _merge_sort(lst, 0, len(lst)-1)
    return comparisons, swaps

def bubble_sort(lst):
    comparisons = 0
    swaps = 0
    n = len(lst)
    while n > 0:
        new_n = 0
        for i in range(1, n):
            if lst[i-1] > lst[i]:
                swap(lst, i-1, i)
                new_n = i
                swaps += 1
            comparisons += 1
        n = new_n
    return comparisons, swaps

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def partition(lst, left, right):
    pivot_idx = right
    pivot_val = lst[pivot_idx]
    right -= 1
    while True:
        while lst[left] < pivot_val:
            left += 1
        while lst[right] > pivot_val:
            right -= 1
        if left >= right:
            break
        swap(lst, left, right)
        left += 1
        right -= 1
    swap(lst, left, pivot_idx)
    return left

def merge_sort(lst):
    comparisons = 0
    swaps = 0
    def _merge_sort(lst, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        _merge_sort(lst, left, mid)
        _merge_sort(lst, mid+1, right)
        merge(lst, left, mid, right)
    _merge_sort(lst, 0, len(lst)-1)
    return comparisons, swaps
