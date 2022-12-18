if __name__ == "__main__":
    string = input()
    whitespace = uppercase = lowercase = symbols = 0
    for char in string:

        if ord('A') <= ord(char) <= ord('Z'):
            uppercase += 1
        elif  ord('a') <= ord(char) <= ord('z'):
            lowercase += 1
        elif char == "_":
            whitespace += 1
        else:
            symbols += 1
        length = len(string)
    print(whitespace/length)
    print(lowercase/length)
    print(uppercase/length)
    print(symbols/length)