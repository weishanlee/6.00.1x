class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print self.incantation    


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print spell

#What is printed?
# does not print anything just sets the variable spell to Accio()
spell = Accio()

# calls the method execute on the variable spell
# however there is not method execute to it goes to Accio()'s superclass and finds the method there                 
spell.execute()

# the function studySpell prints what is passed to it 
     
# the variable spell is passed to studySpell as it is an Accio() it looks for a what it should print in the 
# Accio() class. 
# Accio() class does not have a print method so it goes to its superclass and uses the method there
# the Spell() class takes three arguments to print, the name, the incantation, and a description
# Accio() has no description method associated with it, so it defaults to the superclass description method                                                         
studySpell(spell)


# the class Confondo() is passed to studySpell as with Accio() it does not have  a print method so it
# looks to its superclass/parent
# the Spell() print method is called, because Confundo() has a description method that is called in place of the 
# Spell() description method.
studySpell(Confundo())






