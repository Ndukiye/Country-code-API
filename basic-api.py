import requests
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("API_KEY")
user_input = ""
def get_rate(code):
    response = requests.get(f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{code}')
    if check_response(response):
        code_dic = response.json()["conversion_rates"]
        code_list = list(code_dic.items())
        for item in code_list: print(f'1 {code} = {item[1]} {item[0]}')

def get_codes():
    response = requests.get(f'https://v6.exchangerate-api.com/v6/{api_key}/codes')
    code_list = response.json()["supported_codes"]
    for code in code_list: print(f'{code[0]} - {code[1]}')
        

def convert(code_1, code_2, amount):
    response = requests.get(f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{code_1}/{code_2}/{amount}')
    if check_response(response):
        result = response.json()["conversion_result"]
        print(f'{amount} {code_1} is {result} {code_2}')

def check_response(response):
    if response.json()["result"] == "error":
        print(f'Error: {response.json()["error-type"]}')
        return False
    else:
        return True


while True:
    user_input = input("\nGet Rate - 1\nConversion - 2\nSee all currency codes - 3\nQuit - 4\n")
    match user_input:
        case "1":
            code = input("Enter Currency code: ").upper()
            get_rate(code)
        case "2":
            amount = int(input("Enter amount: "))
            code_1 = input("Enter base currency: ").upper()
            code_2 = input("Enter currency to convert to: ").upper()
            convert(code_1,code_2,amount)
        case "3":
            get_codes()
        case "4":
            break   