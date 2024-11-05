import random
def randomlist():
    nums = []
    for i in range(0,10):
        n = random.randint(1,99)
        nums.append(n)
    return (nums)

def msort(mid, nlist):
    print(mid)
    
    print(nlist[:mid])
    
    print(nlist[mid:])

def main():
    nlist = randomlist()

    mid = len(nlist) // 2
    
    msort(mid,nlist)

if __name__ == "__main__":
    main()