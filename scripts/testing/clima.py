import requests


token = "8a311c33033043d7651f447dea437e73"
URL = f"http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token={token}"
info = (
    "https://www.climatempo.com.br/previsao-do-tempo/cidade/2008/valparaisodegoias-go"
)
u = f"http://apiadvisor.climatempo.com.br/api/v1/climate/rain/locale/2008?token={token}"
r = requests.get(u)
print(r.text)
