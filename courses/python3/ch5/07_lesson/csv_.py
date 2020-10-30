import csv


with open("customers.csv", "r") as file:
    # data = csv.reader(file)
    data = [x for x in csv.DictReader(file)]

with open("customers2.csv", "w") as file:
    wrt = csv.writer(
        file,
        delimiter=",",
        quotechar='"',
        quoting="csv.QUOTE_ALL",
    )

    for d in data:
        wrt.writerow([d["first_name"], d["last_name"], d["email"], d["phone"]])
