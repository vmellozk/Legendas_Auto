#Bibliotecas necessárias para o funcionamento
import yt_dlp
import whisper

#Função para baixar o áudio
def download_audio(video_url, output_path = 'audio'):
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

#Função para converter o áudio salvo em texto
def transcribe_audio(audio_path):
    model = whisper.load_model('base')
    result = model.transcribe(audio_path)
    print(audio_path)
    return result['text']
    print(result)

#Função para salvar o arquivo
def save_and_convert_fileText(transcription, output_file='transcription.txt'):
    with open(output_file, 'w') as file:
        file.write(transcription)

#Script principal
if __name__ == '__main__':
    video_url = input('URL: ')
    download_audio(video_url, 'audio')
    transcription = transcribe_audio('audio')
    save_and_convert_fileText(transcription)

    print("Conversão feita!")
