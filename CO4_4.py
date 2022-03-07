"""
4. Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to
find sum of 2 time.
"""

#Rahul MS 
#21MCA035
class Time:
    __hour=0
    __minute=0
    __second=0
    def __init__(self):
        self.hour=int(input("enter hour"))
        self.minute=int(input("enter minute"))
        self.second=int(input("enter second"))
    
    def __add__(self,obj):
        day=0
        sec1=self.second+obj.second
        mins=sec1//60
        sec1=sec1%60
        min1=self.minute+obj.minute+mins
        hrs=min1//60
        min1=min1%60
        hour1=self.hour+obj.hour+hrs
        day=hour1//24
        hour1=hour1%24
        return "{}:{}:{}:{}".format(day,hour1,min1,sec1)

t1=Time()
t2=Time()


print(t1+t2)