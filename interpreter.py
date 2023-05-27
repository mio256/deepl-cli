import translate


def main():
    while True:
        text = input('> ')
        if text == 'exit':
            break
        print(translate.translate(text))


if __name__ == '__main__':
    main()
