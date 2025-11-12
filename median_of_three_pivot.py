def median_of_three_pivot(arr, low, high):
    if len(arr) == 0:
        return None
    
    mid = (high + low)//2
    # print(arr[mid])
    
    if arr[low] > arr[mid]:
        if arr[low] > arr[high]:
            maximum = low
            if arr[mid] > arr[high]:
                median = mid
                minimum = high
            else:
                median = high
                minimum = mid
        else:
            maximum = high
            median = low
            minimum = mid
    else:
        if arr[mid] > arr[high]:
            maximum = mid
            if arr[low] > arr[high]:
                median = low
                minimum = high
            else:
                median = high
                minimum = low
        else:
            maximum = high
            median = mid
            minimum = low
    
    return arr[median]
        
            

# median_of_three_pivot([10, 9, 5, 2, 6, 4, 7], 0, 6)
median_of_three_pivot([10, 9, 5, 2, 6, 4, 7], 0, 6)
