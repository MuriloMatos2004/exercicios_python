n = 1366516580

first_byte = n & 255
seconde_byte = (n >> 8) & 255
third_byte = (n >> 16) & 255
fourth_byte = (n >> 24) & 255

print('{c4}{c3}{c2}{c1}'.format(c4 = chr(fourth_byte), c3 = chr(third_byte), c2 = chr(seconde_byte), c1 = chr(first_byte)))

