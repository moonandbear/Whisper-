import whisper
import os
import datetime

# ============ 配置 =============
video_path = r"C:\Users\15259\Videos\pijiu.wav"  # 视频文件路径
output_srt_path = r"C:\Users\15259\Videos\888啤酒节.srt"  # 输出的字幕路径
model_size = "small"  # 可选 tiny / base / small / medium / large
language = None  # 设置为 None 表示自动检测
# ===============================

# 工具函数：将秒转为 SRT 时间戳格式
def format_timestamp(seconds: float):
    td = datetime.timedelta(seconds=round(seconds, 3))
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = int((td.total_seconds() - total_seconds) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

# 加载模型
print(f"🔍 正在加载 Whisper 模型 ({model_size}) ...")
model = whisper.load_model(model_size)
print("✅ 模型加载完成。")

# 开始转录
print(f"🎧 开始处理音频文件：{video_path}")
result = model.transcribe(video_path, language=language)
print("✅ 转录完成。正在生成字幕文件...")

# 写入 .srt 字幕文件
with open(output_srt_path, "w", encoding="utf-8") as f:
    for i, segment in enumerate(result["segments"]):
        start = format_timestamp(segment["start"])
        end = format_timestamp(segment["end"])
        text = segment["text"].strip()
        f.write(f"{i+1}\n{start} --> {end}\n{text}\n\n")

print(f"✅ 字幕文件已保存到：{output_srt_path}")
