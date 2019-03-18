# Task 1
# line chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('C:/Users/TheLegitOne/Desktop/data_tasks.xlsx', sheet_name = 'task1')
def x():
    minutes = []
    for i in df.values[:,0]:
        minutes.append(i)
    return minutes
def y():
    temperature = []
    for i in df.values[:,1]:
        temperature.append(i)
    return temperature
def errors():
    errors = []
    for i in df.values[:,2]:
        errors.append(i)
    return errors

error_barValues = errors()
x_values = x()
y_values = y()

line, caps, bars = plt.errorbar(x_values, y_values, yerr = error_barValues,
                                linewidth = 3, elinewidth = .5, ecolor ='k', 
                                capsize = 4, capthick = 1)
plt.legend(["Error Bars (stdev)"], numpoints = 1, loc = ("upper left"))
plt.ylabel("Temperature (C)", fontsize = 12)
plt.xlabel("Time (min)", fontsize = 12)
plt.xlim((.5, 9.5))
plt.xticks([1,2,3,4,5,6,7,8,9])
plt.yticks([0, 5, 10, 15, 20, 25])
plt.title("Task 1", fontsize = 18)
plt.show()
plt.savefig("Task1.png", dpi = 600)
plt.clf()

# Bar chart
plt.bar(x_values, y_values, yerr = error_barValues, align = "center", ecolor = 'black', capsize = 10)
plt.xticks([1,2,3,4,5,6,7,8,9])
plt.yticks([0,5,10,15,20,25])
plt.xlim((.5, 9.5))
plt.ylabel("Temperature (C)", fontsize = 12)
plt.xlabel("Time (min)", fontsize = 12)
plt.title("Task 1", fontsize = 18)
plt.savefig('Task1_2.png', dpi = 600)
plt.show()
plt.clf()

# Task 2
# Bar chart
df2 = pd.read_excel('C:/Users/TheLegitOne/Desktop/data_tasks.xlsx', sheet_name = 'task2')

barWidth = .25

Header_names = list(df2.drop(df2.columns[df2.columns.str.contains('unnamed',case = False)],axis = 1))       
Header_names.remove("Cities")

x = (df2.values[1:8,0])
time1 = (df2.values[1:8,1])
err1 = (df2.values[1:8,2])
time2 = (df2.values[1:8,3])
err2 = (df2.values[1:8,4])
time3 = (df2.values[1:8,5])
err3 = (df2.values[1:8,6])

r1 = range(1,7)
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.title("Cities", fontsize = 18)
plt.bar(r1, time1, width = barWidth, color = '#7f6d5f', edgecolor = "white", label = Header_names[0], yerr = err1, capsize = 5, align = "center")
plt.bar(r2, time2, width = barWidth, color = "#557f2d", edgecolor = "white", label = Header_names[1], yerr = err2, capsize = 5, align = "center")
plt.bar(r3, time3, width = barWidth, color = "#2d7f5e", edgecolor = "white", label = Header_names[2], yerr = err3, capsize = 5, align = "center")
plt.xlabel("Time (hours)", fontweight = "bold")
plt.ylabel("Temperature (C)", fontweight = "bold")
plt.legend()
plt.show()
plt.savefig("Task2.png", dpi = 600)
plt.clf()

# Line chart
line, caps, bars = plt.errorbar(x, time1, yerr = err1, fmt = "rs--", linewidth = 3, elinewidth = .5, ecolor = 'k', capsize = 5, capthick = 1)
line, caps, bars = plt.errorbar(x, time2, yerr = err2, fmt = "bs--", linewidth = 3, elinewidth = .5, ecolor = 'k', capsize = 5, capthick = 1)
line, caps, bars = plt.errorbar(x, time3, yerr = err3, fmt = "gs--", linewidth = 3, elinewidth = .5, ecolor = 'k', capsize = 5, capthick = 1)
plt.title("Cities", fontsize = 18)
plt.xlabel("Time (hours)", fontsize = 12)
plt.ylabel("Temperature (C)", fontsize = 12)
plt.xticks([1,2,3,4,5,6])
plt.yticks([0,10,20,30,40,50])
plt.legend(Header_names, numpoints = 1, loc = ("upper left"))
plt.show()
plt.savefig("Task2_2.png", dpi = 600)
