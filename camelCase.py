# small program to change a sentence to camel case.


def main():
    preformat = input("type a sentence to format ")
    formatting = preformat.split()
    formattedString = formatting[0]

    for i in range(len(formatting)):
        if i > 0:
            formattedString += (formatting[i]).capitalize()
    print(formattedString)

if __name__ == '__main__':
    main()
