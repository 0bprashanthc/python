"""
Given a string S and a set of words D, find the longest word in D that is a
subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can
be deleted from S to form W, without reordering the remaining characters.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple",
"bale", "kangaroo"} the correct output would be "apple"
"""
def longest_substring(s,d):
    largest = ''
    d = sorted(d, key=lambda x: len(x),reverse=True)
    for each_word in d:
        if is_subsequence(each_word,s) and (len(largest) < len(each_word)):
            largest = each_word
    return largest

def is_subsequence(word,s):
    to_continue = True
    while s != '' and to_continue:
        for indx,each_char in enumerate(word):
            if each_char in s:
                if indx == len(word)-1: to_continue = False
                index = s.index(each_char)
                if index != len(s)-1: 
                    s = s[index+1:]
                else:
                    return True
            else:
                return False
    return True

if __name__ == "__main__":
    s = "abppplee"
    d = ["able", "ale", "apple", "bale", "kangaroo"]
    #print(is_subsequence("kangaroo",s))
    print(longest_substring(s,d))
