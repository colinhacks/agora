def approximate_search(T, S):
    """
    Search for string S in document T. Return the position of the first match,
    or None if no match.

    Parameters
    ----------
    T : str
        Document to search.
    S : str
        String to search in document.

    Returns
    -------
    pos : int or None
        Position of first approximate match of S in T, or None if no match.
    """
    table={}
    alphabet="abcdefghijklmnopqrstuvwxyz "
    a=263
    m=2**16-17
    k=len(S)
    n=len(T)
    d=25
    # initial hash of first substring length k
    string = T[:len(S)]
    EXP=a**(len(string)-1)

    string = T[:len(S)]
    count=0
    temp=EXP
    for t in range(k):
        sum+=ord(string[t])*temp
        temp = temp/a
    table[string]=count   
    
    # Hashing other substrings of T with rolling hash
    temp = EXP
    for offset in range(1+n-k)[1:]:
        old = string
        string=T[offset:k+offset]
        table[string]=(table[old]-ord(old[0])*temp)*a+ord(string[-1])

    # Initial hash of S
    string = S
    count = 0
    temp=EXP
    for t in range(k):
        sum+=ord(string[t])*temp
        temp = temp/a
    table[string]=count

    # Hashing all transposition variants
    S_LIST = list(S)
    ex = EXP
    for i in range(k)[:-1]:
        templist=S_LIST
        temp = templist[i]
        templist[i]=templist[i+1]
        templist[i+1] = temp
        table[''.join(templist)]=table[S]-(ord(S[i])*ex)-(ord(S[i+1])*(ex/a)) + (ord(S[i+1])*ex) + (ord(S[i])*(ex/a))
        ex = ex/a

    # Hashing of all substitution characters
    S_LIST = list(S)
    ex = EXP
    for i in range(k):
        templist=S_LIST
        for char in alphabet:
            if not templist[i] == char:
                templist[i]=char
                table[''.join(templist)]=table[S]-(ord(S[i])*ex) + (ord(char)*ex)
        ex = ex/a

    print table
        
        


