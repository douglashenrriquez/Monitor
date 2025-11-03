import psutil
import platform
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def get_system_info():
    try:
        # Información del CPU
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_cores = psutil.cpu_count(logical=False)
        cpu_threads = psutil.cpu_count(logical=True)
        cpu_freq = psutil.cpu_freq()
        
        # Información de memoria RAM
        memory = psutil.virtual_memory()
        memory_total_gb = round(memory.total / (1024 ** 3), 2)
        memory_used_gb = round(memory.used / (1024 ** 3), 2)
        memory_percent = memory.percent
        
        # Información del disco
        disk = psutil.disk_usage('/')
        disk_total_gb = round(disk.total / (1024 ** 3), 2)
        disk_used_gb = round(disk.used / (1024 ** 3), 2)
        disk_free_gb = round(disk.free / (1024 ** 3), 2)
        disk_percent = disk.percent
        
        # Información del sistema operativo (con detección de Windows 11)
        if platform.system() == "Windows":
            # Detectar Windows 11 (build number >= 22000)
            if platform.release() == "10" and int(platform.version().split('.')[2]) >= 22000:
                os_info = "Windows 11"
            else:
                os_info = f"Windows {platform.release()}"
        else:
            os_info = f"{platform.system()} {platform.release()}"
        
        # Información de red
        network = psutil.net_io_counters()
        network_sent_mb = round(network.bytes_sent / (1024 ** 2), 2)
        network_recv_mb = round(network.bytes_recv / (1024 ** 2), 2)
        
        # Información de procesos
        processes = len(psutil.pids())
        
        # Temperatura (si está disponible)
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                cpu_temp = list(temps.values())[0][0].current
            else:
                cpu_temp = "N/A"
        except:
            cpu_temp = "N/A"
        
        system_info = {
            'cpu': {
                'percent': cpu_percent,
                'cores': cpu_cores,
                'threads': cpu_threads,
                'frequency': round(cpu_freq.current, 2) if cpu_freq else 'N/A',
                'temperature': cpu_temp,
            },
            'memory': {
                'total_gb': memory_total_gb,
                'used_gb': memory_used_gb,
                'percent': memory_percent,
            },
            'disk': {
                'total_gb': disk_total_gb,
                'used_gb': disk_used_gb,
                'free_gb': disk_free_gb,
                'percent': disk_percent,
            },
            'system': {
                'os': os_info,
                'platform': platform.platform(),
                'architecture': platform.architecture()[0],
                'version': platform.version(),
            },
            'network': {
                'sent_mb': network_sent_mb,
                'recv_mb': network_recv_mb,
            },
            'processes': processes,
            'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        
        return system_info
        
    except Exception as e:
        # Manejo de errores
        return {
            'error': f"No se pudo obtener la información del sistema: {str(e)}",
            'cpu': {'percent': 0, 'cores': 0, 'threads': 0, 'frequency': 0, 'temperature': 'N/A'},
            'memory': {'total_gb': 0, 'used_gb': 0, 'percent': 0},
            'disk': {'total_gb': 0, 'used_gb': 0, 'free_gb': 0, 'percent': 0},
            'system': {'os': 'N/A', 'platform': 'N/A', 'architecture': 'N/A', 'version': 'N/A'},
            'network': {'sent_mb': 0, 'recv_mb': 0},
            'processes': 0,
            'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

def index(request):
    """Vista principal que muestra el dashboard de monitoreo"""
    system_info = get_system_info()
    context = {
        'system_info': system_info,
        'has_error': 'error' in system_info,
        'current_time': system_info.get('current_time', 'N/A'),
    }
    return render(request, 'sistema/index.html', context)

def api_system_info(request):
    """API endpoint para obtener información del sistema en formato JSON"""
    system_info = get_system_info()
    return JsonResponse(system_info)