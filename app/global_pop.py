import read_csv
import charts

def run():
  data = read_csv.read_csv('./app/data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))
  labels = [i['Country/Territory'] for i in data]
  values = [i['World Population Percentage'] for i in data]
  charts.generate_pie_chart(labels, values)

if __name__ == '__main__':
  run()