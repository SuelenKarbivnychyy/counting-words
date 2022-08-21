"""Count words in file."""


# put your code here.

#pseudocode:
#def function
#create blank dictionary for word count
#open the file
#iterate through the file
#replace punctuation with empty string
#split lines by space, and save it to a variable words
#iterate through each word in the split file
#set every word to be lower case
#append each word to new list, check if word in new list, if word in list increase word by one.


import sys

def tokenize(file_name):
    list_of_words = []

    with open(file_name) as test_file:
        file_text = test_file.read() #reading the whole file at once as string
        file_text = file_text.lower()
        file_text = file_text.replace(",", "").replace(".", "")
        list_of_words = file_text.split() #spliting each word and saving to the list_of_words list
    return list_of_words


#         for line in test_file.readlines():  
#             line = line.replace("\n", "")
#             line_list = line.split(" ")            
#             list_of_words += line_list
            
#     return list_of_words 

def count_words(list_of_string):

    number_of_ocurrences = {}

    for string in list_of_string:

        counter = number_of_ocurrences.get(string, 0) #0 is default value if not found. get is getting value of the key "string"
        counter += 1
        number_of_ocurrences[string] = counter
        
        # number_of_ocurrences[string] = number_of_ocurrences(string, 0) +1        
    
    return number_of_ocurrences
    
def print_word_counts(word_counts):

    for word in word_counts:
        print(word , word_counts[word])


#function call / main program
if len(sys.argv) == 2:    
    list_of_words = tokenize(sys.argv[1]) #function call if has 2 arguments
    count_of_words = count_words(list_of_words)
    # print(list_of_words)   
    # print(count_of_words)
    print_word_counts(count_of_words)
else: #dont run the program otherwise
    print("Missing one arg")    



