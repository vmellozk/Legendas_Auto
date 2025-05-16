import whisper

def transcribe_and_save_audio_youtube(audio_path, output_file):
    try:
        model = whisper.load_model('base')
        result = model.transcribe(audio_path)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result['text'])
    except Exception as e:
        print("Erro na transcrição:", str(e))
