def max_length(s):
    max_ind = 0
    for i in range(0,len(s)):
        diff = 0
        for j in range(len(s)-1,i,-1):
            if s[i] == "(" and s[j] == ")":
                diff = j - i
                break
        if max_ind < diff:
            max_ind = diff
    return max_ind

if __name__ == "__main__":
    s = "((()"
    print(max_length(s))
