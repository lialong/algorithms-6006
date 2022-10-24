def count_long_subarrays(A):
    longest,length,num = 1,0,0
    last = A[0]
    for item in A:
        if item >= last:
            length += 1
            if length > longest:
                longest = length
                num = 1
            elif length == longest:
                num += 1
        else:
            length = 1
        last = item
    return num

if __name__ == "__main__":
    A = (1,3,4,2,7,5,6,9,8,9,10)
    print(count_long_subarrays(A))
