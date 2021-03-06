from ffmpy import FFmpeg


class TranscoderWrapper:

    def __init__(self, source_dir: str, dest_dir: str):
        self.source = source_dir
        self.dest = dest_dir

    def transcode(self):
        ff = FFmpeg(
            inputs={self.source: None},
            outputs={self.dest: '-c:v copy -c:a copy -flvflags add_keyframe_index'}
        )
        ff.run()
