
import random
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[min_loc] > li[j]:
                min_loc = j
        li[min_loc], li[i] = li[i], li[min_loc]
        print(li)


li = list(range(10))
random.shuffle(li)
select_sort(li)

