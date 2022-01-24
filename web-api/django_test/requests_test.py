import requests

TAG = "http://127.0.0.1:8000/api/v0/tag/3/"

# #response = requests.get(TAG)
# #response = requests.delete(TAG)
# auth = ('admin', '123456')
# #response = requests.delete(TAG, auth = auth)
#
# SERVER = '127.0.0.1:8000/api-token-auth/'
#
# response = requests.post(SERVER, auth = auth)
#
# print(response.status_code)
#curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'

token = '834a5446ad08f95a1c76de14e3504607d8747ed0'

headers = {'Authorization': f'Token {token}'}

response = requests.delete(TAG, headers = headers)

print(response.status_code)