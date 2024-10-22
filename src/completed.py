def mark_complete(arr, index):
    if 0 <= index < len(arr):
        arr[index] += f"(completed!)"
    else:
        raise IndexError(f"Index {index} is out of bounds")
    return arr

def mark_incomplete(arr, index):
    if 0 <= index < len(arr):
        arr[index] = arr[index].replace("(completed!)", "")
    else:
        raise IndexError(f"Index {index} is out of bounds")
    return arr