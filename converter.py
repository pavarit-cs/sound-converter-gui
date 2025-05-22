from pydub import AudioSegment
import os

def convert_audio_file(input_path, output_path, output_format):
    """
        Function for Convert file
        return True -> success
        return False -> fail
    """
    if not os.path.exists(input_path):
        return False, f"INVALID : Not found file at {input_path}"
    try :
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format=output_format)
        return True, "Convert file success"
    except FileNotFoundError:
        return False, "INVALID : Can't connect FFmpeg"
    except Exception as e:
        return False, f"INVALID : {e}"

