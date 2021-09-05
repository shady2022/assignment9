class fraction:
     
     def __init__(self, s, m):
         self.soorat = s
         self.makhraj = m
         
         
     def show(self):
         print(self.soorat, '/', self.makhraj)
         
         
     def mul(self, jadid):
         result = fraction(None,None)
         result.soorat = self.soorat * jadid.soorat
         result.makhraj = self.makhraj * jadid.makhraj
         return result
     
     def sum(self, jadid):
         result = fraction(None,None)
         result.soorat = self.soorat*jadid.makhraj + jadid.soorat*self.makhraj
         result.makhraj = self.makhraj*jadid.makhraj
         return result
     
     def div(self, jadid):
         result = fraction(None,None)
         result.soorat =self.soorat*jadid.makhraj
         result.makhraj = self.makhraj*jadid.soorat
         return result
     
     def sub(self, jadid):
         result = fraction(None,None)
         result.soorat = self.soorat*jadid.makhraj - jadid.soorat*self.makhraj
         result.makhraj = self.makhraj*jadid.makhraj
         return result
       
     
     
a = fraction(3,5)
b = fraction(4,3)
c = a.mul(b)
d = a.sum(b)
e = a.div(b)
f = a.sub(b)


a.show()
b.show()
c.show()
d.show()
e.show()
f.show()