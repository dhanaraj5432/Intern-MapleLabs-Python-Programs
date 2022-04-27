country = ['India', 'Pakistan', 'Nepal']
capital = ['New Delhi', 'Islamabad','Kathmandu']
output = {country[i]:capital[i] for i in range(len(country))}
#output = dict(zip(country,capital))
print(output)
