import os
import math
import ffmpeg

def split_video(input_path, output_dir="clips", chunk_duration=60):
    os.makedirs(output_dir, exist_ok=True)

    # Obtenir la durée totale de la vidéo
    probe = ffmpeg.probe(input_path)
    duration = float(probe['format']['duration'])
    total_chunks = math.ceil(duration / chunk_duration)

    clips = []

    for i in range(total_chunks):
        start_time = i * chunk_duration
        output_path = os.path.join(output_dir, f"clip_{i+1}.mp4")

        # Calculer la durée réelle du chunk actuel
        actual_chunk_duration = min(chunk_duration, duration - start_time)

        # Traiter le chunk uniquement si sa durée est de 30 secondes ou plus
        if actual_chunk_duration >= 30:
            (
                ffmpeg
                .input(input_path, ss=start_time, t=actual_chunk_duration)
                .output(output_path, vcodec='copy', acodec='aac', strict='experimental')
                .run(quiet=True, overwrite_output=True)
            )
            clips.append(output_path)
        else:
            print(f"Ignorer le clip {i+1} car sa durée est inférieure à 30 secondes.")

    return clips