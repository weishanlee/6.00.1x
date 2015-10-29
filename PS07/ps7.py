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

#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering)
    
    
    filtered= []
    for story in stories:
         for trig in triggerlist:
             if trig.evaluate(story):
                if story not in filtered:
                    filtered.append(story)
    return filtered

#======================
# Part 4
# User-Specified Triggers
#======================

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
    # remove the phrase from the list and convert it to a string
    phrase = ""
    for i in params:
        phrase += i + " "
    phrase = phrase[:-1] 
    
    # check to see what triggerType it has
    # set up appropriate trigger
    if triggerType == "TITLE":
        triggers = TitleTrigger(phrase)
        
    elif triggerType == "SUBJECT":
        triggers = SubjectTrigger(phrase)
        
    elif triggerType == "SUMMARY":
        triggers = SummaryTrigger(phrase)
        
    elif triggerType == "PHRASE": 
        triggers = PhraseTrigger(phrase)
        
    # beause triggers are stored in triggerMap pull them out using their param name    
        
    elif triggerType == "AND":
        triggers = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
    
    elif triggerType == "OR":
        triggers = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
        
    elif triggerType == "NOT":
        triggers = NotTrigger(triggerMap[params[0]]) 
   
    # assign the new trigger to its name in the dictionary
    triggerMap[name] = triggers
    
    # return the triggerMap
    return triggerMap[name]


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
    
    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        triggerlist = readTriggerConfig("/Users/andrewmarmion/Google Drive/Python/6.00.1x/PS07/triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Andy's RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

