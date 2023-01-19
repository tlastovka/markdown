global rows
global str_element
str_element = ""
ordered_directory = []
unordered_directory = []

def plain():
    return input("- Text: ")


def bold():
    return f"**{input('- Text: ')}**"


def italic():
    return f"*{input('- Text: ')}*"


def inline_code():
    return f"`{input('- Text: ')}`"


def link():
    label = input("- Label: ")
    url = input("- URL: ")

    return f"[{label}]({url})"


def header():
    while True:
        level = int(input("- Level: "))
        if level < 1 or level > 6:
            print("The level should be within the range of 1 to 6")
            continue
        else:
            break

    text = input("- Text: ")

    return f"{'#' * level} {text}\n"


def line_break():
    return '\n'


def list():
    number_of_rows()
    global rows
    global str_element
    global ordered_directory
    global unordered_directory

    # lines of input
    lines = [x for x in range(1, rows+1)]

    # create lines of inputs
    key = [f"Row #{line}: " for line in lines]

    # create corresponding values
    value = []
    for i in range(0, rows):
        value.append(input(f"{key[i]}"))
        ordered_directory.append(f"{i+1}. {value[i]}")
        unordered_directory.append(f"* {value[i]}")

    # create ordered and unordered list
    if formatter == "ordered-list":
        for x in range(rows):
            str_element += f"{ordered_directory[x]}\n"
        return str_element

    if formatter == "unordered-list":
        for x in range(rows):
            str_element += f"{unordered_directory[x]}\n"
        return str_element


def number_of_rows():
    global rows
    rows = int(input("Number of rows: "))
    while rows < 1:
        print("The number of rows should be greater than zero")
        rows = int(input("Number of rows:"))
    return rows # this does not add up


formatters = {"plain": plain, "bold": bold, "italic": italic, "inline-code": inline_code, "link": link,
              "header": header, "new-line": line_break, 'line-break': line_break, 'ordered-list': list,
              'unordered-list': list}

markdown_string = ""
while True:
    formatter = input("- Choose a formatter: ")
    if formatter == '!help':
        print("Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break\n"
              "Special Commands: !help !done")
        continue
    elif formatter == '!done':
        file = open('output.md', "w", encoding='utf-8')
        file.write(markdown_string)
        file.close()
        break
    elif formatter in formatters.keys():
        markdown_string += str(formatters[formatter]())
        print(markdown_string)
    else:
        print("Unknown formatter or command. Please try again")
