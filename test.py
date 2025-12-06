import requests

resp = requests.post('https://textbelt.com/text', {
  'phone': '3472475386',
  'message': 'Hello world',
  'key': 'f4c111bcf51ba4ad9ab788dbad06a0427c5b7b7a8PNivj1Vvkevs3yL77VUF9jBA',
})
print(resp.json())