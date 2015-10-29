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
        
test = NewsStory('foo', 'myTitle', 'mySubject', 'some long summary', 'www.example.com')

print test.getGuid()
print test.getTitle()
print test.getSubject()
print test.getSummary()
print test.getLink()