import yt_dlp
import whisper
import PySimpleGUI as sg
import os
from instaloader import Instaloader

def download_audio_youtube(video_url, output_path='audio'):
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

def transcribe_and_save_audio_youtube(audio_path, output_file='transcription.txt'):
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

def download_video_instagram(url, output_dir):
    try:
        loader = Instaloader()
        loader.download_videos(url, filename = os.path.join(output_dir, "video_instagram.mp4"))
        sg.popup("Download concluído!")
    except Exception as error:
            print(f"Erro ao baixar o vídeo: {str(error)}")

def download_audio_instagram():
        pass

sg.theme('Reddit')
layout = [
    [sg.TabGroup([
        [
            sg.Tab("Youtube", [
                [sg.Text('Cole sua URL aqui: '), sg.InputText(key='-URL-')],
                [sg.Text('Escolha onde quer salvar: '), sg.InputText(key='-OUTPUT-', enable_events=True), sg.FolderBrowse()],
                [sg.Button('Baixar Áudio YT'), sg.Button("Baixar Vídeo YT"), sg.Button("Baixar e Converter Áudio em Legenda"), sg.Button('Cancelar', key='CANCEL-YT')]
            ]),
            sg.Tab("Instagram", [
            [sg.Text('Cole sua URL aqui: '), sg.InputText(key='URL-IG')],
            [sg.Text('Escolha onde quer salvar: '), sg.InputText(key='OUTPUT-IG', enable_events=True), sg.FolderBrowse()],
            [sg.Button('Baixar Áudio IG'), sg.Button("Baixar Vídeo IG"), sg.Button('Cancelar', key='CANCEL-IG')]
            ])
        ]
                ])
    ]
]

window = sg.Window('Conversor de Áudio em Texto', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event in ('CANCEL-YT', 'CANCEL-IG', 'CANCEL-TIK'):
        break

    elif event == 'Baixar Áudio YT':
        video_url = values['-URL-']
        output_dir = values['-OUTPUT-']
        audio_path = os.path.join(video_url, 'audio')
        download_audio_youtube(video_url, 'audio')
        sg.popup("Download realizado!")

    elif event == "Baixar Vídeo YT":
        pass

    elif event == 'Baixar e Converter Áudio em Texto':
        video_url = values['-URL-']
        output_dir = values['-OUTPUT-']
        audio_path = os.path.join(video_url, 'audio')
        transcription_path = os.path.join(output_dir, 'transcription.txt')
        download_audio_youtube(video_url, 'audio')
        transcribe_and_save_audio_youtube('audio.mp3')
        sg.popup("Download e conversão realizados!")

    elif event == "Baixar Áudio IG":
        pass

    elif event == "Baixar Vídeo IG":
        download_video_instagram(values['URL-IG'], values['OUTPUT-DIR'])
