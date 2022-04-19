import os
print('Seja bem-vindo!\nAqui você poderá calcular as raizes de uma equação do 2º grau ')
while True:
        print('insira abaixo os valores solicitados.')
        a = float(input('Digite o valor do coeficiente A: '))
        if a == 0:
            input('Impossível exisitr uma equação do 2º grau onde o coeficiente A seja zero, tecle enter para continuar')
            os.system('cls')
            continue

        b = float(input('Digite o valor do coeficiente B: '))
        c = float(input('Digite o valor do coeficiente C: '))
        delta = (b**2)-4*a*c
        
        if delta < 0:
            print('Delta é negativo, portanto a equação não possui solução no conjunto dos números reais, valor do delta:',delta)
            input('Tecle enter para continuar')
            os.system('cls')
            continue
        else:
            os.system('cls')
            x1 = (-b+delta**0.5)/(2*a)
            x2 = (-b-delta**0.5)/(2*a)
            print('Solução da equação, X1 =', x1, 'e X2 =', x2,'\n\nInformações sobre o gráfico:\n')
            
            if a > 0:
                print('A parábola está voltada para cima pois o coeficiente A é positivo.')
            else:
                print('A parábola está voltada para baixo pois o coeficiente A é negativo.')
            
            if b > 0:
                print('O gráfico da função cruza o eixo Y no intervalo onde a função é crescente pois o coeficiente B é positivo.')
            elif b < 0:
                print('O gráfico da função cruza o eixo Y no intervalo onde a função é decrescente pois o coeficiente B é negativo.')
            else:
                y_vertice = -delta/(4*a)
                if a > 0:
                    print('O gráfico da função cruza o eixo Y exatamente no valor mínimo dela:', y_vertice)
                else: 
                    print('O gráfico da função cruza o eixo Y exatamente no valor máximo dela:', y_vertice)
            input(f'O valor de C corresponde ao ponto onde o gráfico cruza o eixo Y que neste caso foi {c} tecle enter para calcular outra equação.')
            os.system('cls')