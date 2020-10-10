import math
import os

class Transposicao:
    def __init__(self,chave):
        self.chave = chave

    def ler(self,nome_arq):
        arq = open(nome_arq,'r')

        msg=''
        for line in arq:
            msg+=line

        return msg
    
    def cifrar(self,msg):
        '''PRIMEIRAMENTE  REALIZA UM LIMPEZA NA MENSAGEM, TIRANDO PONTUAÇÃO E ESPAÇOS
        '''
        msg = msg.replace(" ","")
        msg = msg.replace('.','')
        msg = msg.replace(',','')
        msg = msg.replace('?','')
        msg = msg.replace('\n','')
        tam = len(msg)
        linhas = math.ceil(tam/len(self.chave))
        mat = [] 
        msg_cifrada=''
        #CRIA UMA MATRIZ COLOCANDO AS LETRAS DA MENSAGEM NAS LINHAS, QUE TEM VALOR MAXIMO IGUAL AO TAMANHO DA CHAVE
        #CASO O NUMERO DE CARACTERES NÃO SEJA IGUAL A UMA DIVISÃO EXATA PELO VALOR DA CHAVE, A MATRIZ É COMPLETADA POR 'X'
        for i in range(linhas):
            matL = []
            for j in range(len(self.chave)):
                try:
                    matL.append(msg[i*len(self.chave) + j].upper())
                except:
                    matL.append('X')
            mat.append(matL)
        #PEGA O INDEX DOS VALORES DA CHAVE EM ORDEM E ADICIONA OS CARACATERES DAS COLUNAS CORRESPONDENTE A UM VARIÁVEL QUE CONTEM A MENSAGEM CIFRADA
        for k in range(1,len(self.chave)+1):
            for j in range(linhas):
                msg_cifrada+=mat[j][self.chave.index(k)]

        return msg_cifrada

    def decifrar(self,msg):
        tam = len(msg)
        linhas = math.ceil(tam/len(self.chave))
        mat = [] 
        msg_decifrada = ''


        #CRIA UMA MATRIZ COLOCANDO AS LETRAS DA MENSAGEM CIFRADA EM COLUNAS, QUE TEM VALOR MAXIMO IGUAL AO TAMANHO DA CHAVE
        for i in range(len(self.chave)):
            matL = []
            for j in range(linhas):
                matL.append(msg[i*linhas + j])
            mat.append(matL)
        #PEGA OS VALORES DA CHAVE EM ORDEM E ADICIONA OS CARACATERES DAS LINHAS CORRESPONDENTES A UM VARIÁVEL QUE CONTEM A MENSAGEM CIFRADA
        for k in range(linhas):
            for j in self.chave:
                msg_decifrada+=mat[j-1][k]

        return msg_decifrada



#cifra = Transposicao([4,1,2,5,3,6,7])


print("DIGITE A CHAVE: (APERTE ENTER A CADA NUMERO)")
chave = []
for i in range (0,7):
    chave.append(int(input()))


cifra = Transposicao(chave)
msg = cifra.ler('claro.txt')
print("APERTE QUALQUER TECLA PARA CONTINUAR O PROCESSO DE CIFRAGEM")
escolha = input()
print("CIFRANDO")

#REALIZA A CIFRAGEM  3X
try:
    msg_cifrada = cifra.cifrar(msg)
    msg_cifrada = cifra.cifrar(msg_cifrada)
    msg_cifrada = cifra.cifrar(msg_cifrada)
    with open('cifrado.txt','w') as txt_cifrado:
        txt_cifrado.write(msg_cifrada)
    print("TEXTO CIFRADO COM SUCESSO...")

    print("APERTE QUALQUER TECLA PARA CONTINUAR O PROCESSO DE DECIFRAGEM")
    escolha =input()
    print("DECIFRANDO")
    #REALIZA A DECIFRAGEM 3X
    msg_para_decifrar = cifra.ler('cifrado.txt')
    msg_decifrada = cifra.decifrar(msg_para_decifrar)
    msg_decifrada = cifra.decifrar(msg_decifrada)
    msg_decifrada = cifra.decifrar(msg_decifrada)
    with open('decifrado.txt','w') as txt_cifrado:
        txt_cifrado.write(msg_decifrada)
    print("TEXTO DECIFRADO COM SUCESSO...")
    msg_para_decifrar=msg_decifrada
except:
    print("HÁ ALGUMA PROBLEMA NA CHAVE ESCOLHIDA")

    

