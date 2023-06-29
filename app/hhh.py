import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(./data.csv,'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      cost = []
      for row in reader:
         cost.append(row[1])
         
   total = sum(int(cost))
   return total

response = read_csv('./data.csv')
print(response)