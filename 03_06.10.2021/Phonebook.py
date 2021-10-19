
def fun():
    phonebook = dict()
    number = ''
    name = ''
    while True:
        name = input()
        if name == 'q':
            break
        number = input()
        if (number == 'q'):
            break
        elif number[0]=='+' and number[1].isdigit and number[2]=="-" and number[3:6].isdigit and number[6]=='-' and number[7:10].isdigit and number[10]=='-' and number[11:13].isdigit and number[13]=='-' and number[14:] and len(number)==16:
            phonebook[name] = number
        else:
            print('Error')
    print(phonebook)

fun()