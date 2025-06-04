import os
import ffmpeg

def convert_to_tiktok_format(input_path, output_path):
    try:
        # Get video information
        probe = ffmpeg.probe(input_path)
        video_info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')

        width = int(video_info['width'])
        height = int(video_info['height'])

        # Calculate scaling and padding to fit 9:16 aspect ratio
        target_width = 1080
        target_height = 1920

        # Calculate the scaling factor to fit within the target dimensions
        scale_factor = min(target_width / width, target_height / height)
        scaled_width = int(width * scale_factor)
        scaled_height = int(height * scale_factor)

        # Calculate padding to center the video
        pad_x = (target_width - scaled_width) // 2
        pad_y = (target_height - scaled_height) // 2

        # Apply scaling and padding
        input_stream = ffmpeg.input(input_path)
        scaled = input_stream.filter('scale', scaled_width, scaled_height)
        padded = scaled.filter('pad', target_width, target_height, pad_x, pad_y, color='black')

        # Output the video with the desired settings
        (
            ffmpeg
            .output(padded, output_path, vcodec='libx264', acodec='aac', r=30, pix_fmt='yuv420p')
            .run(overwrite_output=True, quiet=True)
        )
    except ffmpeg.Error as e:
        print(f"An error occurred during conversion: {e.stderr.decode('utf8')}")
        raise

def process_clips_to_tiktok_format(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".mp4"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"tiktok_{filename}")

            convert_to_tiktok_format(input_path, output_path)
