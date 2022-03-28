class clock:
    def __init__(self):
        self.hour = 0
        self.minutes =0
        self.seconds = 0

    def sethour(self,hour):
       self.hour = hour
       return self.hour
    def setminutes(self,minute):
        self.minutes = minute
        return self.minutes
    def setseconds(self,seconds):
        self.seconds = seconds
        return self.seconds
    def showtime(self):
        print(str(self.hour)+":"+str(self.minutes)+":"+str(self.seconds))

c = clock()
hour = int(input("hour"))
minute = int(input("minute"))
seconds = int(input("seconds"))
c.sethour(hour)
c.setminutes(minute)
c.setseconds(seconds)
c.showtime()