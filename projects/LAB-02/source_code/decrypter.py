# Ethical Disclaimer: Este código é destinado apenas para fins educacionais.
import os
import pyaes

file_name = "TARGET"
file = open(file_name, "rb")
file_data = file.read()
file.close()

key = b"@@---->>ChavatteSecurity<<----@@"
aes = pyaes.AESModeOfOperationCTR(key)

warning_index = file_data.find(b"#!#!#")

if warning_index != -1:
    file_data = file_data[:warning_index]

decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file = "TARGET"

with open(f'{new_file}','wb') as new_file:
    new_file.write(decrypt_data)
    new_file.close()