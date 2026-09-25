def algo():
    pattern = "abba"
    s = "dog cat cat dog"

    mapping1={}
    mapping2={}

    p = s.split()

    for i in range(len(p)):
        if(pattern[i] in mapping1):
            if(mapping1[pattern[i]] != p[i]):
                return False
        else:
            mapping1[pattern[i]] = p[i]

        if(p[i] in mapping2):
            if(mapping2[p[i]] != p[i]):
                return False
        else:
            mapping2[p[i]] =pattern[i]
        return True
algo()
        