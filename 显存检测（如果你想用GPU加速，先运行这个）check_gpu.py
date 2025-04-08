import torch

# 查看 CUDA 设备信息
if torch.cuda.is_available():
    print(f"CUDA Device Count: {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"Device {i}: {torch.cuda.get_device_name(i)}")
        print(f"  Memory Allocated: {torch.cuda.memory_allocated(i) / (1024 ** 3):.2f} GB")
        print(f"  Memory Cached: {torch.cuda.memory_reserved(i) / (1024 ** 3):.2f} GB")
        print(f"  Total Memory: {torch.cuda.get_device_properties(i).total_memory / (1024 ** 3):.2f} GB")
else:
    print("CUDA is not available.")
