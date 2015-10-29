# 6.00.1x Problem Set 7
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, the_id, the_title, the_subject, the_summary, the_address):
        '''
        Initialize a newstory
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
        return self.THE_ID
    
    def getTitle(self):
        return self.THE_TITLE
        
    def getSubject(self):
        return self.THE_SUBJECT
        
    def getSummary(self):
        return self.THE_SUMMARY
        
    def getLink(self):
        return self.THE_ADDRESS
        

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5
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


# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())


# Composite Triggers
# Problems 6-8
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, the_trigger):
        self.THE_TRIGGER = the_trigger
    def evaluate(self, story):
        return not self.THE_TRIGGER.evaluate(story)
        
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.TRIGGER1 = trigger1
        self.TRIGGER2 = trigger2
    def evaluate(self, story):
        return self.TRIGGER1.evaluate(story) and self.TRIGGER2.evaluate(story)
        
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.TRIGGER1 = trigger1
        self.TRIGGER2 = trigger2
    def evaluate(self, story):
        return self.TRIGGER1.evaluate(story) or self.TRIGGER2.evaluate(story)


# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(WordTrigger):
    def __init__(self, the_phrase):
        self.THE_PHRASE = the_phrase
    def evaluate(self, story):
        return self.THE_PHRASE in story.getSubject() or self.THE_PHRASE in story.getTitle() or self.THE_PHRASE in story.getSummary()


def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    # TODO: Problem 11
    phrase = ""
    for i in params:
        phrase += i + " "
    phrase = phrase[:-1] 
    
    if triggerType == "TITLE":
        triggers = TitleTrigger(phrase)
        
    elif triggerType == "SUBJECT":
        triggers = SubjectTrigger(phrase)
        
    elif triggerType == "SUMMARY":
        triggers = SummaryTrigger(phrase)
        
    elif triggerType == "PHRASE": 
        triggers = PhraseTrigger(phrase)
        
    if triggerType == "AND":
        triggers = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
    
    if triggerType == "OR":
        triggers = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
        
    if triggerType == "NOT":
        triggers = NotTrigger(triggerMap[params[0]]) 
   
        
    triggerMap[name] = triggers
    return triggerMap[name]
    
makeTrigger({}, "SUBJECT", ['world'], "t1")


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}
    print lines
    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])
            print "----"
            print triggerMap, linesplit[1], linesplit[2:], linesplit[0] 

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])
    print triggers
    return triggers
    
readTriggerConfig("/Users/andrewmarmion/Google Drive/Python/6.00.1x/PS07/triggers.txt")
