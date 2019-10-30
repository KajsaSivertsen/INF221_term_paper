def mergesort(arr):
    '''Merge sort works as ldksglksdf
    '''
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        l = arr[:mid]  # Dividing the array elements
        r = arr[mid:]  # into 2 halves

        mergesort(l)  # Sorting the first half
        mergesort(r)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays l[] and r[]
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print(arr)
    mergesort(arr)
    print("Sorted array is: ", end="\n")
    print(arr)
