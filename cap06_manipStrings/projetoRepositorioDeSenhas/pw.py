''' Projeto: Repositório de senhas.
    -> Este é um programa de gerenciamento de senhas não seguro. 
       Porém eferece uma demonstração básica de como esses programas funcionam.
    -> Livro: Automatize tarefas maçantes com Python - AL Sweigart (pag 180).
    -> Aluno: João Pedro M. Riuto'''

#! python 3
import sys, pyperclip

PASSWORDS = {'email':   '3nqPEaMZNF7tvnv',
             'blog':    'G1R12yH2DuX7nii',
             'lugagge': '12345'}


#Verifica se o usuário informou o parâmetro com o nome da conta.
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password.')
    sys.exit()

account = sys.argv[1] # O primeiro argumento da linha de comando é o nome da conta.

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard. Enjoy!')
else:
    print('There is no account named ' + account)