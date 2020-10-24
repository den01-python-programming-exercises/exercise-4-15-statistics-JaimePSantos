class Statistics:

    def __init__(self):
        # initialize the variables count and sum here
        self.count = 0
        self.sum = 0

    def add_number(self,number):
        # write code here
        self.count+=1
        self.sum+=number
    
    def sum(self):
      return self.sum

    def get_count(self):
        # write code here
        return self.count
    
    def average(self):
      return (self.sum/self.count)