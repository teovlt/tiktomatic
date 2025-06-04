from downloader import download_youtube_video

if __name__ == "__main__":
    url = input("Entrez votre vidéo youtube  : ")
    path = download_youtube_video(url)
    print(f"✅ Vidéo téléchargée : {path}")
