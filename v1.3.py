'''
Projeto:
Automação utilizada para gerar legenda de vídeos do youtube.

Modo de utilização:
Colar o link do vídeo que quer a legenda, esperar o programa fazer a conversão,
e escolher o diretório de onde quer salvar o arquivo .txt

Como foi feito?
Esta versão funciona tudo!

Motivo:
Nova versão do código
Adicionei o PySimpleGUI

Solução: A função transcribe_and_save_audio transcreve o áudio e salva a transcrição em um arquivo de texto.
Além disso, foram adicionados tratamentos de exceção para lidar com possíveis erros durante a transcrição e o salvamento.

Documentação presente no portfólio pessoal no github.com/vmellozk'''

import yt_dlp
import whisper
import PySimpleGUI as sg
import os

def download_audio(video_url, output_path='audio'):
    try:
        ydl_opts = {
            'format': 'bestaudio/best', 
            'outtmpl': output_path,

            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

    except Exception as error:
        print("\nERRO NO DOWNLOAD", error)
        print()

def transcribe_and_save_audio(audio_path, output_file='transcription.txt'):
    try:
        model = whisper.load_model('base') 
        result = model.transcribe(audio_path)
        transcription = result['text']
        
        try:
            with open(output_file, 'w') as file:
                file.write(transcription)

        except Exception as e:
            print("Erro ao salvar a transcrição:", str(e))
    except Exception as error:
        print('\nERRO PARA CONVERTER O AUDIO EM TEXTO', error)
        print()

#Definindo o tema
sg.theme('Reddit')
#Definindo o Layout
layout = [
    [sg.Text('Cole sua URL aqui: '), sg.InputText(key='-URL-')],
    [sg.Text('Escolha onde quer salvar: '), sg.InputText(key='-OUTPUT-', enable_events=True), sg.FolderBrowse()],
    [sg.Button('Baixar'), sg.Button('Cancelar')]
]

#Criando a janela e implementando o layout dentro
janela = sg.Window('Conversor de Áudio em Texto', layout)

#Criando as ações de dentro da janela   
while True:
    #Ler qualquer evento que ocorra na janela
    #Evento --> que ocorreu, ex: botão pressionado
    #Valores --> dos elementos da janela, ex: texto inserado no campo de entrada
    event, values = janela.read()
    #Condição para fechar a janela
    if event == sg.WINDOW_CLOSED or event == "Cancelar":
        break

    elif event == 'Baixar':
        video_url = values['-URL-']          #key
        output_dir = values['-OUTPUT-']      #key

        #Variáveis que usam a função .join() para fazerem o link da key do diretório escolhido e dá o nome do arquivo padrão
        audio_path = os.path.join(video_url, 'audio')
        transcription_path = os.path.join(output_dir, 'transcription.txt')

        download_audio(video_url, 'audio')
        transcribe_and_save_audio('audio.mp3')