def rm_smallest(d):
    # Your code here!
    m=0
    if(len(d)==0):
        return d
    value = 'a'
    for i in d:
        if(d[i]<=m):
            m=d[i]
            value = i
    d.pop(value)
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()