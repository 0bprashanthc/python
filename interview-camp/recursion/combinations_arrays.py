#print all possible combination arrays of input length x



def printCombos(array,buffer,start_index,buffer_index):
    if start_index == len(array):
        return None
    if buffer_index == len(buffer):
        print buffer
        return None
    for i in range(len(a)):
        buffer[buffer_index] = a[i]
        printCombos(a,b,i+1,buffer_index+1)
