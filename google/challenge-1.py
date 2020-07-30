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

def index_hash(s):
    ih = dict()
    for index,char in enumerate(s):
        if char in ih:
            ih[char].append(index)
        else:
            ih[char] = [index]
    return ih

def is_subsequence(word,s):
    to_continue = True
    ih = index_hash(s)
    x = -1
    for each_char in word:
        if each_char in ih:
            x = search_x(ih[each_char],x)
            if x == -1:
                return False
        else:
            return False
    return True

def search_x(array, x):
    low,mid,high = 0,0,len(array)-1
    while low < high:
        mid = (low+high)/2
        if array[mid] < x:
            low = mid+1
        elif array[mid] == x:
            return mid+1
        elif array[mid] > x:
            high = mid-1
    return array[mid]

if __name__ == "__main__":
    s = "abppplee"
    d = ["able", "ale", "apple", "bale", "kangaroo"]
    #print(is_subsequence("kangaroo",s))
    print(longest_substring(s,d))
