#! /usr/bin/env python3
with open('input.txt') as f:
	lines = f.readlines()
f.close()

digits = ['0','1','2','3','4','5','6','7','8','9']
text_to_numeric = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

total = 0

for line in lines:
    line_total = 0
    line = line.strip()
    # forward
    f_digit = ''
    for char in line:
        if f_digit != '':
            break
        if char in digits:
            f_digit = char
            break
        elif char.isalpha():
            word = ''
            for char2 in line:
                if f_digit != '':
                    break
                if char2.isalpha():
                    word += char2
                    for num in text_to_numeric:
                        if num in word:
                            f_digit = text_to_numeric[num]
                            break
                else:
                    break

    # backwards
    b_digit = ''
    rev_line = line[::-1]
    for char in rev_line:
        if b_digit != '':
            break
        if char in digits:
            b_digit = char
            break
        elif char.isalpha():
            word = ''
            for char2 in rev_line:
                if b_digit != '':
                    break
                if char2.isalpha():
                    word += char2
                    rev_word = word[::-1]
                    for num in text_to_numeric:
                        if num in rev_word:
                            b_digit = text_to_numeric[num]
                            break
                else:
                    break


    line_total += int(f_digit + b_digit)
    total += line_total
print(total)

