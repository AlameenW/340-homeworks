class Search_Pattern:
    def __init__(self,reference):
        self.reference = reference
    
    def contains(self, pattern):
        if(pattern in self.reference):
            print(f'{pattern} is in {self.reference}')
        else:
            print(f'{pattern} is not in {self.reference}')

    def isSubset(self,pattern):
        sRef = dict(self.reference.split())
        sPat = dict(pattern.split())
        if(sPat <= sRef):
            print(f'{pattern} is a subset if {self.reference}')
        else:
            print(f'{pattern} is not a subset if {self.reference}')

regex = Search_Pattern('This is a test')
regex.contains("This is a subset")
regex.isSubset("This is a test")
    
