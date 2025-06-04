from downloader import download_youtube_video
from video_splitter import split_video

if __name__ == "__main__":
    url = input("Colle le lien YouTube ici : ").strip()
    try:
        video_path = download_youtube_video(url)
        print(f"✅ Vidéo téléchargée : {video_path}")

        clips = split_video(video_path, output_dir="clips")
        print(f"✅ Vidéo découpée en {len(clips)} clips:")
        for clip in clips:
            print(" -", clip)
    except Exception as e:
        print("❌ Une erreur est survenue :", e)
