from string import Template
from datetime import datetime

with open("template.html", "r") as html:
    template = Template(html.read())
    date = datetime.now().strftime("%d/%m/%Y")
    message_body = template.safe_substitute(name="Misa", date=date)


print(message_body)
