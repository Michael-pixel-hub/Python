import re

def email_parse(email_address):
    proverk = r'.+@.+'
    em = re.findall(proverk, email_address)
    if not em:
        raise ValueError
    pattern_name = r'[a-zA-Z0-9/.]+(?=@)'
    pattern_email = r'[a-z]+\.[a-z]+'
    vocabulary = {}
    result_name = re.findall(pattern_name, email_address)
    result_email = re.findall(pattern_email, email_address)
    for i in range(len(result_name)):
        vocabulary[result_name[i]] = result_email[i]
    print(vocabulary)

email_parse("kurashevmichael@gmail.com")