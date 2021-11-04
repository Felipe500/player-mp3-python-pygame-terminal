from arquivos.Player_Funcoes import *

class Aplication(Funcoes_Player):
    def __init__(self):
        self.tocar = True
        self.buscar_arquivos_mp3()
        self.iniciar()
        self.play()

    def play(self):

        while self.tocar==True:  
            freq =mixer.get_init()    
            
            print("s/sim(iniciar)--n/nao(encerrar)--comandos(ajuda)")
            resp = str(input("digite seu comando: ",))
            o = mixer.get_busy()

           
            if resp == 'temp':
                self.tempo_segundos()
            
            
            #iniciar audio
            if resp == 's' or resp == 'sim' or resp=='S':     
                self.iniciar()
                
            #encerrar audio        
            elif resp == 'n' or resp=='nao' or resp=='N':
                self.sair()
                self.tocar=False

            #PAUSAR AUDIO
            elif resp == 'p' or resp == 'P':
                self.play_pause()
            #CONTINUAR    
            elif resp == 'c' or resp == 'C':
                self.play_pause()

            #Reiniciar
            elif resp == 'r' or resp == 'R':
                
                self.reinicio()
            #AUMENTAR VOLUME
            elif resp == '=' or resp=='+':
               self.aumentar_vol()
                
            #ABAIXAR VOLUME
            elif resp == '_' or resp=='-':
                self.abaixar_vol()
                
            #EXIBIR VOLUME    
            elif resp == 'vol' or resp == 'volume':
                print('volume: ',str(self.volume))

            #AVANÇAR
            elif resp == '>':
                self.avancar_musica()
                    
             #voltar   
            elif resp == '<':
                self.voltar_musica()

            #lista musicas   
            elif resp == 'mm':
                musicas = self.Listar_musicas()
                n=0
                for x in musicas:
                    n=n+1
                    print('musica:',n,'°' ,basename(x[:-4]))

             #exibir número de musicas       
            elif resp == 'nn' or resp=='show':
                self.total_musicas()

            #procurar sintonia de frequencia de som 
            elif resp == 'fre':
                self.sintonizar_frequencia()

            #buscar por numeração na lista      
            elif resp == 'buscar' or resp == 'scaner' or resp=='iniciar' or resp=='start':
                self.procurar_p_numeracao()

            elif resp == 'helpe' or resp=='ajuda':
                self.ajuda()

            elif resp== 'atualizar' or resp== 'update' or resp== 'add':
                mixer.quit()
                self.buscar_arquivos_mp3()
                self.iniciar()
         
Aplication()


