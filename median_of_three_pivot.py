def median_of_three_pivot(arr, low, high):
    if len(arr) == 0:
        return None
    
    mid = (high + low) // 2
    
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


## alternate solution
def median_of_three_pivot_alternate_solution(arr, low, high):
    if len(arr) == 0:
        return None
    
    mid = (high + low) // 2
    # print(arr[mid])

    if arr[low] < arr[mid] < arr[high] or arr[high] < arr[mid] < arr[low]:
        return arr[mid]
    elif arr[mid] < arr[low] < arr[high] or arr[high] < arr[low] < arr[mid]:
        return arr[low]
    else:
        return arr[high]    
        
            

# median_of_three_pivot([10, 9, 5, 2, 6, 4, 7], 0, 6)
print(median_of_three_pivot([10, 9, 5, 2, 6, 4, 7], 0, 6))
print(median_of_three_pivot_alternate_solution([10, 9, 5, 2, 6, 4, 7], 0, 6))
