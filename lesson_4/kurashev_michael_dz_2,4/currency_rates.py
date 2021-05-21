import requests


def page_text(url):
    response = requests.get(url)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    return content


def division_string_list(split_list, split_string, index):
    list_one = []
    for i in split_list:
        i = i.split(split_string)
        del i[index]
        list_one.append(i[0])
    return list_one

def currency_rates(course):
    vocabulary = {}

    page = page_text("http://www.cbr.ru/scripts/XML_daily.asp")

    list_valute_one = page.split("<CharCode>")
    del list_valute_one[0]

    list_valute_two = division_string_list(list_valute_one, "</CharCode>", 1)

    list_convert_one = page.split("<Value>")
    del list_convert_one[0]

    list_convert_two = division_string_list(list_convert_one, "</Value>", 1)

    a = 0

    for i in list_valute_two:
        vocabulary[i] = list_convert_two[a]
        a = a + 1

    return vocabulary[course]

if __name__ == "__main__":
    print(currency_rates("XDR"))



# list_b = division_string_list(list_a, "<CharCode>", 0) #создаем обрезанный список 1
# print(list_b)

# list_c = division_string_list(list_b, "</CharCode>", 1) #создаем обрезанный список 2 и получаем валюту
# print(list_c)
