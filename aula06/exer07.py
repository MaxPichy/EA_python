import pandas as p

tempos = [100, 105, 110, 102, 108, 115, 120, 103, 107, 500]
serie = p.Series(tempos)

ma = serie.sum() / len(tempos)
me = serie.median()
a = serie.max() - serie.min()
vp = serie.var(ddof=0)
dp = serie.std(ddof=0)

qtd = int(input('Quantidade de vezes para repetir o loop: '))
i = 0

while(i < qtd):
    menu = int(input('Digite um valor para obter os resultados: \n1. Média Aritmética\n2. Mediana\n3. Amplitude\n4. Variância\n5. Desvio Padrão\n6. Sair\n'))

    match menu:
        case 1:
            print(f'Média Aritmética: {ma:.2f}')

        case 2:
            print(f'Mediana: {me:.2f}')

        case 3:
            print(f'Amplitude: {a:.2f}')

        case 4:
            print(f'Variância Populacional: {vp:.2f}')

        case 5:
            print(f'Desvio Padrão Populacional: {dp:.2f}')

        case 6:
            break

        case default:
            print('Entrada Inválida.')
    i += 1