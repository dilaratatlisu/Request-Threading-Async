import requests

# https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json

def get_crypto_data():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    return response.json()

crypto_response = get_crypto_data()
user_input = input("Please enter crypto name: ")

for crypto in crypto_response:
    if crypto["currency"] == user_input:
        print(crypto["price"])
        break
