



acesso = input('Deseja acessar o sistema? s/n --')

while acesso == 's': 
                nome = input('Nome Aluno >> ') #variavel
                #snake_case
                nota_1 = float(input('nota 1>> '))
                nota_2 = float(input('nota 2>> '))
                nota_3 = float(input('nota 3>> '))

                lista = []
                lista.append(nota_1)
                lista.append(nota_2)
                lista.append(nota_3)

                média = sum(lista)/len(lista)

                print('O aluno(a)', nome, 'possui a média', média)


                if média >= 7:
                    print(f"O {nome} Passou de Ano")
                elif média >= 5 and média < 7:
                    print(f'O {nome} Está de Recuperação')
                else:
                    print(f'O {nome} Não Passou de Ano...')
                acesso = input('Deseja o continuar? s/n >> ')

print('Até logo...')
input('clique ENTER  spara sair...')   

