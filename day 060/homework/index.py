def min_max(lst):
    return [min(lst), max(lst)]

print("Min and Max:", min_max([1, 2, 3, 4, 5]))


def area_or_perimeter(l, w):
    return l * w if l != w else 4 * l



def get_volume_of_cuboid(length, width, height):
    return length * width * height



def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count = sum(1 for x in arr if x > 0)
    total = sum(x for x in arr if x < 0)
    return [count, total]

print("Positives and Negatives:", count_positives_sum_negatives([1, -2, 3, -4, 5]))


def check(seq, elem):
    return elem in seq
