

def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        print(li)
        if not exchange:
            break


li = [7, 8, 3, 12, 11, 1, 2, 5]
bubble_sort(li)