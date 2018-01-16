# small program to change a sentence to camel case.


def display_banner():
    '''Display program name in a banner'''
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n',  stars, '\n')


def main():
    display_banner()

    preformat = input("type a sentence to format ")
    formatting = preformat.split()
    formattedString = formatting[0]

    for i in range(len(formatting)):
        if i > 0:
            formattedString += (formatting[i]).capitalize()
    print(formattedString)

if __name__ == '__main__':
    main()
