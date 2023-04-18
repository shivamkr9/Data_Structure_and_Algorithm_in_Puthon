def find_sublist_with_target_sum(lst, target):
    """
    Returns a continues sublist of `lst` whose elements sum up to `target`, or `None` if no such sublist exists.
    """
    n = len(lst)
    start = 0
    end = 0
    curr_sum = 0

    while end < n:
        if curr_sum == target:
            return lst[start:end]
        elif curr_sum < target:
            curr_sum += lst[end]
            end += 1
        else:  # curr_sum > target
            curr_sum -= lst[start]
            start += 1

    return None  # no sublist found


# example usage
lst = [2, 2, 5, 7, 6, 8, 9]
target = 18
sub_lst = find_sublist_with_target_sum(lst, target)
print(sub_lst)