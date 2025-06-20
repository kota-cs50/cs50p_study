def convert(character):
    character = character.replace(":)", "🙂")
    character = character.replace(":(", "🙁")
    return character


def main():
    character = input()
    text = convert(character)
    print(text)


main()
