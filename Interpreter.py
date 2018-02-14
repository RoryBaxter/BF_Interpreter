array = [0 for x in range(300)]

LEGAL = ["+","-",">","<",".",",","[","]"]

array_pointer = 0
code_pointer  = 0

offset = 0

depth = 0

code = input("Code to run\n")

sterile_code = ""

for letter in code:
    if letter in LEGAL:
        sterile_code += letter

while True:
    token = sterile_code[code_pointer]
    if token == "+":
        array[array_pointer] += 1
        code_pointer += 1
    elif token == "-":
        array[array_pointer] -= 1
        code_pointer += 1
    elif token == ">":
        array_pointer += 1
        code_pointer += 1
    elif token == "<":
        array_pointer -= 1
        code_pointer += 1
    elif token == ".":
        print(chr(array[array_pointer]),end="")
        code_pointer += 1
    elif token == ",":
        array[array_pointer] = ord(input())
        code_pointer += 1
    elif token == "[":
        if array[array_pointer] == 0:
            offset = 0
            depth = 1
            while True:
                offset += 1
                if sterile_code[code_pointer+offset] == "[":
                    depth += 1
                elif sterile_code[code_pointer+offset] == "]":
                    depth -= 1
                if depth == 0:
                    code_pointer += offset
                    break
        code_pointer += 1
    elif token == "]":
        offset = 0
        depth = 1
        while True:
            offset += 1
            if sterile_code[code_pointer-offset] == "]":
                depth += 1
            elif sterile_code[code_pointer-offset] == "[":
                depth -= 1
            if depth == 0:
                code_pointer -= offset
                break
    if code_pointer == len(sterile_code):
        break
