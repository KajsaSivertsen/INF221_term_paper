def insertion_sort(a):
    ''' insertion sort works
    '''
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key


# to test the above code
if __name__ == '__main__':
    A = [1, 5, 8, 9, 4, 3, 7, 0, 3, 7, 9]
    print ("Given array is", end="\n")
    print(A)
    insertion_sort(A)
    print("Sorted array is: ", end="\n")
    print(A)
