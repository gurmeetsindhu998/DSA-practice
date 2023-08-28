import csv
data= []
with open('example.csv', newline='') as csvfile:  #read csv file with name example.csv 
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        formate = '"'+row[0]+'"'
        data.append(formate)
    data= data[1:]
    data = ",".join(data)
    data+="."

##  creating and writing to file output.txt in the same forlder
with open('output.txt', 'w') as f:
    f.write("%s\n" % data)