# small program to change a sentence to camel case.


def display_banner(msg):
    # Display program name in a banner

    stars = '*' * len(msg)
    banner = ("\n" + stars + "\n" + msg + "\n" + stars + "\n")
    return banner


def instructions(msg):
    message = (msg + "\n")
    return message


def convert(msg):
    formatting = msg.split()
    formatted_string = formatting[0]

    for i in range(len(formatting)):
        if i > 0:
            formatted_string += (formatting[i]).capitalize()
    return formatted_string


def main():
    print(display_banner('AWESOME camelCaseGenerator PROGRAM'))
    # print(instructions('please enter a sentence to convert to camelCase.'))

    preformat = input(instructions('please enter a sentence to convert to camelCase:'))

    print(convert(preformat))


if __name__ == '__main__':
    main()
