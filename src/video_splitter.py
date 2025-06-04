import os
import math
import ffmpeg

def split_video(input_path, output_dir="clips", chunk_duration=60):
    os.makedirs(output_dir, exist_ok=True)

    # Récupérer la durée totale de la vidéo
    probe = ffmpeg.probe(input_path)
    duration = float(probe['format']['duration'])
    total_chunks = math.ceil(duration / chunk_duration)

    clips = []

    for i in range(total_chunks):
        start_time = i * chunk_duration
        output_path = os.path.join(output_dir, f"clip_{i+1}.mp4")

        (
            ffmpeg
            .input(input_path, ss=start_time, t=chunk_duration)
            .output(output_path, vcodec='copy', acodec='aac', strict='experimental')
            .run(quiet=True, overwrite_output=True)
        )

        clips.append(output_path)


    return clips
