"""Count words in file."""


# put your code here.

#pseudocode:
#def function
#create blank dictionary for word count
#open the file
#iterate through the file
#determine each word
#count each word in the file
#close file


def word_count(file_name):

    counting_words = {}
    
    with open(file_name) as test_file:  
        
        for line in test_file:
            line = line.rstrip()
            line = line.replace(",", "")
            line = line.replace(".", "")
            line = line.replace("?", "")
            words = line.split(' ')

            for word in words:
                word = word.lower()
                counting_words[word] = counting_words.get(word, 0) + 1         
    
    return counting_words

word_counts = word_count('test.txt')
print(word_counts)


