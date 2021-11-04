from pygame import mixer,mixer_music
from os.path import dirname, join, basename
from arquivos.classe_player import *
from glob import glob
from os import curdir
from sys import platform
import time

Player_Musica = Player_mp3()
class Funcoes_Player(object):
    """
    Classe de controle das funções do player
    """
    def buscar_arquivos_mp3(self):
        """
        ira procurar qualquer arquivo mp3 que houver na pasta selecionada ->'Player_Musica.pasta_linux'
        """
        if len(Player_Musica.playlist) > 0:
            # verificar se a lista já possui musicas
            # caso sim, a lista será limpada
            Player_Musica.playlist.clear()
            print('limpando lista')
        # verificando qual o sistema operacional está em uso
        if 'linux' in platform:
            print(Player_Musica.Linux)
            try:
                #Numerador para as musicas
                Player_Musica.nmusicas = 0
                for musica in glob(join(curdir,Player_Musica.pasta_linux, '*.mp3')):
                    # contar numero de musicas
                    Player_Musica.nmusicas = Player_Musica.nmusicas + 1
                    # nome da musica
                    print(Player_Musica.nmusicas, '°', basename(musica[:-4]).replace('_', ' '))
                    # adicionar a lista de reprodrução
                    Player_Musica.playlist.append(musica)


            except:
                print("Diretórios de músicas não encontrados!...");
        # verificando qual o sistema operacional está em uso
        if 'win' in platform:
            print(Player_Musica.windows)
            try:
                # Numerador para as musicas
                Player_Musica.nmusicas = 0
                for musica in glob(join(curdir, "/media/the_felipe/Arquivos2/musicas", '*.mp3')):
                    # contar numero de musicas
                    Player_Musica.nmusicas = Player_Musica.nmusicas + 1
                    # nome da musica
                    print(Player_Musica.nmusicas, '°', basename(musica[:-4]).replace('_', ' '))
                    # adicionar a lista de reprodrução
                    Player_Musica.playlist.append(musica)

            except:

                print("Diretórios de músicas não encontrados!...")

        print("player mp3 inicializado...")

    def inicializar(self):
        """Inicializando mixer de audio, carregando musica inicial e
        configurando o volume da musica inicial"""
        mixer.init(frequency=Player_Musica.frequencia_som, size=-16, channels=2, buffer=5996)



    def iniciar(self):
        if mixer.get_init() == None:
            self.inicializar()
            tocando = mixer_music.get_busy()
            if tocando == False:
                x = mixer_music.get_busy()
                musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
                mixer_music.set_volume(Player_Musica.volume)
                mixer_music.play()

            else:
                print("já inicializado")

            print("frequênci atual:  ", Player_Musica.frequencia_som)
            print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))

    def sair(self):
        """
        Encerrar o mixer de audio
        """
        try:
            mixer_music.stop()
            mixer.quit()
            print("Encerrando music_x player.....")
        except:
            print("deseja sair mesmo...N/S ou s/n ")
            print("Encerrando music_x player.....")

    def play_pause(self):
        """
        Continuar e pausar musica
        """
        tocando = mixer_music.get_busy()
        if tocando == False:
            mixer_music.unpause()
            print("Musica tocando")

        else:
            mixer_music.pause()
            print("Musica em parad")

    def reinicio(self):
        """
        Reiniciar a musica
        """
        mixer_music.rewind()
        print("Musica reinicializada")

    def aumentar_vol(self):
        """
        Aumentar o volume do mixer de audio
        """
        Player_Musica.volume = Player_Musica.volume + 0.05
        if Player_Musica.volume > 1:
            Player_Musica.volume = 1
            mixer_music.set_volume(Player_Musica.volume)
            print('volume: ', str(Player_Musica.volume))
        else:
            mixer_music.set_volume(Player_Musica.volume)
            print('volume: ', str(Player_Musica.volume))

    def abaixar_vol(self):
        """
        Diminuir o volume do mixer de audio
        """
        Player_Musica.volume = Player_Musica.volume - 0.05
        if Player_Musica.volume < 0:
            Player_Musicavolume = 0
            mixer_music.set_volume(Player_Musica.volume)
            print('volume: ', str(Player_Musica.volume))
        else:
            vol = mixer.music.set_volume(Player_Musica.volume)
            print('volume: ', str(Player_Musica.volume))
    def Listar_musicas(self):
        """
        Retorna a lista contendo todas as muiscas da playlist
        """
        return Player_Musica.playlist

    def total_musicas(self):
        """
        Exibir total de musicas
        """
        print('Total de musicas: ',len(Player_Musica.playlist))

    def avancar_musica(self):
        """
        Avançar a musica
        """
        if Player_Musica.rodando + 1 >= len(Player_Musica.playlist):
            mixer_music.stop
            Player_Musica.rodando = 0
            musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
            mixer_music.play()
            print("if frequência de som atual:  ", Player_Musica.frequencia_som)
            print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))

        else:
            mixer_music.stop
            Player_Musica.rodando = Player_Musica.rodando + 1
            musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
            mixer_music.play()
            print("else frequência de som atual:  ", Player_Musica.frequencia_som)
            print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))

    def voltar_musica(self):
        """
        Voltar musica
        """
        if mixer.init:
            mixer.init()
        if Player_Musica.rodando <= 0:
            music_x = 0
            mixer_music.stop
            l = len(Player_Musica.playlist)
            Player_Musica.rodando = l - 1
            musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
            mixer_music.play()
            print("frequênci atual:  ", Player_Musica.frequencia_som)
            print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))
        else:
            music_x = 0
            mixer_music.stop
            Player_Musica.rodando = Player_Musica.rodando - 1
            musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
            mixer_music.play()
            print("frequênci atual:  ", Player_Musica.frequencia_som)
            print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))

    def sintonizar_frequencia(self):
        """
        Atualizar frequencia de som
        """
        print("(--sintonização manual de frequência--)")
        try:
            freq = int(input("Digite o número da frequência... "))
            if not len(str(Player_Musica.frequencia_som)) < 4:
                mixer.quit()
                Player_Musica.frequencia_som = freq
                mixer.init(frequency=Player_Musica.frequencia_som)
                musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
                mixer.music.set_volume(Player_Musica.volume)
                mixer_music.play()
                print("frequênci atual:  ", Player_Musica.frequencia_som)
                print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))

            else:
                print("Digite 4 algarismos: entrada - ", len(str(freq)), " algarismos")
        except:
            print("Digite apenas numeros...")

    def procurar_p_numeracao(self):
        """
        Procurar música pela numeração.
        Ná dúvida digite 'mm' para saber quantas musicas existem na playlist
        """

        try:
            music_x = int(input("digite o número da música: "))
            if not music_x - 1 > len(Player_Musica.playlist) or music_x - 1 < 1:
                if mixer.get_init()==False:
                    mixer.quit()
                    self.inicializar()
                else:
                    print("Player já inicializou - ", Player_Musica.frequencia_som)

                print("======================================")
                print("Total de musicas listadas: ", len(Player_Musica.playlist))
                print("======================================")

                Player_Musica.rodando = music_x - 1
                musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
                mixer_music.set_volume(Player_Musica.volume)
                mixer_music.play()
                print("frequênci atual:  ", Player_Musica.frequencia_som)
                print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))


            else:
                print("======================================")
                print("Musica nao encontrada... ")
                print("total de musicas listadas: ", len(Player_Musica.playlist))
                print("======================================")


        except:
            print("digite apenas números....0 - ", len(Player_Musica.playlist))

    def tempo_segundos(self):
        """
        Mostrar o tempo decorrido da musica em segundos
        """
        temp = mixer_music.get_pos()
        pos3 = time.strftime("%H:%M:%S", time.gmtime(temp / 1000))
        print(pos3)

    def ajuda(self):
        """
        Exibir todos os comandos
        """
        print("""
        ------------------------------------------------------------------------
                Para verificar número de músicas digite -- nn 
                Para ver a lista de músicas digite --------mm
                Para avançar ----------------------------- >
                Para Voltar ------------------------------ <
                Para pausar ou continuar ----------------- 'p' , 'c'
                Para selecionar por número --------------- start, iniciar
                Para sintonizar a frequência de som ------ fre
                Para controlar volume -------------------- diminuir(-,_) aumentar(=,+)
                Para encerrar o programa digite ---------- n, nao
                Para atualizar a pasta de músicas -------- update, atualizar, add
        -------------------------------------------------------------------------        
        |__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
        -------------------------------------------------------------------------

                """)



