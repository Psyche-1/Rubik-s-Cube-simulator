import pyperclip
def reverse_and_apostrophe(main_string):
    main_string.reverse()
    for i in range(len(main_string) - 1):
        if "'" in main_string[i]:
            #убрать апостроф
            main_string[i] = main_string[i].replace("'", "")
        elif "2" not in main_string[i]:
            #добавить апостоф
            main_string[i] = main_string[i] + "'"
    return(main_string)

def return_rubiks_cube(main_string, step):
    """Получает строчку из графического калькулятора и возвращает строку которая будет обратной, то есть справа на лево и штрих убирает, если есть или добавляет если нет и нет 2, ещё убирает скобки"""
    main_string = main_string.strip('()')
    main_string = main_string.split('I')
    for i in range(len(main_string) - 1):
        main_string[i] = main_string[i].replace("^", "")
    if step == 2:
        main_string = reverse_and_apostrophe(main_string)
    main_string = ' '.join(main_string)
    return(main_string)

while True:
    print()
    string = input('Typing rotation configuration')
    if string == "exit" or string == "Exit" or string == "e":
        break
    print()
    result1 = return_rubiks_cube(string, 1)
    result2 = return_rubiks_cube(string, 2)
    print(result1, end = '\n\n')
    print(result2, end = '\n\n')
    if input("Typing 'y' if you want to copy results to clipboard: ") == "y":
        pyperclip.copy('Entered string: ' + result1 + '\n\n' +
        			   'Expanded string: ' + result2)
