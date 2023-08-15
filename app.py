#Aplicação para ler um arquivo excel e gerar um arquivo txt com os dados do excel
#Autor: Darcio Gleidson
#Data: 15/08/2023
#Versão: 1.0

import pandas as pd
import os

#Função para ler o arquivo excel
def lerArquivoExcel():
    #Lendo o arquivo excel
    df = pd.read_excel('arquivo.xlsx', sheet_name='Planilha1')
    #Retornando o dataframe
    return df

#Função para gerar o arquivo txt
def gerarArquivoTxt(df):
    #Criando o arquivo txt
    arquivo = open('arquivo.txt', 'w')
    #Percorrendo o dataframe
    for index, row in df.iterrows():
        #Escrevendo no arquivo txt
        arquivo.write(str(row['Nome']) + ' - ' + str(row['Idade']) + '\n')
    #Fechando o arquivo txt
    arquivo.close()

#Função para exibir o arquivo txt
def exibirArquivoTxt():
    #Lendo o arquivo txt
    arquivo = open('arquivo.txt', 'r')
    #Exibindo o arquivo txt
    print(arquivo.read())
    #Fechando o arquivo txt
    arquivo.close()

#Função para exibir o menu
def exibirMenu():
    #Exibindo o menu
    print('1 - Gerar arquivo txt')
    print('2 - Exibir arquivo txt')
    print('3 - Sair')
    #Lendo a opção do usuário
    opcao = int(input('Digite a opção desejada: '))
    #Retornando a opção do usuário
    return opcao

#Função principal
def main():
    #Lendo o arquivo excel
    df = lerArquivoExcel()
    #Exibindo o menu
    opcao = exibirMenu()
    #Verificando a opção do usuário
    while opcao != 3:
        #Verificando a opção do usuário
        if opcao == 1:
            #Gerando o arquivo txt
            gerarArquivoTxt(df)
        elif opcao == 2:
            #Exibindo o arquivo txt
            exibirArquivoTxt()
        else:
            #Exibindo mensagem de erro
            print('Opção inválida!')
        #Exibindo o menu
        opcao = exibirMenu()
    #Exibindo mensagem de saída
    print('Saindo...')

#Executando a função principal
main()
