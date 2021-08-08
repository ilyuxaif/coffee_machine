coffeeTypes: list = ['americano', 'espresso', 'cappuccino', 'latte']
sizes: list = ['small', 'medium', 'large']

manifest: list = [
	{
		'model': 'model-x',
		'coffeeTypes': [coffeeTypes[0], coffeeTypes[2], coffeeTypes[3]],
		'sizes': [sizes[0], sizes[1]]
	},
	{
		'model': 'model-z',
		'coffeeTypes': [coffeeTypes[1], coffeeTypes[2], coffeeTypes[3]],
		'sizes': [sizes[1], sizes[2]]
	},
	{
		'model': 'model-y',
		'coffeeTypes': [coffeeTypes[0], coffeeTypes[1], coffeeTypes[2], coffeeTypes[3]],
		'sizes': [sizes[0], sizes[1], sizes[2]]
	}
]

