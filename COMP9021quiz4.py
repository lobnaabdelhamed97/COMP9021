# -*- coding: utf-8 -*-

import sys


def encode(list_of_integers):
    # print(list_of_integers)
    result = ""
    for item in list_of_integers:
        bin_item = bin(item)[2:]
        for e in bin_item:
            result = result + str(e)*2
        result = result +'0'
    result = result[:-1]
    return int(result,2)


def decode(integer):
    temp = ""
    result = list()
    str1 = str(bin(integer)[2 :])
    i = 0
    if len(str1)==1:return None
    while(True):
        try:
            if(str1[i] == str1[i+1]):
                temp = temp + str1[i]
                i = i + 2
            elif str1[i]!=str1[i+1] and str1[i]=='0':
                result.append(temp)
                temp=""
                i = i + 1
            else:
                return None
        except IndexError:
            return None

        if i >= len(str1):
            break
    result.append(temp)
    
    return [int(e,2) for e in result]


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))