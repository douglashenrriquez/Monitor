# Monitor del Sistema - Django + Psutil

## Descripción del Proyecto
Aplicación web desarrollada con Django que permite monitorear en tiempo real el estado del sistema, incluyendo el uso del CPU, memoria RAM, almacenamiento en disco y otros recursos del sistema utilizando la librería `psutil`.

## Características
- **Monitoreo en tiempo real** de recursos del sistema
- **Interfaz web responsive** y moderna
- **Actualización manual y automática** de datos
- **Detección automática de Windows 11**
- **Métricas incluidas**:
  - Uso de CPU (porcentaje, núcleos, frecuencia)
  - Memoria RAM (uso, total, porcentaje)
  - Almacenamiento en disco (uso, libre, total)
  - Información del sistema operativo
  - Estadísticas de red
  - Número de procesos activos

## Requisitos del Sistema
- Python 3.8+
- Django 4.2+
- Psutil 5.9+

## Instalación y Ejecución

### 1. Clonar o descargar el proyecto
https://github.com/douglashenrriquez/Monitor.git

### 2. Instalar dependencias
pip install -r requirements.txt

### 3. Ejecución de la Aplicación
python manage.py runserver
