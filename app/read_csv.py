import csv

def read_csv(path):
  with open(path,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {i:e for i, e in iterable}
      data.append(country_dict)
  return data

def country_population(data):
  population = {}
  for i in data:
    if i.values() is int == True:
      population.append(i)

  return population
  

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])

  population = country_population(data)
  print(population)