class time:
    
    def __init__(self, h, m, s):
        self.hours = h
        self.minute = m
        self.second = s 
        
    def show(self):
            print(self.hours,':', self.minute, ':', self.second)
    
    
    
    def sum(self, new):
        result = time(None,None,None)
        result.hours = self.hours + new.hours
        result.minute = self.minute + new.minute
        if result.minute >= 60:
            result.minute -=60
            result.hours +=1
        result.second = self.second + new.second
        if result.second >= 60:
            result.second -=60
            result.minute +=1
            return result
    
    def sub(self, new):
        result = time(None,None,None)
        result.hours = self.hours - new.hours
        result.minute = self.minute  - new.minute
        if result.minute <0:
            result.minute +=60
            result.hours -=1
        result.second = self.second - new.second
        if result.second <0:
            result.second +=60
            result.minute -=1
            return result
    

    def convert_timetosecond(self):
        self.second = self.hours *3600 + self.minute*60 + self.second
        print('second:' , self.second)
        
        
    def convert_secondtotime(self):
        self.hours = self.second / 3600
        self.minute = self.second /60
        self.second = (self.second %3600)%60
        
           
    
t1 =time(3, 30, 14)
t2 =time(7, 20, 15)
t3 = t1.sum(t2) 
t4 = t2.sub(t1)



t3.show()
t4.show()

    
 