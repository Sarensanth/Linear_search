def linear_search(array,k):
    count=0
    for i in array:
        if i==k:
            count+=1

    return count

array=list(map(int,input().split()))
k=int(input())
print(linear_search(array,k))