import yt_dlp
import re


def download_youtube_as_mp3(youtube_url):
    with yt_dlp.YoutubeDL() as ydl:
        video_info = ydl.extract_info(youtube_url, download=False)
        video_title = video_info.get['title', 'Unknown Title']
        video_uploader = video_info.get('uploader', 'Unknown Author')

        safe_filename = re.sub(
            r'[^\w\s-]', '', f"{video_title} - {video_uploader}")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f"{safe_filename}",
        }

        ydl = yt_dlp.YoutubeDL(ydl_opts)
        ydl.download([youtube_url])

        return safe_filename


# youtube_url = "https://www.youtube.com/watch?v=aYcxqX6hgyg"

youtube_url = input('Please enter youtube URL: ')

file_name = download_youtube_as_mp3(youtube_url)
print(f"File saved as: {file_name}.mp3")
