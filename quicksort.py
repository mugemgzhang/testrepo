from random import shuffle
a = ['q','w','e','r','t','y','u','i','o',
'p','a','s','d','f','g','h','j','k','l','z',
'x','c','v','b','n','m']
shuffle(a)
def quicksort(a,lo,hi):
    if lo>=hi:
        return
    index = partition(a,lo,hi)
    quicksort(a,lo,index)
    quicksort(a,index+1,hi)
def partition(a,lo,hi):
    i,j = lo+1,hi
    v=a[lo]
    while 1:
        while i<hi and a[i]<=v:
            i+=1
        while j>lo and a[j]>=v:
            j-=1
        if i>=j:
            break
        a[i],a[j] = a[j],a[i]
    a[lo],a[j] = a[j],a[lo]
    return j
quicksort(a,0,len(a)-1)
print(a)
