

def bigger_size(l):
    """Function that takes a list convert all positives to "big"""
    for i in range(len(l)):
        if l[i] > 0:
            l[i] = "big"


l = [-1, 3, 5, -5]
bigger_size(l)
print("Bigger Size:", l)


def count_positives(l):
    """replace the last value with the number of positive values."""
    count = 0
    for i in l:
        if i > 0:
            count += 1
    l[-1] = count


l = [1, 6, -4, -2, -7, -2]
count_positives(l)
print("Count positives:", l)


def sum_total(l):
    """returns the sum of all the values in the array."""
    sum = 0
    for i in l:
        sum += i
    return sum


l = [1, 2, 3, 4]
print("Sum Total:", sum_total(l))


def average(l):
    """returns the average of all the values."""
    return sum_total(l) / len(l)


l = [1, 2, 3, 4]
print("Average:", average(l))


def length(l):
    """returns the length of the list."""
    return len(l)


l = [1, 2, 3, 4]
print("Length:", length(l))


def minimum(l):
    """returns the minimum value in the list. If the list is empty, function returns False."""
    if len(l) == 0:
        return False
    min_num = l[0]
    for i in l:
        if i < min_num:
            min_num = i

    return min_num


l = [37, 2, 1, -9]
print("Minimum:", minimum(l))


def maximum(l):
    """returns the maximum value in the list. If the list is empty, function returns False."""
    if len(l) == 0:
        return False
    max_num = l[0]
    for i in l:
        if i > max_num:
            max_num = i

    return max_num


l = [37, 2, 1, -9]
print("Maximum:", maximum(l))


def ulitmate_analysis(l):
    """takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list."""
    d = {"sum_total": sum_total(l), "average": average(
        l), "minimum": minimum(l), "maximum": maximum(l), "length": length(l)}
    return d


l = [37, 2, 1, -9]
print("Ulitmate Analysis:", ulitmate_analysis(l))


def reverse_list(l):
    """takes a list and return that list with values reversed. Do this without creating a second list"""
    for i in range(int(len(l) / 2)):
        l[i], l[-i-1] = l[-i-1], l[i]

    return l


l = [37, 2, 1, -9]
print("Reverse list:", reverse_list(l))
