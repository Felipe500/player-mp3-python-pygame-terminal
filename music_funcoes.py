from pygame import mixer,mixer_music
from os.path import basename
from os.path import dirname, join, basename
from variaveis import *
from glob import glob
from os import curdir
tocar = True
from sys import platform


def varrer_mp3():
        global nmusicas
        global musicas
        global rodando
        if len(musicas)>0:
                musicas.clear()
                print('limpando lista')
        #varrer pasta
        """
        curdir = dirname(__file__)
        for filename in glob(join(curdir, "D:/Projetos e programas tecnico em informática/SYSTEM/AR/multimidia", '*.mp3')):
            #contar numero de musicas
            nmusicas = nmusicas + 1
            #nome da musica
            print(nmusicas,'°',basename(filename[:-4]).replace('_', ' '))
            #exibir caminhos de musicas
            #print(filename)
            #adicionar a lista de reprodrução
            musicas.append(filename)
            """
        if 'linux' in platform:
                print("""
				_____________________///////
        		PLataforma Linux @_@
        		--------------------- 
        		""")
                try:
                        curdir2 = dirname(__file__)
                        for filename2 in glob(join(curdir2, "/media/the_felipe/Arquivos2/musicas", '*.mp3')):
                            #contar numero de musicas
                            nmusicas = nmusicas + 1
                            #nome da musica
                            print(nmusicas,'°',basename(filename2[:-4]).replace('_', ' '))
                            #exibir caminhos de musicas
                            #print(filename2)
                            #adicionar a lista de reprodrução
                            musicas.append(filename2)
                        if musicas.count==0:
                                 pass

                except:
                       print("Diretórios de músicas não encontrados!...");
        if 'win' in platform:
            
        	

            try:
                curdir2 = dirname(__file__)
                for filename2 in glob(join(curdir2, "D:\musicas", '*.mp3')):
                    #contar numero de musicas
                    nmusicas = nmusicas + 1
                    #nome da musica
                    print(nmusicas,'°',basename(filename2[:-4]).replace('_', ' '))
                    #exibir caminhos de musicas
                    #print(filename2)
                    #adicionar a lista de reprodrução
                    musicas.append(filename2)

            except:
            
                print("Diretórios de músicas não encontrados!...")
            
            print(windows)    
        print("player mp3 inicializado...")           

def inicio():
        global rodando
        global fre
        freq =mixer.get_init()
        
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',musicas[rodando])
        global resp
        resp = str(input("Deseja ouvir  musicas pelo pygame? sim-s/não-n "))
        print(os.get_exec_path(musicas))
       
    
def iniciar():
        global rodando
        global volume
        global fre
        global musicas
        if mixer.init:
                mixer.init()
                        
        print(mixer.get_init())
        print(musicas[rodando])
        musica = mixer_music.load(musicas[rodando])
        
        mixer_music.set_volume(volume)
        mixer_music.play()
        x = mixer_music.get_busy()
        if x==0:
                print("mal mixado")
                
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',basename(musicas[rodando]))
        

def sair():
      
        try:
                mixer_music.stop()
                mixer.quit()
                print("Encerrando music_x player.....")
                
        
        except:
                print("deseja sair mesmo...N/S ou s/n ")
                print("Encerrando music_x player.....")
                
        
def pausar():
    mixer.music.pause()
    print("(PAUSE)")
    print("Pressione 'c' para continuar")
def continua():
    mixer_music.unpause()
    print("Pressione 'c' para continuar")

def reinicio():
    mixer_music.rewind()        
    print("Musica reinicializada")
def aumentar_vol():
    global volume
    volume=volume+0.05
    if volume>1:
            volume=1
            mixer_music.set_volume(volume)
            print('volume: ',str(volume))
    else:
            mixer_music.set_volume(volume)
            print('volume: ',str(volume))
        
def abaixar_vol():
    global volume
    volume=volume-0.05
    if volume<0:
            volume=0
            mixer_music.set_volume(volume)
            print('volume: ',str(volume))
    else:
            vol = mixer.music.set_volume(volume)
            print('volume: ',str(volume))

def avancar():
    #definir a variavel que vai ser usada global na função    
    global rodando
    global musicas
    global fre
    try:
        if mixer.init:
                mixer.init()    
        mixer_music.stop
        
        rodando=rodando+1
        musica = mixer_music.load(musicas[rodando])
        mixer_music.play()
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',basename(musicas[rodando]))
        x = mixer_music.get_busy()
        if x==0:
                print("mal mixado")
        

    except:
        print("retorno...")
        
        rodando = 0
            
        mixer_music.stop
            
        musica = mixer_music.load(musicas[rodando])
        mixer_music.play()
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',basename(musicas[rodando]))
        x = mixer_music.get_busy()
        if x==0:
                print("mal mixado")

def voltar():
    global rodando
    global musicas
    global music_x
    global fre
    if mixer.init:
                mixer.init()
    if rodando<=0:
        music_x = 0
        mixer_music.stop
        l = len(musicas)
        rodando=l-1
        musica = mixer_music.load(musicas[rodando])
        mixer_music.play()
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',basename(musicas[rodando]))
        

    else:
        music_x = 0
        mixer_music.stop
        rodando=rodando-1
        musica = mixer_music.load(musicas[rodando])
        mixer_music.play()
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',basename(musicas[rodando]))
        


def auto_freq():
        global rodando
        global volume
        global musicas
        global fre
        
        while True:
                x = mixer_music.get_busy()
                c=0
                for c in freq:
                        if x==0:
                                mixer.quit()
                                mixer.init(frequency=freq[c])
                                musica = mixer_music.load(musicas[rodando])
                                mixer.music.set_volume(volume)
                                mixer_music.play()
                                c=c+1
                        
                        
                print("---musica ajustada---")
                
        

        
def sintonizar_frequencia():
        global rodando
        global volume
        global musicas
        global fre
        print("(--sintonização manual de frequência--)")
        fre = int(input("Digite o número da frequência... "))
        
      
           
        mixer.quit()
        mixer.init(frequency=fre)
        musica = mixer_music.load(musicas[rodando])
        mixer.music.set_volume(volume)
        mixer_music.play()
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',basename(musicas[rodando]))
     

def procurar_p_numeracao():
        global rodando
        global volume
        global musicas
        global fre

        try:
                music_x = int(input("digite o número da música: "))
        
                if mixer.init:
                        print('Mixer de Audio não inicializou...')
                        for z in range(10):
                                print('Iniciando...',z)
                        mixer.init(frequency=fre)
                else:
                      mixer.quit()   
                if music_x-1>len(musicas) or music_x-1<0:
                    print("musica não esta na lista ")
                    print("total de musicas listadas: ",len(musicas))
                try:
                    rodando = music_x-1
                   
                    
                    musica = mixer_music.load(musicas[rodando])
                    mixer.music.set_volume(volume)
                    mixer_music.play()
                    print("frequênci atual:  ",fre)    
                    print(rodando+1,' ',basename(musicas[rodando]))

                    
                except:
                    print("não listado...")

        except:
                print("digite apenas números....0 - ",len(musicas))
        
def tempo_segundos():
        temp = mixer_music.get_pos()
        print(temp)


def ajuda():
        print("""
------------------------------------------------------------------------
        Para verificar número de músicas digite -- nn 
        Para ver a lista de músicas digite --------mm
        Para avançar ----------------------------- >
        Para Voltar ------------------------------ <
        Para pausar ------------------------------ p
        Para continuar - ------------------------- c
        Para selecionar por número --------------- start, iniciar
        Para sintonizar a frequência de som ------ fre
        Para controlar volume -------------------- diminuir(-,_) aumentar(=,+)
        Para encerrar o programa digite ---------- n, nao
        Para atualizar a pasta de músicas -------- update, atualizar, add
-------------------------------------------------------------------------        
|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
-------------------------------------------------------------------------

        """)
def mx():
        global select_fre
        global rodando
        global musicas
        global volume
        global freq
        global v
        v=0
        certo = False

       
                        
                





