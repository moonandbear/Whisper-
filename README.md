# Whisper-
基于 PyTorch 和 Whisper 的本地语音识别系统，支持 CUDA 加速，输出标准 .srt 字幕文件。


Whisper Subtitle Generator (GPU-Accelerated, Local Deployment)

本项目基于 [OpenAI Whisper](https://github.com/openai/whisper)，实现本地部署的语音转写和字幕 (.srt) 生成工具，支持 **PyTorch GPU 加速**，适用于多种自动字幕生成场景。

> 技术栈：Python + PyTorch + CUDA + Whisper  
>  环境依赖已适配本地部署，显著加快推理速度  



项目结构
.
├── whisper_transcribe.py     # 主程序：从音频生成字幕
├── check_gpu.py              # 可选工具：检测 CUDA 和显存状态
├── requirements.txt          # pip 安装依赖（可选）
├── environment.yml           # conda 环境配置（可选）
└── samples/                  # 输入音频和输出字幕示例（可选）
