''' O script obterá o texto do clipboard, adicionará um
    asterisco e um espaço no início de cada linha e, em
    seguida, colará esse novo texto no clipboard. '''

#! python3
import pyperclip

text = pyperclip.paste()

# ToDo: Separa as linhas e acrescenta asteriscos.
lines = text.split('\n')
for i in range(len(lines)):   
    lines[i] = '# resultado: ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
print(text)

# resultado: * Às folhas tantas
# resultado: * Do livro matemático
# resultado: * Um Quociente apaixonou-se
# resultado: * Um dia
# resultado: * Doidamente
# resultado: * Por uma Incógnita.
# resultado: * Olhou-a com seu olhar inumerável
# resultado: * E viu-a, do Ápice à Base.
# resultado: * Uma figura ímpar:
# resultado: * Olhos rombóides, boca trapezóide,
# resultado: * Corpo ortogonal, seios esferóides. 