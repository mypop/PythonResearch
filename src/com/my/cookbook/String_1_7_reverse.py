'''
Created on Mar 12, 2017

@author: mayue
'''

test_string = "This is my python world."

# reverse by letters
print "reversed str: ", test_string[::-1]

# reverse by word
word_list = test_string.split()
word_list.reverse()
print "reversed str: ", " ".join(word_list)

# reverse by word
import re
word_list = re.split(r'(\s+)', test_string)
word_list.reverse()
print "reversed str: ", ''.join(word_list)