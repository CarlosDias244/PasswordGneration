import random

def generation():
    palavra = True
    while palavra:
        letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numeros = '0123456789'
        caracter = '!@#$%¨&*()_+-='
        tudo = letras + numeros + caracter
        senha = ''
        ussuario = input('Quantos caracteres deseja em sua senha [08-50]:')
        if not ussuario.isdigit():
            print('seloko num compensa')
            continue
        ussuario = int(ussuario)
        if ussuario> 50 or ussuario< 8:
                print('seloko num compensa')
                continue
        elif ussuario<= 50 or ussuario>= 8:
            for _ in range(ussuario):
                senha+= random.choice(tudo)
            print(f'A senha gerada foi: {senha}')
            continuar = int(input('Deseja recriar sua senha?\n[1] Sim\n[2] Não\n>>>'))
            if continuar == 1:
                 continue
            elif continuar == 2:
                 palavra = False
       

generation()