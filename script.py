import os
import platform
import psutil
import json

bytes_in_gb = 1024**3

mem = psutil.virtual_memory()
mem_total=round(mem[0]/bytes_in_gb,1)

sys_drive = os.getenv('SystemDrive', '/')
drive = psutil.disk_usage(f'{sys_drive}')
drive_total = round(drive[0]/bytes_in_gb,1)
drive_free = round(drive[2]/bytes_in_gb,1)

result = {
    'os_info' : {
        'os': platform.system(),
        'os_release': platform.release(),
        'os_version': platform.platform(),
        'os_architecture': platform.machine(),
        'file_system_type': psutil.disk_partitions()[0][2]
    },
    'hardware_stats' : {
        'cpu_count': os.cpu_count(),
        'ram': f'{mem_total} GB',
        'drive_total': f'{drive_total} GB',
        'drive_free': f'{drive_free} GB'
    }
}

with open('output_json','w') as f:
    json.dump(result,f, indent = 4)