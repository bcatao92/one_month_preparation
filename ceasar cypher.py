string = 'middle-Outz'
k = 2
aux = ""
for char in string:
    dummy = ord(char)
    if char == "'" or char == '-':
        aux+=char
    else:
        if char.isupper():
            if dummy >= 65 and dummy < 90:
                aux += str(chr((dummy + k) % 90))
        else:
            aux += str(chr((dummy + k) % 122))
print(aux)
