from downloader import download_youtube_video
from video_splitter import split_video
from tiktok_converter import process_clips_to_tiktok_format

if __name__ == "__main__":
    url = input("Colle le lien YouTube ici : ").strip()
    try:
        # Télécharger la vidéo YouTube
        video_path = download_youtube_video(url)
        print(f"✅ Vidéo téléchargée : {video_path}")

        # Diviser la vidéo en clips
        clips = split_video(video_path, output_dir="clips")
        print(f"✅ Vidéo découpée en {len(clips)} clips:")
        for clip in clips:
            print(" -", clip)

        process_clips_to_tiktok_format("clips", "tiktok_clips")
        print("✅ Conversion des clips en format TikTok terminée.")

    except Exception as e:
        print("❌ Une erreur est survenue :", e)
