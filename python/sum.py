def sum(lst, n):
    # Your code here!
    l = len(lst)
    for i in range(l):
        for j in range(i+1,l):
            if(lst[i] + lst[j]  == n):
                return True
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()