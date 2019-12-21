# Given a list of numbers, find and print all elements that are an even number. In
# this case use a for-loop that iterates over the list, and not over its indices! That
# is, don't use range.

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23, 55, 576, 63, 43]
for i in num_list:
    if i % 2 == 0:
        print(i)
