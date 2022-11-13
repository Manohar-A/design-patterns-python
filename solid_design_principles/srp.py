# srp = Single Responsibility Priciple 
# soc = Separatio of Concerns
"""If you have a class, the class should have its primary responsility, whatever its meant to be doing.
    and it should not take on other responsibilities."""



class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self,text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self,position):
        del self.entries[position]

    def __str__(self) -> str:
        return '\n'.join(self.entries)

    # storing and removing is the Journal's primary resposibility. 
    # we are not breaking the principle yet,

    # let's give the journal the secondary responsibility to save

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    
    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass

    # adding this secondary responsibility is bad for so many reasons
    """If we have a complete website, where in addition to journals we have other differnt types,
     all those types might have same save, load and load_from_web methods."""

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry("I started the design patterns today")
j.add_entry("I should finish the course in a month's time")
print(f"Journal entries: \n{j}")

file = r'C:\Users\Manohar\Desktop\design-patterns\design-patterns-python\journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())


"""
key-takeaway: Do not overload the objects with too many responsibilites.
Anti-pattern: patterns are good. Anti-patterns are bad.
God object is one of the anti patterns.
    --- sticking everything into a single class and have a massive class at the end.
SRP prevents you from making God objects and enforces the idea that 
"A class should have a single reason to change and that change should be somehow related to its primary responsibility."
"""