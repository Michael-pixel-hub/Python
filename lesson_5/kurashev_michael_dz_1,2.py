#с использование yield
def odd_number_generator(last_namber):
    for element in range(1, last_namber+1, 2):
        yield element

list_final = odd_number_generator(13)
print(*list_final)

#без использования yield
generation_number = 13
final_list = (i for i in range(1, generation_number + 1, 2))
print(*final_list)