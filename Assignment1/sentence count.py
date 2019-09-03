def wordcount(sentence):
    upper = 0
    lower = 0
    number = 0
    special = 0

    for i in range(len(sentence)):
        if sentence[i] >= 'A' and sentence[i] <= 'Z':
            upper += 1
        elif sentence[i] >= 'a' and sentence[i] <= 'z':
            lower += 1
        elif sentence[i] >= '0' and sentence[i] <='9':
            number += 1
        else:
            special = special + 1
    print("Upper case letters:", upper)
    print("Lower case letters:", lower)
    print("Numbers:", number)
    print("Special: ", special)



sentence = input("Enter Sentence:")
wordcount(sentence)

