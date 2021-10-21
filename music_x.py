from pygame import mixer,mixer_music


from os import curdir
from music_funcoes import *

#buscar directorios de musicas e pastas(path) 
#print(listdir('e:/Ar'))


varrer_mp3()

print("bem-vindo ao Music x....")

print(mixer.get_init())
mixer.init(frequency=44100 ,size=-16,channels=2,buffer=5996)  
while tocar==True:
    
     
    
    freq =mixer.get_init()    
    
    print("s/sim(iniciar)--n/nao(encerrar)--comandos(ajuda)")
    resp = str(input("digite seu comando: ",))
    o = mixer.get_busy()

   
    if resp == 'temp':
        tempo_segundos()
    
    if o ==0:
        print("erro na frequencia")
    if mixer_music == False:
        print("não legal")
    
    #iniciar audio
    if resp == 's' or resp == 'sim' or resp=='S':
        iniciar()    
        
    #encerrar audio        
    elif resp == 'n' or resp=='nao' or resp=='N':
        sair()
        tocar=False

    #PAUSAR AUDIO
    elif resp == 'p' or resp == 'P':
        pausar()
    #CONTINUAR    
    elif resp == 'c' or resp == 'C':
        continua()

    #Reiniciar
    elif resp == 'r' or resp == 'R':
        
        reinicio()  
    #AUMENTAR VOLUME
    elif resp == '=' or resp=='+':
       aumentar_vol()
        
    #ABAIXAR VOLUME
    elif resp == '_' or resp=='-':
        abaixar_vol()
        
    #EXIBIR VOLUME    
    elif resp == 'vol' or resp == 'volume':
        print('volume: ',str(volume))

    #AVANÇAR
    elif resp == '>':
        avancar()
            

     #voltar   
    elif resp == '<':
        voltar()

    #lista musicas   
    elif resp == 'mm':
        n=0
        for x in musicas:
            n=n+1
            print('musicas:',n,'°' ,basename(x[:-4]))
     #exibir número de musicas       
    elif resp == 'nn' or resp=='show':
        print('número de musicas: ',len(musicas))
    #procurar sintonia de frequencia de som 
    elif resp == 'fre':
        sintonizar_frequencia()
    #buscar por numeração na lista      
    elif resp == 'buscar' or resp == 'scaner' or resp=='iniciar' or resp=='start':
        procurar_p_numeracao()
          
    elif resp == 'tsf' or resp == 'test':
        mx()

    elif resp == 'helpe' or resp=='ajuda':
        print("......................")
        ajuda()
    elif resp== 'atualizar' or 'update' or 'add':
        mixer.quit()
        varrer_mp3()


   
