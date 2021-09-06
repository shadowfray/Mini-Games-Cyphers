'''
Shadowfray
Trying to write some basic cyphers
'''
def main(phrase):
    output = caesar(phrase,3,0)
    final = caesar_decrypt(output,3)
    
'''
Caesar() takes an input string to be scrambled among the ASCII characters,
values 32-126. It takes a shift among, how much you want to move them in
either direction for the cypher. Finally, it has the option of superscrable,
where it changes each value by the constant value with each cycle. For
example, if SUPERSCRABLE = 2 it would change it by +2, +4, +6, and so on
with each cycle. This feature is assumed to be off.
'''
def caesar(inputstr, shift,superscramble=0):
    shift = int(shift)
    split_input = []
    asci_holdstring = []
    output = []
    split_input += inputstr
    #a = 1 or 0, 1 means superscramble is on
    a = 0

    for i in split_input:
        ascival = ord(i)
        asci_holdstring.append(ascival)
        
    for m in asci_holdstring:
        
        a += 1
        #to avoid the first 31 characters of the table
        m -= 31
        #The %95 stops out values from getting too large and beyond the table
        #superscrable is here but assumed off
        asci_returnval = ((m+shift)+(a*superscramble))%95
        asci_returnval += 31
        ascichr = chr(asci_returnval)
        output.append(ascichr)
        
    final = ''.join(output)
    return final

'''Tries shifting the words to find the real message, assuming it was
encrypted using the same method here but you for some reason lost
the key. Cycles through all possible outputs using this technique.
'''
def caesar_decrypt_guess(inputstr, shift=0,superscramble=0):
    split_in = []
    split_in += inputstr
    f_output = ''
    a, i = 0,0
    
    while i < 95:
        i += 1
        output = []
        asci_holdstring = []
            
        for m in split_in:
            ascival = ord(m)
            asci_holdstring.append(ascival)
            #print(asci_holdstring)

        for n in asci_holdstring:
            a += 1
            n -= 31
            #if you know shift?
            asci_returnval = ((n-i)-a*superscramble)%95
            asci_returnval += 31
            ascichr = chr(asci_returnval)
            output.append(ascichr)

        f_output = ''.join(output)
        print(i, f_output)

#Used to decrypt your messages
def caesar_decrypt(inputstr, shift):
    split_in = []
    split_in += inputstr
    f_output = ''
    output = []
    asci_holdstring = []

    for m in split_in:
        ascival = ord(m)
        asci_holdstring.append(ascival)

    for i in asci_holdstring:
        i -= 31
        asci_returnval = (i - shift)%95
        asci_returnval += 31
        ascichr = chr(asci_returnval)
        output.append(ascichr)

    f_output = ''.join(output)
    print(f_output)

#creates a key based on the day
def shiftgen(val):
    #take the day the message was sent for val
    #so if it was sent on 3/2/2019, val = 3219
    val = ((val*2 + 20)**2)//308
    val = val % 4000
    return val
        

'''
Makes a matrix with 3 rows and enough columns to fill the entire phrase.
It adds spaces to make the script enough for the length to be a multiple
of 3 to avoid index errors in the step where it splits the phrase among
the 3 lists. It then combines List 1 + List 2 + List 3.
"Hello" becomes:
["H","l"]
["e","o"]
["l"," "]
and then: "Hleol "
'''
def matrix(inputstr):
    printlist = False
    inputlist = []
    inputlist += inputstr
    list1,list2,list3 = [], [],[]
    count = 0

    #puts in spaces to avoid index error
    #you need the difference of the remainder, not the remainder
    remainder = 3-(len(inputlist)%3)
    for l in range(remainder):
        inputlist.append(' ')


    while inputlist != [] :
        list1 += inputlist[0]
        inputlist.pop(0)
        list2 += inputlist[0]
        inputlist.pop(0)
        list3 += inputlist[0]
        inputlist.pop(0)
        count += 1

    if printlist == True:
        print(list1)
        print(list2)
        print(list3)

    finallist = list1 + list2 + list3
    final = ''.join(finallist)
    final = final.strip()
    return final

#The inverse of matrix() to decode it
def dematrix(inputstr):
    output = []
    input_split = list(inputstr)

    #reformats it so it will fit
    input_length = len(input_split)
    if input_length % 3 != 0:
        remainder = 3 - input_length % 3
        for i in range(remainder):
            input_split.append(' ')
        adj_len = len(input_split)

    third = adj_len//3
    for i in range(third):
        output.append(input_split[i])
        output.append(input_split[i+third])
        output.append(input_split[i+third+third])
    final = ''
    final = final.join(output)
    return final

    

