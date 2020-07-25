"""
2[a3[bc]]
source_arr => ba3[3]2
source_arr => 2[a3[bc]]
result = []
source_arr:
    2,[,a,3,[,b,c,
    value_buff = []
    pop()=> ]
    pop()=> value_buff[c,b] ( value )
    pop()=> [
    pop()=> 3 ( multiplier )
b,a append()=> value_buff*multiplier => result
b,a,3,3,3
    append() => 2
"""
print string_compress(str_):
    result = []
    for char in str_:
        if char is not ']':
            result.append(char)
        else:
            value_buff = []
            while c is not '[':
                value_buff.append(result.pop())
                c = result.pop()
            multiplier = c.pop()
            string = ''.join(value_buff)*multiplier
            #bc*3 => bcbcbc
            #abcbcbc*2 = abcbcbcabcbcbc
            result.extend(string)
            #2[abcbcbc
    return ''.join(result)
