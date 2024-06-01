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
Solução: A função transcribe_and_save_audio transcreve o áudio e salva a transcrição em um arquivo de texto.
Além disso, foram adicionados tratamentos de exceção para lidar com possíveis erros durante a transcrição e o salvamento.

Documentação presente no portfólio pessoal no github.com/vmellozk'''


# Bibliotecas necessárias para o funcionamento
import yt_dlp
import whisper

# Função para baixar o áudio
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



# Função para transcrever o áudio e salvar a transcrição em um arquivo de texto
def transcribe_and_save_audio(audio_path, output_file='transcription.txt'):
    try:
        # Carregar o modelo Whisper
        model = whisper.load_model('base') 
        # Transcrever o áudio
        result = model.transcribe(audio_path)
        transcription = result['text']
        
        # Salvar a transcrição em um arquivo de texto
        try:
            with open(output_file, 'w') as file:
                file.write(transcription)

        except Exception as e:
            print("Erro ao salvar a transcrição:", str(e))
    except Exception as error:
        print('\nERRO PARA CONVERTER O AUDIO EM TEXTO', error)
        print()



# Script principal
if __name__ == '__main__':
    url = input('URL: ')
    download_audio(url, 'audio')
    transcribe_and_save_audio('audio.mp3')
