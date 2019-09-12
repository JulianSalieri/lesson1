number  = [3,5,7,9,10.5]
print(number)


number.append('Python')
print(len(number))

print(number[0])
print(number[-1])
print(number[2:5])
del number[-1]

temper_city= {'city': 'Москва', 'temperature': '20'}
print(temper_city[city])

print(temper_city.get('country'))

print(temper_city.get('country', 'Россия'))

temper_city['date']='27.05.2019'
print(len(temper_city))