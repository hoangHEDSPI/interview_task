import sys
from collections import OrderedDict

if __name__=="__main__":
  	# Read from stdin
    dictionary = OrderedDict()
    line_counter = 0
    look_up_word = None
    for line in sys.stdin:
        if line_counter == 0:
          	continue
        else:
            word_definition = line.split(":")
            if len(word_definition) > 1:
                dictionary[word_definition[0]] = word_definition[1]
            else:
                look_up_word = word_definition[0]
        line_counter += 1

    # Sort dictionary key alphabetically
    keyList = sorted(dictionary.keys())
    resultKeys = []
    counter = 0
    for i, v in enumerate(keyList):
        if v == look_up_word:
            resultKeys = keyList[i:i+6]

    if len(resultKeys) == 0:
        print([])
    else:
        for i in resultKeys:
            print(i + ":" + dictionary[i])