class Day:
    def __init__(self,d1,d2):
        self.entry_1 = d1.getEntry()
        self.exit_1 = d1.getExit()
        self.entry_2 = d2.getEntry()
        self.exit_2 = d2.getExit()
        self.duration = Clock.timeSum(d1.duration,d2.duration)

    def __str__(self):
        return  "|| "  + str(self.entry_1)  + " ~ " + str(self.exit_1) + \
                " | "  + str(self.entry_2)  + " ~ " + str(self.exit_2) + \
                " | " + str(self.duration) + " ||"

class Duration:
    def __init__(self,c1,c2):
        self.entry = c1
        self.exit = c2
        self.duration = Clock.difference(self.entry, self.exit)

    def getDuration(self):
        return self.duration

    def getEntry(self):
        return self.entry
    
    def getExit(self):
        return self.exit

    def __str__(self):
        return self.duration


class Clock:
        
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) + "h"

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes
        
    def setHours(self, hours):
        self.hours = hours
        
    def setMinutes(self, minutes):
        self.minutes = minutes
    
    @classmethod
    def timeSum(clock,c1,c2):
        
        h = c1.getHours() + c2.getHours() + (c1.getMinutes() + c2.getMinutes())//60
        m = (c1.getMinutes() + c2.getMinutes())%60
        c = clock(h,m)

        return c

    @classmethod
    def difference(clock,c1,c2):

        elapsed_time = ((c2.getHours() * 60) + c2.getMinutes()) - ((c1.getHours() * 60) + c1.getMinutes())

        if elapsed_time < 0:
            return 0
            
        c = clock(elapsed_time//60, elapsed_time%60)
 
        return c

class Chart:
    def __init__(self):
        self.durations = []
    
    def insertDay(self,day):
        self.durations.insert(-1,day)

    def __str__(self):

        bound = "================================================\n"
        title = "|| entry1 ~ exit1  | entry2 ~ exit2  | Total  ||\n"
        line  = "||-----------------+-----------------+--------||\n"

        body = line.join([str(day) + "\n" for day in self.durations])

        return bound + title + line + body + bound


c1 = Clock(9,30)
c2 = Clock(14,30)
c3 = Clock(16,0)
c4 = Clock(19,30)
d1 = Duration(c1,c2)
d2 = Duration(c3,c4)
day = Day(d1,d2)
chart = Chart()
chart.insertDay(day)
chart.insertDay(day)
chart.insertDay(day)
chart.insertDay(day)