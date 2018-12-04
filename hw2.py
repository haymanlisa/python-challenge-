import csv
file1 = open("budget.csv", 'r')

#budget = file1.read()
#print(type(budget))

csv_reader = csv.reader(file1)

next(csv_reader)

prev = 0
alist = []
temp_sum = 0

month = 0
total = 0



#sumofall = 0
for row in csv_reader:
    month = month + 1
  
    total = int(row[1])+ total
    
    #print(int(row[1]))
    #sumofall = sumofall + int(row[1])

    temp_sum = int(row[1]) - prev

    #temp_sum == 4030

    alist.append([row[0], temp_sum])
    #alist_m.append(row[0])

    prev = int(row[1])

my_dict = dict(alist)

var_m = ''
var_n = ''
var_max = 0
var_min = 0


for k, v in my_dict.items():
   
    if var_max < v:
        var_max = v
        var_m = k


    #prev == 4030

    if var_min > v:
        var_min = v
        var_n = k


month_list = list(my_dict.values())
skip_first = month_list[1:]
how_many_item = len(skip_first)
sum_of_all = sum(skip_first)

avg_each_month = sum_of_all / how_many_item

print("Fiancial Analysis")
print("-------------------")
print("Total Months" + " : " + str(month))
print("Total" + " : " + str(total))
print("Average Change" + " : " + str(avg_each_month))
print("Greatest Increase in Profits" + " : " + str(var_m), str(var_max))
print("Greatest Decrease in Profits" + " : " + str(var_n), str(var_min))










    







    











