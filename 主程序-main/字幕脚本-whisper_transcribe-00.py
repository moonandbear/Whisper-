import whisper
import datetime

# 配置
video_path = r"C:\path\to\audio.wav"  # 更改为音频文件路径
output_srt_path = r"C:\path\to\output.srt"  # 更改为字幕输出路径
model_size = "small"  # 选择适合的模型

# 工具函数：将秒转为 SRT 时间戳格式
def format_timestamp(seconds: float):
    td = datetime.timedelta(seconds=round(seconds, 3))
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = int((td.total_seconds() - total_seconds) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

# 加载模型并转录音频文件
model = whisper.load_model(model_size)
result = model.transcribe(video_path)

# 生成字幕文件
with open(output_srt_path, "w", encoding="utf-8") as f:
    for i, segment in enumerate(result["segments"]):
        f.write(f"{i+1}\n{format_timestamp(segment['start'])} --> {format_timestamp(segment['end'])}\n{segment['text'].strip()}\n\n")
