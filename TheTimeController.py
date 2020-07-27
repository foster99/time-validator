import operator
import functools

class Day:
    def __init__(self,d1,d2):
        self.entry_1 = d1.getEntry()
        self.exit_1 = d1.getExit()
        self.entry_2 = d2.getEntry()
        self.exit_2 = d2.getExit()
        self.duration = d1.duration + d2.duration
    
    @classmethod
    def rawDay(self,h0,m0,h1,m1,h2,m2,h3,m3):
        c1 = Clock(h0,m0)
        c2 = Clock(h1,m1)
        c3 = Clock(h2,m2)
        c4 = Clock(h3,m3)
        d1 = Duration(c1,c2)
        d2 = Duration(c3,c4)
        return Day(d1,d2)

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
        if self.hours < 100:
            return str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2) + "h"

        return str(self.hours).zfill(3) + ":" + str(self.minutes).zfill(2) + "h"


    def __add__(self,other):
        h = self.getHours() + other.getHours() + (self.getMinutes() + other.getMinutes())//60
        m = (self.getMinutes() + other.getMinutes())%60
        return Clock(h,m)

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes
        
    def setHours(self, hours):
        self.hours = hours
        
    def setMinutes(self, minutes):
        self.minutes = minutes
    

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

        body  = line.join([str(day) + "\n" for day in self.durations])
        total_count = functools.reduce(operator.add, [day.duration for day in self.durations], Clock(0,0))

        if total_count.getHours() < 100:
            total = "||                         TOTAL TIME: " + str(total_count) + " ||\n"
        else:
            total = "||                        TOTAL TIME: " + str(total_count) + " ||\n"

        return bound + title + bound + body + bound + total + bound
