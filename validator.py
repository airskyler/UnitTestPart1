__author__ = 'Jessy'


## LAB 3 , Part 1

## I got some help from Mason from Learning center for this problem



def main():

    sentence = userInput()

    if not valid_sentence(sentence):
        print("Can't process this input")
        return


    words = split(sentence)   ## Split the sentence to each word separated by space


    method_name = ""


##  Start looping over each word that was split from sentence
    first_word_done = False

    for word in words:

        if not first_word_done:  ## if it is not TRUE
            camel = first_word(word)  ##  make the first word that was split to all lower case letter
            first_word_done = True


##  start to make the second word and word after the second word split from the sentence
##  to change the first letter to upper case and rest of the letter in word to
##  lower case
        else:
            camel = camelcase_word(word)

##  add first word first and kipping adding the second word and on
##  to create a new sentence
        method_name += camel


##  print the new sentence
    display_output(method_name)



##   simple validating method for testing a sentence
##   if the split sentence have more than one word,
##   return True, if not return False

def valid_sentence(sentence):
    test = sentence.split()


    if len(test) < 1:
        return False

    for word in test:

        if "'" in word:     ## if the sentence from the word contain single quotation
            return False    ##  return false


        if "-" in word:     ## if sentence from word contain "-" return false
            return False


        if "\"" in word :   ## if the sentence from the word contain double quotation
            return False    ##  return false


        if test[0].isnumeric():    ## if the sentence contains a number, return false
            return False


    return True






def display_output(output):
    print(output)



def first_word(word):   ## make the first word from the sentence all lower case letter
    return word.lower()


def camelcase_word(word):       ## make the first letter from word upper case and
    inlowercase = word.lower()  ## make the rest of the letter from word a lower case letter
    firstletter = word[0]       ##  and add the first word from the sentence and rest of the
    firstletter = firstletter.upper()       ## words together to create new sentence
    rest_of_word = inlowercase[1:]

    camelcased = firstletter + rest_of_word

    return camelcased


if '__name__ ' == '__main__':
    main()



## asking for user input on sentence
def userInput():

    sentence = (input("please write a sentence"))

    return sentence



## split the sentence by space between the words
def split(words):
    Allword = words.split()
    return Allword








