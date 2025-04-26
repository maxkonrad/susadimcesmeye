import yt_dlp
import os

def download_audio(url, output_folder):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    input_file = 'urls.txt'  # Text file containing YouTube URLs
    output_folder = 'downloads'  # Output folder for MP3 files
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    with open(input_file, 'r') as file:
        for line in file:
            url = line.strip()
            if url:
                print(f'Downloading: {url}')
                download_audio(url, output_folder)
    
    print('All downloads completed!')

if __name__ == '__main__':
    main()
