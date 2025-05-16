# 📝 Gerador de Legendas e Transcrições com IA

Ferramenta com interface gráfica que transforma automaticamente o áudio de vídeos em texto, utilizando inteligência artificial. Ideal para criar transcrições, apoiar a acessibilidade, organizar conteúdos e auxiliar nos estudos.

## ✨ Funcionalidades

- 🎙️ Transcrição automática de áudio com alta precisão (.txt)
- 🎞️ Geração de legendas sincronizadas (em breve)
- 🌐 Suporte multilíngue (em desenvolvimento)
- 🧠 IA baseada no modelo Whisper da OpenAI
- 🖥️ Interface gráfica moderna com PySide6
- 💾 Salvamento automático em diretórios definidos pelo usuário

---

## 📷 Demonstração

![Demonstração da interface](imagem.png)

---

## ⚙️ Tecnologias Utilizadas

- [Whisper (OpenAI)](https://github.com/openai/whisper) – Transcrição com IA
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) – Download de vídeos do YouTube e Instagram
- [PySide6 (Qt)](https://doc.qt.io/qtforpython/) – Interface gráfica
- [Instaloader](https://instaloader.github.io/) – Suporte complementar ao Instagram
- `os`, `pathlib`, `shutil`, entre outros – Manipulação de arquivos

---

## 🚀 Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/vmellozk/criador-legendas.git
cd criador-legendas
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
```

4. Ative o ambiente virtual:

```bash
source venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

5. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Execute a aplicação:

```bash
python audio_transcriber.py
```

## 🛠️ Estrutura do Projeto

```kotlin
📁 criador-legendas/
├── assets/                # Pasta com arquivos de imagens do aplicativo
│ 
├── core/                  # Funções principais (transcrição, download, etc.)
│   ├── instagram.py
│   ├── transcription.py
│   └── youtube.py
│
├── gui/                   # Interface gráfica com PySide6
│   ├── __init__.py
│   └── ui_main.py
│
├── main.py                # Arquivo principal para iniciar a aplicação
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação
```

## 📌 Aplicações

- Acessibilidade para pessoas com deficiência auditiva
- Transcrição de entrevistas, aulas, podcasts e vídeos
- Organização de conteúdos audiovisuais
- Apoio a estudos e produção de material didático

## 🧪 Em Desenvolvimento

- Tradução automática de transcrições
- Suporte completo a múltiplos idiomas
- Exportação para PDF e outros formatos
- Otimização da segmentação e pontuação

## 📄 Licença
Este projeto está licenciado sob a Licença MIT. Disponibilizarei o arquivo 'LICENSE' para mais detalhes.

## 🤝 Contribuições
Contribuições são bem-vindas! Fique à vontade para abrir issues ou pull requests.
