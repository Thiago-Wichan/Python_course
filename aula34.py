# if / elif / else

entrada = input ('Você deseja entrar ou sair? ')


if entrada == 'entrar' :    # if pode ficar sozinho
    print('Você entrou no sistema')

elif entrada == 'sair' :    #elif depende do if
    confirmacao = input('Você realmente deseja sair do sistema? ')
    if confirmacao == "sim":
        print('Você saiu do sistema')
    elif confirmacao == "não" :
        print('Você permanece no sistema')    

else: print('Digite "entrar" ou "sair"')   #será a última opção


 