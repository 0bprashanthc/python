# coding: utf-8 
"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""
def string_splosion(string):
    result = ''
    for i in range(len(string)):
        result += string[:i+1]
    return result

if __name__ == "__main__":
    print(string_splosion('Code'))
    print(string_splosion('abc'))
    print(string_splosion('ab'))