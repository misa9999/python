from sales.format.price import dollar


def increase(value, percentage, format=False):
	r = value + (value * percentage / 100)

	if format:
		return dollar(r)
	return r

def reduction(value, percentage, format=False):
	r = value - (value * percentage / 100)
	
	if format:
		return dollar(r)
	return r