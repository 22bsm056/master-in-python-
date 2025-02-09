#write a python program for IIITDM Jabalpur students so anyone can get information  about students using your class.
class Students:
    def __init__(self,name,roll,branch,cpi,home):
        self.name= name
        self.roll=roll
        self.branch=branch
        self.cpi=cpi
        self.home=home
    def info(self):
        return f"{self.name,self.roll,self.branch,self.cpi,self.home}"
class Other(Students):
    def __init__(self,name,roll,branch,cpi,home,clg):
        super().__init__(name,roll,branch,cpi,home)
        self.clg=clg
    def info(self):
        return f"{super().info(),self.clg}"
std1=Students("shubham","22bsm056","smart manufacturing","7","nawada")
#print(std1.branch,std1.name,std1.cpi,std1.home,std1.roll)
std2=Other("aman","jec46","cse","8","jabalpur","Jec")
#now add function so i can get all details using only that function
print(std1.info())
print(std2.info())


