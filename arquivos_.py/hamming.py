import random
import math
from itertools import combinations
xs = []
palavra_NaN = []
x = []


def combina(lista, resultado_esperado):
    aux = lista
    for i in range(2, len(aux) + 1):
        aux2 = combinations(aux, i)
        for j in aux2:
            if sum(j) == resultado_esperado:
                return list(j)
    return False


def operacao_xor(x, palavra):
    global xs
    xs = []
    new_x = []
    exp = 0
    for i in range(len(palavra)):
        if palavra[i] == 'NaN':
            for j in range(0, len(x), 2):
                if int(math.pow(2, exp)) in x[j + 1]:
                    new_x.append(x[j])
            exp += 1
            xor = ''
            aux_xs = []
            for k in range(len(new_x)):
                if k == 0:
                    xor = palavra[new_x[k] - 1]
                else:
                    if (palavra[new_x[k] - 1] == '1' and xor == '0') or (palavra[new_x[k] - 1] == '0' and xor == '1'):
                        xor = '1'
                    else:
                        xor = '0'
                aux_xs.append(new_x[k] - 1)

            palavra[i] = xor
            aux_xs.append(i)
            xs.append(aux_xs)
            aux_xs = []
            new_x = []
    return palavra


class Hamming:
    __slots__ = ['_palavra']

    def __init__(self):
        self._palavra = []

    @property
    def palavra(self):
        return self._palavra

    @palavra.setter
    def palavra(self, palavra):
        self._palavra = palavra

    def verifica(self):
        if (len(self._palavra) >= 4) and (len(self._palavra) <= 256):
            for i in self._palavra:
                if i != '0' and i != '1':
                    return False
            print("\nTamanho da palavra inserida: %d bits" % len(self._palavra))
            return True
        else:
            return False

    def gerador_aleatorio(self):
        tamanho_da_palavra = random.randint(4, 256)
        print("Tamanho da palavra gerada: %d bits" % tamanho_da_palavra)
        for i in range(tamanho_da_palavra):
            self._palavra.append(str(random.randint(0, 1)))
        print("Palavra gerada: %s" % "".join(self._palavra))
        return self._palavra

    def gerador(self):
        try:
            op = input("Voce deseja inserir a palavra(digite 1) ou que seja gerada automaticamente(digite 2)? ")
            if op == '1':
                while 1:
                    self._palavra = list(input("Insira a palavra(de 4 a 256 bits): "))
                    if self.verifica():
                        return self._palavra
                    else:
                        print("\nErro!\n")
            elif op == '2':
                self._palavra = self.gerador_aleatorio()
        except:
            print("Ocorreu um erro! Tente novamente")

    def decompoe(self):
        global x
        exp = 0
        m = []
        for cont in range(1, len(self._palavra) + 1):
            if self._palavra[cont - 1] != 'NaN':
                for i in range(1, cont + 1):
                    if i == math.pow(2, exp):
                        exp += 1
                        m.append(i)
                x.append(cont)
                x.append(combina(m, cont))
                exp = 0
                m = []
        self._palavra = operacao_xor(x, self._palavra)

    def decomposicao(self):
        global palavra_NaN
        nw_palavra = []
        cont = 1
        exp = 0
        cont_pl = 1
        while cont_pl <= len(self._palavra):
            if cont == math.pow(2, exp):
                nw_palavra.append('NaN')
                exp += 1
            else:
                nw_palavra.append(self._palavra[cont_pl - 1])
                cont_pl += 1
            cont += 1

        palavra_NaN = nw_palavra.copy()
        self._palavra = nw_palavra
        self.decompoe()

    def validacao(self):
        paridade = 0
        binario = []
        for i in range(len(xs)):
            for j in xs[i]:
                paridade += int(self._palavra[j])
            if paridade % 2 == 0:
                binario.append('0')
            else:
                binario.append('1')
            paridade = 0
        if '1' in binario:
            print("\nHouve um erro na transmissao!\n")
            exp = 0
            tot = 0
            while 1:
                tot += pow(2, exp) * int(binario[exp])
                if exp == len(binario) - 1:
                    break
                exp += 1
            tot -= 1
            print("O erro foi encontrando no bit na posicao %d" % tot)
            print("Palavra antes da correcao: ", "".join(self._palavra))
            if self._palavra[tot] == '0':
                self._palavra[tot] = '1'
            else:
                self._palavra[tot] = '0'
            print("\nO erro foi corrigido!\n")
            print("Palavra depois da correcao: ", "".join(self._palavra))
        else:
            print("Não houve erro na transmissao!\n")

    def colocando_erro(self):
        global palavra_NaN
        pos = random.randint(1, len(palavra_NaN)) - 1
        if self._palavra[pos] == '1':
            print("O erro foi colocado na posiçao %d" % pos)
            print("Palavra antes: ", "".join(self._palavra))
            self._palavra[pos] = '0'
            print("Palavra depois: ", "".join(self._palavra))
        else:
            print("\nO erro foi colocado na posiçao %d" % pos)
            print("Palavra antes: ", "".join(self._palavra))
            self._palavra[pos] = '1'
            print("Palavra depois: ", "".join(self._palavra))


