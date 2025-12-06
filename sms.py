import requests 


def send_sms(phone_number,message):
    res = requests.post('https://textbelt.com/text', {
  'phone': phone_number,
  'message': message,
  'key': 'f4c111bcf51ba4ad9ab788dbad06a0427c5b7b7a8PNivj1Vvkevs3yL77VUF9jBA',
})
    print(res.headers)


if __name__ == '__main__':
    send_sms("3472475386",'Yes test message from sms.py')