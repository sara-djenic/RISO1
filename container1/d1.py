import http.client
import json

conn = http.client.HTTPSConnection("getpantry.cloud")
payload = json.dumps({
  "id": "id1234",
  "ime": "Paja",
  "prezime": "Patak",
  "smer": "IT",
  "predmeti": [
      "programiranje1",
      "programiranje2",
      "programiranje3"
  ],
  "prosek": 7.7,
  "kontakt": {
      "adresa": "Kneza Mihaila 6",
      "mesto": "Beograd",
      "telefon": "011-33-48-079"
  }

})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/apiv1/pantry/565376db-b298-4d9b-ad93-0f57a001548a/basket/domaci1", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))