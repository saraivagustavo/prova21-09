'''Faça um programa, em Python 3.x, que leia um valor inteiro entre 1000 (MIL) e 9999 (NOVE MIL NOVECENTOS E NOVENTA E NOVE) (inclusive os dois valores)  e, utilizando apensa recursos  matemáticos (DIV:  % e MOD: //) que já aprendemos em sala de aula, inverta esse número, entregando um valor inteiro como resposta (NÃO É PERMITIDO UTILIZAR QUALQUER RECURSO DE STRING OU MÉTODO/FUNÇÃO NÃO APRENDIDOS E USADOS NA DISCIPLINA, EM CASO DE USO, A QUESTÃO TERÁ NOTA ZERO). Ao final, o programa deverá verificar se o valor digitado é uma CAPICUA, imprimindo a informação conforme os casos de teste.

CAPICUA: sequência de algarismos que permanece a mesma se lida na ordem direta ou inversa (p.ex., 13231).'''

def main():
    #declaração de variáveis
    numero = int(0)

    #entrada de dados
    numero = int(input())

    #processamento
    unidade = numero % 100
    print(unidade)
    resto = numero // 100
    print(resto)
    dezena = resto % 10
    print(dezena)
    milhar = numero // 1000
    print(milhar)
    return 0

if __name__ == "__main__":
    main()