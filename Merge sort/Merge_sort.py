import random
def randomlist():
    nums = []
    for i in range(0,10):
        n = random.randint(1,99)
        nums.append(n)
    return (nums)

def msort( nlist):
    mid = len(nlist) // 2
    print(nlist)
    if len(nlist) <= 1:
        return nlist
    
    msort((nlist[:mid]))

def main():
    nlist = randomlist()
    print(msort(nlist))

if __name__ == "__main__":
    main()