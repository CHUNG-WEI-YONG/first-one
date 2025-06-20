class polygon():
    def __init__(self,width=0,length = 0):
        self.length = length
        self.width = width

    def __setattr__(self,name,value):
        
        if name == 'square':
            self.width = value
            self.length = value
        else:
           super().__setattr__(square ,  value)

    def __square(self):
        self.length == self.width
        
        
              
        
