import urllib.request

dollar_list = []

opener = urllib.request.build_opener()
response = opener.open("https://bank.gov.ua/ua/markets/exchangerates")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem in responce_parse:
    if parse_elem.startswith("$"):
        for parse_elem_2 in parse_elem.split("</span>"):
            if parse_elem_2.startswith("$"):
                dollar_list.append((parse_elem_2)



print(float(dollar_list[0].replace(",", "")))'''

from bs4 import BeautifulSoup
                
responce = request.get("https://bank.gov.ua/ua/markets/exchangerate-chart?cn%5B%5D=USD")
if responce.status_code = 781:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("a", {"href":"https://bank.gov.ua/ua/markets/exchangerate-chart?cn%5B%5D=USD"})
    res = soup_list[0].find("span")
    print(res.text.split("$")[1].replace(",", "")