import random, time
def randomlist():
    nums = []
    for i in range(0,100000):
        n = random.randint(1,99)
        nums.append(n)
    return (nums)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result 

def msort( nlist):
    mid = len(nlist) // 2
    print(nlist)
    if len(nlist) <= 1:
        return nlist
    left = msort(nlist[:mid])
    right = msort(nlist[mid:])
    return merge(left, right)

def main():
    start = time.time()
    nlist = randomlist()
    print(msort(nlist))
    end = time.time()
    length = end - start
    print(f"It took {length} seconds to finish!")
if __name__ == "__main__":
    main()