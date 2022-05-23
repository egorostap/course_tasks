import requests
datas = {
    'email':'def',
    'password':'def'
}

login = input('Enter email: ')
psswrd = input('Enter pass: ')

datas['email'] = login
datas['password'] = psswrd
url = 'https://vktarget.ru/login'
s = requests.Session()
loging = s.post(url, data = datas)
with open('result.txt', 'w') as f:
    f.write(loging.text)
