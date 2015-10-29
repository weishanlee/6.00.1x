''''
Solutions to problems 2, 3, 4, 5, 6, 7, 8, 9
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

#koala     = NewsStory('', 'Koala bears are soft and cuddly', '', '', '')
#print TitleTrigger("bears").evaluate(koala)
 
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
        
# Problem 6
class NotTrigger(Trigger):
    def __init__(self, the_trigger):
        self.THE_TRIGGER = the_trigger
    def evaluate(self, story):
        return not self.THE_TRIGGER.evaluate(story)
        
# Problem 7
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.TRIGGER1 = trigger1
        self.TRIGGER2 = trigger2
    def evaluate(self, story):
        return self.TRIGGER1.evaluate(story) and self.TRIGGER2.evaluate(story)
        
# Problem 8
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.TRIGGER1 = trigger1
        self.TRIGGER2 = trigger2
    def evaluate(self, story):
        return self.TRIGGER1.evaluate(story) or self.TRIGGER2.evaluate(story)
        
# Problem 9
class PhraseTrigger(WordTrigger):
    def __init__(self, the_phrase):
        self.THE_PHRASE = the_phrase
    def evaluate(self, story):
        return self.THE_PHRASE in story.getSubject() or self.THE_PHRASE in story.getTitle() or self.THE_PHRASE in story.getSummary()

# Solution to problem 9 is really quite straight forward. It involves checking each
# of the story - subject, title, summary to see if the chosen phrase in in it

# Problem 10
def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    
    This cycles through all the stories and the triggers
    if the trigger fires for a specific story then it returns true
    before storing the story in filtered it is checked to see if it is already there
    """

     
    filtered= []
    for story in stories:
         for trig in triggerlist:
             if trig.evaluate(story):
                if story not in filtered:
                    filtered.append(story)
    return filtered
    
pt = PhraseTrigger("New York City")
a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
noa = NewsStory('', "something something new york city", '', '', '')
nob = NewsStory('', '', "something something new york city", '', '')
noc = NewsStory('', '', '', "something something new york city", '')

triggers = [pt]
stories = [a, b, c, noa, nob, noc]
        
print filterStories(stories, triggers)
            

        
        