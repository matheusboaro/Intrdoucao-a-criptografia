import random
from string import ascii_lowercase

class Enigma:
    def __init__(self):
        self.alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.giro1 = 0
        self.giro2 = 0
        self.giro3 = 0
        self.alphaOut=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.cilindro = []
        self.count=0

    def ler(self,nome_arq):
        arq = open(nome_arq,'r')

        msg=''
        for line in arq:
            msg+=line

        return msg

    #Gira o cilindro para frente
    def moverPraFrente(self, cil,giro):
        for i in range(giro):
            cil = cil[-1:] + cil[:-1]
        return cil

    #Gira o cilindro para trás
    #- Utilizado pelo alfabeto
    def moverPraTras(self, dic):
        dic = dic[1: ] + dic[:1]
        return dic

    #Realiza a cifragem da mensagem
    def cifrar(self,msg):
        encripted =''
        # Primeiramente retira algumas pontuações básicas assim com quebras de textos
        msg = msg.replace(" ","")
        msg = msg.replace('.','')
        msg = msg.replace(',','')
        msg = msg.replace('?','')
        msg = msg.replace('\n','')
        msg = msg.replace('-','')
        for l in msg.upper():
            if l not in self.alpha:
                break
            
            #Primeiramente calcula a posição em que o primeiro cilindro esta em relação a quantidade de giros
            #  em relação a letra a ser cifrada

            aux_letter = self.moverPraFrente(self.cilindro[0],self.giro1).index(self.alpha.index(l))

            #Atualiza o valor da posição em que a letra a ser cifrada esta em relação ao cilindro dois
            if aux_letter-self.giro2 <0:
                aux_letter = len(self.alpha) - self.giro2 + aux_letter
            else:
                aux_letter -=  self.giro2

            #Utiliza a posição atualizada da letra para realizar a busca no cilindro dois em relação a quantidade de giros

            aux_letter = self.moverPraFrente(self.cilindro[1],self.giro2).index(aux_letter)
            
            #Atualiza o valor da posição em que a letra a ser cifrada esta em relação ao cilindro três
            if aux_letter-self.giro3 <0:
                aux_letter = len(self.alpha) - self.giro3 +aux_letter
            else:
                aux_letter -=  self.giro3

            #Utiliza a posição atualizada da letra para realizar a busca no cilindro três em relação a quantidade de giros
            aux_letter = self.moverPraFrente(self.cilindro[2],self.giro3).index(aux_letter)

            #Realiza o giro no cilindro
            self.giro1 += 1
            #Caso o primeiro cilindro tenha chegado ao final, reseta o cilindro 1 e gira o cilindro 2
            if self.giro1 % len(self.alpha) == 0:
                self.giro2 += 1
                self.giro1 = 0
            #Caso o primeiro e o segundo cilindro tenham chegado ao final, reseta o cilindro 1 e cilindro 2 gira o cilindro 3
            if self.giro2 % len(self.alpha) == 0 and self.giro1 % len(self.alpha) == 0 and self.giro2 >= len(self.alpha) - 1:
                self.giro3 += 1
                self.giro2 = 0
            self.alpha=self.moverPraTras(self.alpha)
            #Olha no dicionario de saída o valor na posição correspondente 
            encripted+=self.alphaOut[aux_letter]

        return encripted

    #Faz o processo inverso ao de cifragem
    def decifrar(self, msg):

        decripted = ""

        for letter in msg.upper():
            #Procura o index da letra no alphabeto de saída e busca no cilindro 3
            aux_letter = self.moverPraFrente(self.cilindro[2],self.giro3)[self.alphaOut.index(letter)]

            #Atualiza o valor da posição em que a letra a ser cifrada esta em relação ao cilindro três
            aux_letter =  (aux_letter + self.giro3)%len(self.alpha)
            
            #Procura a letra correspondente na posição atualizada no cilindro 2
            aux_letter = self.moverPraFrente(self.cilindro[1],self.giro2)[aux_letter]
            
            #Atualiza o valor da posição em que a letra a ser cifrada esta em relação ao cilindro 2
            aux_letter =  (aux_letter + self.giro2)%len(self.alpha)

            #Procura a letra correspondente na posição atualizada no cilindro 1
            aux_letter = self.moverPraFrente(self.cilindro[0],self.giro1)[aux_letter]

            #Procura no alfabeto correspondente de entrada a letra na posição dada
            decripted+=self.alpha[aux_letter]
            #Realiza o giro no cilindro
            self.giro1 += 1
            #Caso o primeiro cilindro tenha chegado ao final, reseta o cilindro 1 e gira o cilindro 2
            if self.giro1 % len(self.alpha) == 0:
                self.giro2 += 1
                self.giro1 = 0
            #Caso o primeiro e o segundo cilindro tenham chegado ao final, reseta o cilindro 1 e cilindro 2 gira o cilindro 3
            
            if self.giro2 % len(self.alpha) == 0 and self.giro1 % len(self.alpha) == 0 and self.giro2 >= len(self.alpha) - 1:
                self.giro3 += 1
                self.giro2 = 0
            #Olha no dicionario de saída o valor na posição correspondente 
            self.alpha=self.moverPraTras(self.alpha)
            


        
        return decripted
    
m = Enigma()
m.cilindro.append([3,6,22,0,1,7,13,11,20,2,4,16,18,25,5,10,8,21,23,9,12,17,14,19,15,24])
m.cilindro.append([17,6,5,1,23,4,22,9,11,13,14,24,12,2,20,18,3,15,19,10,7,21,0,8,16,25])
m.cilindro.append([14,18,3,5,4,10,24,13,11,20,17,12,6,22,2,19,1,7,16,0,21,8,25,9,15,23])

msg = m.ler('claro.txt')
print("APERTE QUALQUER TECLA PARA CONTINUAR O PROCESSO DE CIFRAGEM")
escolha = input()
print("CIFRANDO...")
msg_cifrada = m.cifrar(msg)

with open('cifrado.txt','w') as txt_cifrado:
    txt_cifrado.write(msg_cifrada)
print("TEXTO CIFRADO COM SUCESSO!")

print("APERTE QUALQUER TECLA PARA CONTINUAR O PROCESSO DE DECIFRAGEM")
escolha =input()
print("DECIFRANDO...")
m2 = Enigma()
m2.cilindro.append([3,6,22,0,1,7,13,11,20,2,4,16,18,25,5,10,8,21,23,9,12,17,14,19,15,24])
m2.cilindro.append([17,6,5,1,23,4,22,9,11,13,14,24,12,2,20,18,3,15,19,10,7,21,0,8,16,25])
m2.cilindro.append([14,18,3,5,4,10,24,13,11,20,17,12,6,22,2,19,1,7,16,0,21,8,25,9,15,23])

msg2 = m2.ler('cifrado.txt')
msg_decifrada = m2.decifrar(msg2)
with open('decifrado.txt','w') as txt_cifrado:
    txt_cifrado.write(msg_decifrada)
print("TEXTO DECIFRADO COM SUCESSO!")