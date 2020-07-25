def reverse(s):
    result = ""
    i = j = len(s)-1
    while i >= 0:
        if s[i] == " ":
            result += (s[i+1:j+1]+" ")
            j = i-1
        i -= 1
    return result

if __name__ == "__main__":
    s = "i live in a house"
    print(reverse(s))
