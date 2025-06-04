import os
import math
import ffmpeg

def split_video(input_path, output_dir="clips", chunk_duration=60):
    os.makedirs(output_dir, exist_ok=True)

    # Get the total duration of the video
    probe = ffmpeg.probe(input_path)
    duration = float(probe['format']['duration'])
    total_chunks = math.ceil(duration / chunk_duration)

    clips = []

    for i in range(total_chunks):
        start_time = i * chunk_duration
        output_path = os.path.join(output_dir, f"clip_{i+1}.mp4")

        # Calculate the actual duration of the current chunk
        actual_chunk_duration = min(chunk_duration, duration - start_time)

        # Only process the chunk if its duration is 30 seconds or more
        if actual_chunk_duration >= 30:
            (
                ffmpeg
                .input(input_path, ss=start_time, t=actual_chunk_duration)
                .output(output_path, vcodec='copy', acodec='aac', strict='experimental')
                .run(quiet=True, overwrite_output=True)
            )
            clips.append(output_path)
        else:
            print(f"Skipping clip {i+1} as its duration is less than 30 seconds.")

    return clips