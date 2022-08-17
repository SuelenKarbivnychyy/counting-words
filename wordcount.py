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


def word_count(file_name):

    counting_words = {}
    
    with open(file_name) as test_file:  
        
        for line in test_file.readlines():
            line = line.rstrip()
            line = line.replace(",", "").replace(".", "").replace("?", "")
            words = line.split(' ')

            for word in words:
                word = word.lower()
                counting_words[word] = counting_words.get(word, 0) + 1         
    
    return counting_words

word_counts = word_count('test.txt')
print(word_counts)