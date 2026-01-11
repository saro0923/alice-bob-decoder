
code_to_letter = {
    "._": "A", "_...": "B", "_._.": "C", "_..": "D", ".": "E",
    ".._.": "F", "__.": "G", "....": "H", "..": "I", ".___": "J",
    "_._": "K", "._..": "L", "__": "M", "_.": "N", "___": "O",
    ".__.": "P", "__._": "Q", "._.": "R", "...": "S", "_": "T",
    ".._": "U", "..._": "V", ".__": "W", "_.._": "X", "_.__": "Y",
    "__..": "Z"
}
encrypted_message = input().strip()
results = []

def decode(index, current_word):
    if index == len(encrypted_message):
        results.append(current_word)
        return

    for code in code_to_letter:
        if encrypted_message.startswith(code, index):
            decode(index + len(code), current_word + code_to_letter[code])

decode(0, "")
results.sort()
for word in results:
    print(word)

