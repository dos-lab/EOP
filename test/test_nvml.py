from py3nvml import py3nvml
py3nvml.nvmlInit()
handle = py3nvml.nvmlDeviceGetHandleByIndex(0)#0就是GPU idx
meminfo = py3nvml.nvmlDeviceGetMemoryInfo(handle)
print(meminfo.used)
