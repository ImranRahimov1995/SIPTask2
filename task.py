def list_flattener(lst):
    if not lst:
        return lst

    if isinstance(lst[0], list):
        return list_flattener(lst[0]) + list_flattener(lst[1:])
    return [lst[0]] + list_flattener(lst[1:])


if __name__ == '__main__':
    transformed_list = list_flattener(
        [[[1, 2], 3], [4], [5, 6], [7, [8, 9]]]
    )

    print(transformed_list)
    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
