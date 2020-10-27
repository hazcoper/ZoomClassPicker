import datetime
import os
import re

#chage to the dir
print(os.getcwd())
os.chdir("C:/Users/Hazcoper/Desktop/getAulas")
# get the day of the week
# get the time

today = datetime.datetime.now()
day = today.strftime("%w")
hour = today.strftime("%H")
minute = today.strftime("%M") 


main_link = ""
#open the file and read line by line
with open("link_aulas.txt", "r") as file:
    line = file.readline()
    data = re.split(',|;', line)
    while(line != ""):
        line = file.readline()           #readline
        data1 = re.split(',|;', line)    # parse line
        if len(data1) < 2:
            break    #discard empty line
        if int(data1[2]) == day:
            if int(data[2]) != day:
                data = data1 # means the first class is trash so I wil; change it and move one
            elif hour - int(data1[3].split("h")[0]) < hour - int(data[3].split("h")[0]):
                #this is closer to the time then the one I have so change class
                data = data1

print(f"""
Aula : {data[1]}
Horario : {data[3]}
{data[0]}
""")
