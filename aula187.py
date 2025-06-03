# Criando arquivos com Python + Context Manager with
 # Usamos a função open para abrir
 # um arquivo em Python (ele pode ou não existir)
 # Modos:
 # r (leitura), w (escrita), x (para criação)
 # a (escreve ao final), b (binário)
 # t (modo texto), + (leitura e escrita)
 # Context manager - with (abre e fecha)
 # Métodos úteis
 # write, read (escrever e ler)
 # writelines (escrever várias linhas)
 # seek (move o cursor)
 # readline (ler linha)
 # readlines (ler linhas)
 # Vamos falar mais sobre o módulo os, mas:
 # os.remove ou unlink - apaga o arquivo
 # os.rename - troca o nome ou move o arquivo
 # Vamos falar mais sobre o módulo json, mas:
 # json.dump = Gera um arquivo json
 # json.load

caminho_arquivo = 'aula187.txt'
 
# Abrir e fechar o arquivo:
 
 # arquivo = open(caminho_arquivo, 'w')
 # #
 # arquivo.close()

# Com o context manager ele abre e fecha o arquivo.
with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
     arquivo.write('Linha 1\r\n')
     arquivo.write('Linha 2\n')
     arquivo.write('Atenção')

     