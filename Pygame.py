import random #Import random, é utilizado para gerar Sequências Aleatórias.
import time #Import time, é utilizado para atrasar aos funções

def geraVetor(C,n): #Gera uma sequência de acordo com os critirios já estabelecidos.
    if C==1:
        vetor=[]
        N1=1
        for i in range(n):
            vetor.append(N1)
            N1+=1
    elif C==2:
        vetor=[]
        N1=n
        for i in range(n):
            vetor.append(N1)
            N1-=1


    elif C==3:
        vetor= []
        for i in range(n):
            N1=random.randint(1,125)
            vetor.append(N1)

    return vetor
def BubbleSort(V,n,div1,div2,T,XS): #Organiza em Bubble Sort
    for i in range(len(V)):
        for j in range(i+1,n):
            if V[i]>V[j]:
                N1=V[i]
                V[i]=V[j]
                V[j]=N1
                time.sleep(T) #Atrasa a função
                Pygame(V,n,i,j,div1,div2,1,XS) #Desenha a imagem, repetidas vezes para gerar uma animação
    return V

def SelectionSort(V,n,div1,div2,T,XS):#Organiza em Selection Sort
    for i in range(len(V)-1):
        min=i
        for j in range(i+1,len(V)):
            if V[min]>V[j]:
                min= j
        if min !=1:
            N1=V[i]
            V[i]=V[min]
            V[min]=N1
            time.sleep(T) #Atrasa a função
            Pygame(V,n,i,min,div1,div2,2,XS) #Desenha a imagem, repetidas vezes para gerar uma animação
    return V


def InsertionSort(V,n,div1,div2,T,XS): #Organiza em Insertion Sort
    for i in range(1,len(V)):
        x=V[i]
        j=i-1
        while j>=0 and x<V[j]:
            V[j+1]=V[j]
            j-=1
        V[j+1]=x
        time.sleep(T) #Atrasa a função
        Pygame(V,n,i,j,div1,div2,3,XS) #Desenha a imagem, repetidas vezes para gerar uma animação
    return V


import pygame
from pygame import mixer
import math

def QuickSort(Lista,Inicio,Fim,div1,div2,T,XS): #Organiza em Quick Sort
    if Inicio<Fim:
        Pivo=Partition(Lista,Inicio,Fim,div1,div2,T,XS)
        QuickSort(Lista,Inicio,Pivo-1,div1,div2,T,XS)
        QuickSort(Lista,Pivo+1,Fim,div1,div2,T,XS)
        

def Partition(Lista,Inicio,Fim,div1,div2,T,XS):
    Pivo= Lista[Fim]
    i=Inicio
    for j in range(Inicio,Fim):
        if Lista[j]<=Pivo:
            Lista[j],Lista[i]=Lista[i],Lista[j]
            i+=1
    Lista[i],Lista[Fim]=Lista[Fim],Lista[i]
    time.sleep(T) #Atrasa a função
    Pygame(Lista,Fim,i,j,div1,div2,4,XS) #Desenha a imagem, repetidas vezes para gerar uma animação
    return i

def Merge(lista, inicio, meio, fim,div1,div2,T,XS): 
    esquerda = lista[inicio:meio] 
    direita = lista[meio:fim]
    top_e,top_d = 0, 0
    for k in range(inicio, fim): 
        if top_e >= len(esquerda): 
            lista[k] = direita[top_d]
            top_d+=1
        elif top_d >= len(direita): 
            lista[k] = esquerda[top_e]
            top_e+=1
        elif esquerda[top_e] < direita[top_d]: 
            lista[k] = esquerda[top_e]
            top_e+=1
        else:
            lista[k] = direita[top_d]
            top_d+=1
        time.sleep(T) #Atrasa a função
        Pygame(lista,fim,meio,k,div1,div2,5,XS) #Desenha a imagem, repetidas vezes para gerar uma animação
        
def MergeSort(lista, inicio, fim,div1,div2,T,XS): #Organiza em Merge Sort   
    if (fim-inicio) > 1:                
        meio=(inicio + fim)//2 
        MergeSort(lista, inicio, meio,div1,div2,T,XS) 
        MergeSort(lista, meio, fim,div1,div2,T,XS) 
        Merge(lista, inicio, meio, fim,div1,div2,T,XS)

def Songs(i): # Coloca para tocar uma música de Acordo com os diferentes momentos ou funções
    from pygame import mixer
    if i==0:
        mixer.init()
        mixer.music.load("smw_coin.mp3")
        mixer.music.set_volume(0.7)  
        mixer.music.play()
    elif i==1:
        mixer.init()
        mixer.music.load("Algoritmo.mp3")
        mixer.music.set_volume(1)  
        mixer.music.play()
    elif i==2:
        mixer.init()
        mixer.music.load("smw_1-up.mp3")
        mixer.music.set_volume(1)  
        mixer.music.play()
    elif i==3:
        mixer.init()
        mixer.music.load("smw_course_clear-_1_.mp3")
        mixer.music.set_volume(1)  
        mixer.music.play()

        
def Pygame(V,n,i,j,div1,div2,K,XS): #Gera o desenho, utilizando os critérios, respectivamente :Sequência,tamanho da Sequência, posição i e j (para determinar as barras vermelha e amarela da animação), div1 e div2(para determinar a proporção da largura e altura)
    # K para determinar qual é o tipo de organização, XS para determinar se tiver som ou não.
    pygame.init() # Inicia o pygame
    screen= pygame.display.set_mode((1100,800),5,0)# define a tela e tamanho da tela
    pygame.display.set_caption("VISUALIZAÇÃO GRAFICA DOS ALGORITMOS DE ORDENAÇÃO") # define nome do programa pygame
    screen.fill((255,255,255)) # define o fundo da tela para branco
    
    #Cores
    preto=(0,0,0)
    sombra=(18,27,32)
    branco=(255,255,255)
    vermelho=(255,0,0)
    verde=(0,255,0)
    azul=(0,0,255)
    amarelo=(255,255,0)
    ciano=(0,255,255)
    magenta=(255,0,255)
    
    if XS==True: # coloca o som caso XS seja TRUE
        Songs(0)
        
    # a seguir vem muitas contas para determinar a proporção da largura e tamanho das barras
    div1+=40
    N1=40
    Sub=div1-N1
    # varias contas para determinar qual barra è a barra amarela (Comparação), e vermelha(Troca)
    NI1=40+(Sub*i)
    NI2=480-(V[i]*div2)
    divI=NI1+Sub
    NJ1=40+(Sub*j)
    NJ2=480-(V[j]*div2)
    divJ=NJ1+Sub
    PgTxt(screen,K) # escreve na tela de acordo com qual tipo de organização foi determinada
    for a in range (len(V)): # desenha a animação
        N2=480-(V[a]*div2)
        pygame.draw.polygon(screen,ciano,([N1,N2],[N1,540],[div1,540],[div1,N2]))
        pygame.draw.polygon(screen,preto,([N1,N2],[N1,539],[div1,539],[div1,N2]),3)
        pygame.draw.rect(screen,preto,(40,40,500,500),3)
        N1=div1
        div1+=Sub
    pygame.draw.polygon(screen,amarelo,([NI1,NI2],[NI1,539],[divI,539],[divI,NI2]),3)
    pygame.draw.polygon(screen,vermelho,([NJ1,NJ2],[NJ1,539],[divJ,539],[divJ,NJ2]),3)
    pygame.display.flip()


    
def Finish(V,n,div1,div2,XT,XC,XS,vet,Tempo): # finaliza a organização e desenha na tela
    # codigo padrão para inicar o pygame
    pygame.init()
    screen= pygame.display.set_mode((800,800),5,0)
    pygame.display.set_caption(" Ordenação Finalizado")
    screen.fill((255,255,255))
    
    #Cores
    preto=(0,0,0)
    sombra=(18,27,32)
    branco=(255,255,255)
    vermelho=(255,0,0)
    verde=(0,255,0)
    azul=(0,0,255)
    amarelo=(255,255,0)
    ciano=(0,255,255)
    magenta=(255,0,255)

 
    for i in range(len(V)): # verifica se a sequência está correta ee corrige.
        for j in range(i+1,n):
            if V[i]>V[j]:
                N1=V[i]
                V[i]=V[j]
                V[j]=N1
                
    if XS==True: # colocar outra música
        Songs(2)
        

    pygame.display.flip()            
    pygame.init()
    screen= pygame.display.set_mode((1000,800),5,0)
    pygame.display.set_caption("FINALIZADO")
    screen.fill((255,255,255))

    # contas para definir tamanho.
    div3=div1
    div3+=40
    N1=40
    Sub=div3-N1
    
    for a in range (n): # desenha
        N2=480-(V[a]*div2)
        pygame.draw.polygon(screen,verde,([N1,N2],[N1,540],[div3,540],[div3,N2]))
        pygame.draw.polygon(screen,preto,([N1,N2],[N1,539],[div3,539],[div3,N2]),3)
        pygame.draw.rect(screen,preto,(40,40,500,500),3)
        N1=div3
        div3+=Sub

    # a função abaixo define um botão para fechar o gráfico, após finalizar e a ordenação e apos fechar o progama continua
    pygame.display.flip() 
    font = pygame.font.SysFont('Consolas.ttf',70) 
    text = font.render('X' , True , preto)
    TXT= font.render('Organização: Completa', True, preto)
    while True:
        mouse = pygame.mouse.get_pos() 
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: 
                   pygame.quit()   
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 950 <= mouse[0] <= 1000 and 0 <= mouse[1] <= 50:
                    pygame.quit()
                    main(XT,XC,XS,vet,Tempo)
            if 950 <= mouse[0] <= 1000 and 0 <= mouse[1] <= 50:
                pygame.draw.rect(screen,preto,[950,0,50,50],5)
                pygame.draw.rect(screen,vermelho,[950,0,50,50])
            else:
                pygame.draw.rect(screen,verde,[950,0,50,50]) 
            screen.blit(text , (960,5))
            screen.blit(TXT, (50,600))
            pygame.display.update()

def PgTxt(screen,i): # escreve um texto na tela.
    #Cores
    preto=(0,0,0)
    sombra=(18,27,32)
    branco=(255,255,255)
    vermelho=(255,0,0)
    verde=(0,255,0)
    azul=(0,0,255)
    amarelo=(255,255,0)
    ciano=(0,255,255)
    magenta=(255,0,255)
    
    font = pygame.font.SysFont('consolas.ttf', 72)
    if i==1:
        TXT1 = font.render('Bubble Sort', True, preto)
    elif i==2:
        TXT1 = font.render('Selection Sort', True, preto)
    elif i==3:
        TXT1 = font.render('Insertion Sort', True, preto)
    elif i==4:
        TXT1 = font.render('Quick Sort', True, preto)
    elif i==5:
        TXT1 = font.render('Merge Sort', True, preto)
    elif i==6:
        font = pygame.font.SysFont('consolas.ttf', 32)
        TXT1= font.render('Novembro de 2021', True, preto)
        TXT2= font.render('Trabalho: VISUALIZAÇÃO GRAFICA DOS ALGORITMOS DE ORDENAÇÃO ', True, preto)
        screen.blit(TXT2, (40,100))
        TXT3= font.render('Aluno: Lucas Iudi Corregliano Gallinari', True, preto)
        screen.blit(TXT3, (40,200))
        TXT4= font.render('Turma: 2G ', True, preto)
        screen.blit(TXT4, (40,300))
        TXT5= font.render('Matricula:32138628', True, preto)
        screen.blit(TXT5, (50,400))
    screen.blit(TXT1, (50,600))
    


def Menu(x): # printa no IDE uma os instruções.
    if x==0:
        print("Trabalho: VISUALIZAÇÃO GRAFICA DOS ALGORITMOS DE ORDENAÇÃO")
        print("Aluno: Lucas Iudi Corregliano Gallinari")
        print("Turma: 2G")
        print("Matricula:32138628")
        
    elif x ==1:
        print("Digite (1), para organização BubbleSort")
        print("Digite (2), para organização SelectionSort")
        print("Digite (3), para organização InsertionSort")
        print("Digite (4), para organização QuickSort")
        print("Digite (5), para organização MergeSort")
        print("Digite (6),para Créditos")
        print("Digite (7),para Configurações")
        print("Digite (0), para Finalizar o Programa")
        
    elif x==2:
        print("Digite (1), para criar uma Sequência crescente")
        print("Digite (2), para criar uma Sequência decrescente")
        print("Digite (3), para criar uma Sequência aleatória")

    elif x==3:
        print("Digite (1), para criar e salvar uma Sequência")
        print("Digite (2), para configuração do Tempo")
        print("Digite (3), para configuração de Som")
        
    elif x==4:
        print("Digite (0), para Não Salvar a Sequência")
        print("Digite (1), para Salvar a Sequência")

    elif x==5:
        print("O Tempo pode ser colocado em valores entre 0 e 1,")
        print("e é recomendado para reduzir o tempo de espera, porém ainda ser visivel as alterações")
    elif x==6:
        print("Digite (1), para Ativar o Som")
        print("Digite (0), para Desativar o Som")
        
    elif x==7:
        for a in range (5):
            print("")
        print("Sem Configurar o Programa, antes de iniciar a organização, o mesmo irá colocar um Sequência aleatória, com um nùmero aleatório de Elementos")
        print("Deixará o Tempo com Valor igual a 0.1, ou seja, as trocas ocorrerão muito rápido")
        print("e Deixará com o Som padrão")
        for b in range (5):
            print("")

def Copy(V): # recria a sequência
    X=[]
    for a in range(len(V)):
        N1=V[a]
        X.append(N1)
    return X
        
Menu(0)
def Configs(): #define as configuração, inicia e finaliza o programa
    XT=False
    XC=False
    XS=True
    Tempo=0
    vet=[]
    main(XT,XC,XS,vet,Tempo)
    pygame.quit()
        


def main(XT,XC,XS,vet,Tempo): # é aonde define define os comandos
    MAIN=False
    if XS==True:
        Songs(1)
        
    while MAIN==False:
        Menu(1)
        if XT==False and XC==False and XS==True:
            Menu(7)
            
        Verificacao=False
        while Verificacao==False:
            menu=int(input("Digite o Comando: "))
            if -1<menu<8:
                Verificacao=True
            else:
                print("Comando Inválido")

        Verificacao=False
        if menu==7: # abre as Configs
            Verificacao=False
            while Verificacao==False: # Comando das Configs
                Menu(3)
                X=int(input("Digite o Comando: "))
                if 0<X<4:
                    Verificacao=True
                else:
                    print("Comando Inválido")
            if X==1:        
                Verificacao=False
                while Verificacao==False:  # define o tamanho da sequência
                    n=int(input("Tamanho da Sequência: "))
                    if n>0 and n<126:
                        Verificacao=True
                    else:
                        print("Valor Inválido")
                        if n>125:
                            print("Números maiores que 125 ocasionam problemas na hora de visualizar a animação")
                        elif n<=0:
                            print("Números negativos ou zero, não são válidos")
                
                Verificacao=False
                while Verificacao==False: # define iqual será a organização da sequência
                    Menu(2)
                    c=int(input("Selecione o Tipo de Sequência: "))
                    if 1<=c<=3:
                        Verificacao=True
                        XC=True
                        vet=geraVetor(c,n)
                        print(vet)
                    else:
                        print("Comando Inválido")

                Verificacao=False
                while Verificacao==False: # Salva sequência ou não
                    Menu(4)
                    Salvar=int(input("Salvar ou Não: "))
                    if Salvar==1 or Salvar==0:
                        Verificacao=True
                        if Salvar==1:
                            print("Sequência Salva")
                        elif Salvar==0:
                            XC=False
                        Config1=True
                                  
                    else:
                        print("Comando Inválido")

            elif X==2:
                Verificacao=False
                while Verificacao==False: # define o Tempo
                    Menu(5)
                    Tempo=float(input("Selecione quanto será o tempo de espera entre cada troca em segundos: "))
                    if Tempo>=0:
                        Verificacao=True
                        XT=True
            
                    else:
                        print("Comando Inválido")
                        
                Verificacao=False
                while Verificacao==False: # salva o Tempo
                    Salvar=int(input("Salvar(1) ou Não(0): "))
                    if Salvar==1 or Salvar==0:
                        Verificacao=True
                        if Salvar==1:
                            print("Tempo Salvo")
                        elif Salvar==0:
                            XT=False
                        Config2=True
                                  
                    else:
                        print("Comando Inválido")

                        
            elif X==3:
                Verificacao=False
                while Verificacao==False: # ativa ou desativa o Som
                    Menu(6)
                    Som=int(input("Ativar(1) ou Desativar(0): "))
                    if -1<Som<2:
                        if Som==1:
                            Verificacao=True
                            XS=True
                        elif Som==0:
                            Verificacao=True
                            XS=False
                        elif XT==False:
                            Tempo=0.1
                        elif XC==False:
                            vet=[]
                        pygame.init()
                        pygame.quit()
                        main(XT,XC,XS,vet,Tempo)#Recomeça o codigo com ou sem o som ,com as mesmas configs.
                    else:
                        print("Comando Inválido")
        
        N=random.randint(1,125)
        if menu==1: # inicia Bubble Sort
            print("BubbleSort")
            if XC==True: # se tiver uma sequência Salva ela é regastada
                B1=Copy(vet)
                n=len(vet)
            elif XC==False: # se não a sequência é gerada de maneira aleatoria
                n=N
                B1=geraVetor(3,n)
                print(B1)
            div1=500/n
            div2=440//125
            T=0.1
            if XT==True: # define o tempo
                T=Tempo
            Vet1=BubbleSort(B1,n,div1,div2,Tempo,XS) # coloca em bubble sort, com as configurações
            print(B1)
            Finish(Vet1,n,div1,div2,XT,XC,XS,vet,Tempo) # Desenha o final

            # todas as opções seguem o mesmo estilo do bubble sort acima.
                    
        elif menu==2: # inicia Selection Sort
            print("SelectionSort")
            if XC==True:
                S1=Copy(vet)
                n=len(vet)
            elif XC==False:
                n=N
                S1=geraVetor(3,n)
                print(S1)
            div1=500/n
            div2=440//125
            T=0.1
            if XT==True:
                T=Tempo
            Vet2=SelectionSort(S1,n,div1,div2,T,XS)
            print(S1)
            Finish(Vet2,n,div1,div2,XT,XC,XS,vet,Tempo)
                    
        elif menu==3: # Inicia Insertion Sort
            print("InsertionSort")
            if XC==True:
                I1=Copy(vet)
                n=len(vet)
            elif XC==False:
                n=N
                I1=geraVetor(3,n)
                print(I1)
            div1=500/n
            div2=440//125
            T=0.1
            if XT==True:
                T=Tempo
            Vet3=InsertionSort(I1,n,div1,div2,T,XS)
            print(I1)
            Finish(Vet3,n,div1,div2,XT,XC,XS,vet,Tempo)
                    
        elif menu==4: # inicia Quick Sort
            print("QuickSort")
            if XC==True:
                Q1=Copy(vet)
                n=len(vet)
            elif XC==False:
                n=N
                Q1=geraVetor(3,n)
                print(Q1)
            div1=500/n
            div2=440//125
            T=0.1
            if XT==True:
                T=Tempo
            QuickSort(Q1,0,(len(Q1)-1),div1,div2,T,XS)
            print(Q1)
            Finish(Q1,n,div1,div2,XT,XC,XS,vet,Tempo)
                    
        elif menu==5: # inicia Merge Sort
            print("MergeSort")
            if XC==True:
                M1=Copy(vet)
                n=len(vet)
            elif XC==False:
                n=N
                M1=geraVetor(3,n)
                print(M1)
            div1=500/n
            div2=440//125
            T=0.1
            if XT==True:
                T=Tempo
            MergeSort(M1,0,(len(M1)-1),div1,div2,T,XS)
            Finish(M1,n,div1,div2,XT,XC,XS,vet,Tempo)
            print(M1)
                    
        elif menu==6:
            Menu(0)
            #Cores
            preto=(0,0,0)
            sombra=(18,27,32)
            branco=(255,255,255)
            vermelho=(255,0,0)
            verde=(0,255,0)
            azul=(0,0,255)
            amarelo=(255,255,0)
            ciano=(0,255,255)
            magenta=(255,0,255)

            # Função do Botão
            pygame.init()
            screen= pygame.display.set_mode((1000,800),5,0)
            pygame.display.set_caption("Créditos")
            screen.fill((255,255,255))
            PgTxt(screen,6)
            pygame.display.flip() 
            font = pygame.font.SysFont('Consolas.ttf',70) 
            text = font.render('X' , True , preto) 
            while True:
                mouse = pygame.mouse.get_pos() 
                for ev in pygame.event.get(): 
                    if ev.type == pygame.QUIT: 
                        pygame.quit()   
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if 950 <= mouse[0] <= 1000 and 0 <= mouse[1] <= 50:
                            pygame.quit()
                            main(XT,XC,XS,vet,Tempo)
                if 950 <= mouse[0] <= 1000 and 0 <= mouse[1] <= 50:
                    pygame.draw.rect(screen,preto,[950,0,50,50],5)
                    pygame.draw.rect(screen,vermelho,[950,0,50,50])
                else: 
                    pygame.draw.rect(screen,verde,[950,0,50,50]) 
                screen.blit(text , (960,5))
                pygame.display.update()

        # finaliza o programa
        elif menu==0:
            if XS==True:
                Songs(3)
                time.sleep(8)
            print("Programa Finalizado")
            MAIN=True


Configs()

