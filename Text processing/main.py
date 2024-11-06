def counting_letter(word:str) -> int:
    index = 0
    for i in word:
        if i == ' ':
            continue
        else:
            index += 1
    else:
        return f'index: {index}'


def counting_word(sentence:str) -> int:
    letter_list = sentence.split()
    for item in letter_list:
        if item.isalpha() == False:
            letter_list.remove(item)
        else:
            continue
    return f'words: {len(letter_list)}'


def counting_character(sentence:str) -> int:
        letter_list = sentence.split()
        for item in letter_list:
            if item.isalpha():
                continue
            else:
                letter_list.remove(item)
        return f'characters: {len(letter_list)}'




