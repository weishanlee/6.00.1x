''''
Solutions to problems 2, 3, 4, and 5
'''

import string

class NewsStory(object):
    
    def __init__(self, the_id, the_title, the_subject, the_summary, the_address):
        '''
        Initialize a newstory the variable names are clear enough so that no
        description is required
        
        ID:             string 
        the_title:      string
        the_subject:    string
        the_summary:    string
        the_address:    string
        '''
        self.THE_ID = the_id
        self.THE_TITLE = the_title
        self.THE_SUBJECT = the_subject
        self.THE_SUMMARY = the_summary
        self.THE_ADDRESS = the_address
    
    def getGuid(self):
        # returns the ID
        return self.THE_ID
    
    def getTitle(self):
        # returns the title
        return self.THE_TITLE
        
    def getSubject(self):
        # returns the subject
        return self.THE_SUBJECT
        
    def getSummary(self):
        # returns the summary
        return self.THE_SUMMARY
        
    def getLink(self):
        # returns the web address
        return self.THE_ADDRESS
test = NewsStory('foo', "Microsoft, I love hello's. hell'o!!! soft", 'mySubject', 'some long summary', 'www.example.com')

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError
        
# Problem 2        
class WordTrigger(Trigger):
    def __init__(self, the_word):
        self.THE_WORD = the_word.lower()
    
    def isWordIn(self, the_text):
        '''
        split text up into words
        check the list of words to see if it matches the chosen word
        '''
        self.THE_TEXT = the_text.lower()
        punc = string.punctuation
        new_text = ''
        for i in self.THE_TEXT:
            if i in punc:
                new_text += " "
            else:
                new_text += i
        final = new_text.split(' ')
        if self.THE_WORD in final:
            return True
        else:
            return False
   
# Problem 3
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

# TitleTrigger inherits the methods from WordTrigger so we can put a word in the 
# brackets and this will be treated the same as it would be in WordTrigger
# Each TitleTrigger() much have its own evaluate() method as the Tigger() class will
# only raise an exception if it does not exsit
# This evaluate() method should return true
# Because we pass the variable story to evaluate() this gives us an instance that 
# we can use that to call the getTitle() method. 
# This was tricky to figure out, and I was only able to solve it by looking at the 
# testing code

koala     = NewsStory('', 'Koala bears are soft and cuddly', '', '', '')
print TitleTrigger("bears").evaluate(koala)
 
# Following on from the solution to TitleTrigger() it was easy to convert the 
# the classes for SubjectTrigger and Summary Trigger  
     
# Problem 4
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
# Problem 5
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())