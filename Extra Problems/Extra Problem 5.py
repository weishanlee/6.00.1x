import string

class PHPGoAway(object):
    def __init__(self):
        '''
        key: string. This is the word that is used to encode the text
        message: string This is the phrase to be encoded or decoded
        
        alphaDict : dictionary
        '''
        self.KEY = None
        self.MESSAGE = None
        
        # creates a dictionary of all the lowercase letters
        # as keys with the positions as values
        alphabet = string.ascii_lowercase
        self.alphaDict = {}
        count = 0
        for c in alphabet:
            self.alphaDict[c] = count
            count += 1 
        
        
    def setKey(self, key):
        '''
        key: string This is the word that is used to encode the text
        
        '''
        self.KEY = key
        
     
    def __createShifted(self, shift):
        '''
        shift:     int this is how far the alphabet must be shifted
        
        Returns dictionary of letter:letter that has been shifted by the required amount
        '''
        self.SHIFT = shift
        alphabet_shifted ={}
        lower_alphabet = string.ascii_lowercase
        lower_shifted = lower_alphabet
        letter_low = lower_shifted[0:self.SHIFT]
        lower_shifted += letter_low
        lower_shifted = lower_shifted[self.SHIFT:]
    
        for lower_value, shifted_value in zip(lower_alphabet, lower_shifted):
            alphabet_shifted[lower_value] = shifted_value
        return alphabet_shifted
        
    def __createTable(self, message):
        '''
        message:    String
        
        Returns a table that pairs up the letters in the message with the 
        letters in the key word
        '''
        self.MESSAGE = message
            
        # creates a table that matches each letter in the message with
        # the correct letter in the key    
        table = []
        i = 0
        for c in self.MESSAGE:
            if c != " ":
                letter = self.KEY[i%len(self.KEY)].lower()
                table.append((c.lower(), letter))
                i += 1
            else:
                table.append((" "," "))
        return table
          
    
    def forLove(self, message):
        '''
        message: string     This is what is to be encoded
        
        returns the encoded message. The assumption for this code is that spaces
        will have no effect on the encoded message
        '''
        self.MESSAGE = message

        table = self.__createTable(self.MESSAGE)        
        # this encodes the text by first calculating the shift and then using the
        # function createShifted to find the correct encoded letter   
        encoded = ''
        for x in table:
            if x[1] in self.alphaDict:
                shift = self.alphaDict[x[1]]
                shifted_alphabet = self.__createShifted(shift)
                letter = shifted_alphabet.values()[shifted_alphabet.keys().index(x[0])]                
            else:
                letter = " "
            encoded += letter
        return encoded
    
    def fromLove(self, message):
        '''
        message: string the message to be decoded
        
        returns the decrypted message. The assumption for this code is that spaces
        will have no effect on the encoded message
        '''
        self.MESSAGE = message
        
        table = self.__createTable(self.MESSAGE)         
        # this encodes the text by first calculating the shift and then using the
        # method createShifted to find the correct encoded letter   
        unencoded = ''
        for x in table:
            if x[1] in self.alphaDict:
                shift = self.alphaDict[x[1]]
                shifted_alphabet = self.__createShifted(26-shift)
                letter = shifted_alphabet.values()[shifted_alphabet.keys().index(x[0])]                
            else:
                letter = " "
            unencoded += letter
        return unencoded
        
  
# testing        
encoded = PHPGoAway()
encoded.setKey("LEMON")
print encoded.forLove("Victor lets meet at the school")
print encoded.fromLove("LXFOPVEFRNHR") 

encoded = PHPGoAway()
encoded.setKey("yophp")
print encoded.forLove("i love you")                    #g zdct wcj    
print encoded.fromLove("rvt mtczxuvq ogl bshjha")     #the feelings are mutual

      