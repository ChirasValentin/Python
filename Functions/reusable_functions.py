def emoji(symbols):
    emojis = {
        ":)": "😂",
        ":(": "😔",
        "<3": "❤"
    }
    return emojis.get(symbols,symbols)


def print_emoji(message):
    words = message.split(' ')
    output = ""
    for word in words:
        output += emoji(word) + ' '
    return output


message = input(">")
print(print_emoji(message))
