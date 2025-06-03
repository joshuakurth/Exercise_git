import matplotlib.pyplot as plt


def merge_sort(sort_list):
    if (len(sort_list) <= 1):
        return
    mid = len(sort_list) // 2
    left = sort_list[:mid]
    right = sort_list[mid:]

    merge_sort(left)
    merge_sort(right)

    i_l = 0
    i_r = 0
    i_iter = 0

    while i_l < len(left) and i_r < len(right):
        if left[i_l] <= right[i_r]:
            sort_list[i_iter] = left[i_l]
            i_l += 1
        else:
            sort_list[i_iter] = right[i_r]
            i_r += 1
        i_iter += 1

    while i_l < len(left):
        sort_list[i_iter] = left[i_l]
        i_l += 1
        i_iter += 1

    while i_r < len(right):
        sort_list[i_iter] = right[i_r]
        i_r += 1
        i_iter += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
merge_sort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
