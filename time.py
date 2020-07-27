from TheTimeController import *
import re

chart = Chart()

######################################################################################
######################################################################################
######################################################################################

## Introduce el nombre del archivo
name = "HORAS"

## Introduce las horas de entrada y salida.
## En caso de no querer poner una hora, puedes poner como entrada y salida las 00:00

chart.insertDay(Day.rawDay(8,15, 14,30,   16,15, 19,35))
chart.insertDay(Day.rawDay(8,15, 14,30,   16,15, 19,35))
chart.insertDay(Day.rawDay(8,15, 14,30,   16,15, 19,35))
chart.insertDay(Day.rawDay(8,15, 14,30,   16,15, 19,35))
chart.insertDay(Day.rawDay(8,15, 14,30,   16,15, 19,35))
chart.insertDay(Day.rawDay(8,15, 14,30,   00,00, 00,00))
chart.insertDay(Day.rawDay(8,15, 14,30,   16,15, 19,35))
chart.insertDay(Day.rawDay(8,15, 14,30,   16,15, 19,35))
chart.insertDay(Day.rawDay(8,15, 14,30,   16,15, 19,35))
chart.insertDay(Day.rawDay(8,15, 14,30,   16,15, 19,35))
chart.insertDay(Day.rawDay(8,15, 14,30,   16,15, 19,35))
chart.insertDay(Day.rawDay(8,15, 14,30,   16,15, 19,35))
chart.insertDay(Day.rawDay(8,15, 14,30,   16,15, 19,35))


######################################################################################
######################################################################################
######################################################################################

output = re.sub("00:00h ~ 00:00h", "---------------", str(chart))
print(output)

## Print output to file
text_file = open(name + ".txt", "w")
n = text_file.write(output)
text_file.close()
