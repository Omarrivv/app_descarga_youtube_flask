from flask import Flask, request, redirect, url_for, render_template, send_from_directory, session
from pytube import YouTube
from moviepy.editor import VideoFileClip
from os.path import splitext, join
import os, threading, secrets
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Necesario para usar sesiones
DOWNLOAD_FOLDER = 'downloads'
AUDIO_FOLDER = 'audio'
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['AUDIO_FOLDER'] = AUDIO_FOLDER
# Ruta para la página principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_link = request.form['videoURL']
        if video_link and ("youtube.com" in video_link or "youtu.be" in video_link):
            try:
                yt = YouTube(video_link)
                video = yt.streams.get_highest_resolution()
                if not os.path.exists(DOWNLOAD_FOLDER):
                    os.makedirs(DOWNLOAD_FOLDER)
                video.download(output_path=DOWNLOAD_FOLDER)
                filename = video.default_filename
                session['filename'] = filename  # Almacenar el nombre del archivo en la sesión
                return redirect(url_for('options'))
            except Exception as e:
                return f"Error al descargar el video: {e}"
        else:
            return "URL inválida. Por favor, inserte un enlace válido de YouTube."
    return render_template('index.html')
# Ruta para mostrar opciones después de la descarga
@app.route('/options')
def options():
    filename = session.get('filename', None)
    if filename:
        return render_template('options.html', filename=filename)
    return redirect(url_for('index'))
# Ruta para descargar el archivo de video
@app.route('/downloads/<filename>')
def downloaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)
# Ruta para convertir a audio y descargar
@app.route('/convert_to_audio/<filename>', methods=['GET'])
def download_audio(filename):
    video_path = join(app.config['DOWNLOAD_FOLDER'], filename)
    audio_path = convert_to_audio(video_path)
    return send_from_directory(app.config['AUDIO_FOLDER'], os.path.basename(audio_path), as_attachment=True)

def convert_to_audio(video_path):
    if not os.path.exists(app.config['AUDIO_FOLDER']):
        os.makedirs(app.config['AUDIO_FOLDER'])
    video = VideoFileClip(video_path)
    audio = video.audio
    output_path = f"{app.config['AUDIO_FOLDER']}/{splitext(os.path.basename(video_path))[0]}.mp3"
    audio.write_audiofile(output_path)
    audio.close()
    video.close()
    return output_path
if __name__ == '__main__':
    app.run(debug=True)