def positionOfFirstLargest(arr):
    count=0
    max_pos=0
    max = arr[0]
    for a in arr:
        if max<a:
            max=a
            print(max)
            max_pos=count
            print(max_pos)
        count+=1
    return max_pos

positionOfFirstLargest([0,1,5,3,4,5])