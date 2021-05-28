def split_g(list_split, division_end, division_beginning=0):
    if division_beginning == 0:
        split_one = list_split.split(division_end, 1)
        final_result = split_one.pop(0)
        return final_result
    else:
        split_one = list_split.split(division_end, 1)
        split_two = split_one[0].split(division_beginning, 1)
        final_result = split_two.pop()
        return final_result

#создал функцию, которая находит нужный мне обьект в списке

with open('ginx_logs.txt', 'r', encoding='utf-8') as file_1:
    split_list = file_1.readlines()
    final_result = []
    for line in split_list:
        split_ip = split_g(line, ' -')
        split_get = split_g(line, ' /', ' "')
        split_address = split_g(line, ' H', 'T ')
        split_tuple_ip_get_address = (split_ip, split_get, split_address)
        final_result.append(split_tuple_ip_get_address)
    for index in final_result:
        print(index)

    #создал список картежей логов и вывел их

    split_ip = [split_g(i, ' -') for i in split_list]

    #выявил ip адреса

    dictionary_ip = {i: split_ip.count(i) for i in split_ip}

    #создал словарь, в котором есть ip адреса и кол-во каждого из них

    dictionary_ip_max_namekey = max(dictionary_ip, key=dictionary_ip.get)
    dictionary_ip_max_meaning = str(dictionary_ip.get(dictionary_ip_max_namekey))
    print("IP адрес спамера: " + dictionary_ip_max_namekey + "\nКолличество запросов: " + dictionary_ip_max_meaning)

    #выявил ip адрес спамера и колличество запросов его запросов. После вывел информацию о нем

