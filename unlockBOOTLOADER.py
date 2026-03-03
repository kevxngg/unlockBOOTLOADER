#!/usr/bin/env python3
"""
unlockBOOTLOADER - Xiaomi Bootloader Unlock Request Optimizer
Author: kevxngg (GitHub/Facebook/Instagram/Telegram: @kevxngg)
Description: Automated tool for Xiaomi bootloader unlock request timing optimization
License: MIT
Repository: https://github.com/kevxngg/unlockBOOTLOADER
Version: 2.1.0
"""

import subprocess
import sys
import os
import hashlib
import random
import time
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta
from typing import Optional, Tuple

# ============================================================================
# FIX: Asegurar que trabajamos en el directorio del script
# ============================================================================

# Obtener el directorio donde está el script
SCRIPT_DIR = Path(__file__).parent.resolve()

# Cambiar al directorio del script
os.chdir(SCRIPT_DIR)

print(f"📁 Directorio de trabajo: {SCRIPT_DIR}\n")

# ============================================================================
# INSTALACIÓN AUTOMÁTICA DE DEPENDENCIAS
# ============================================================================

def install_package(package: str) -> bool:
    """Instala un paquete de Python usando pip de forma silenciosa"""
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package, "--quiet"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        return False

# Dependencias necesarias
REQUIRED_PACKAGES = ["ntplib", "pytz", "urllib3", "colorama"]
for package in REQUIRED_PACKAGES:
    try:
        __import__(package)
    except ImportError:
        print(f"📦 Instalando {package}...")
        if not install_package(package):
            print(f"❌ Error instalando {package}. Instálalo manualmente: pip install {package}")
            sys.exit(1)

os.system('cls' if os.name == 'nt' else 'clear')

import ntplib
import pytz
import urllib3
from colorama import init, Fore, Style

# ============================================================================
# CONFIGURACIÓN GLOBAL
# ============================================================================

# Colores
init(autoreset=True)
COL_G = Fore.GREEN
COL_Y = Fore.YELLOW
COL_B = Fore.BLUE
COL_R = Fore.RED
COL_C = Fore.CYAN
COL_M = Fore.MAGENTA

# Constantes
SCRIPT_VERSION = "OPTIMIZED_v2.1_PATH_FIX"
API_BASE_URL = "https://sgp-api.buy.mi.com/bbs/api/global"

# RUTAS ABSOLUTAS basadas en la ubicación del script
TOKEN_FILE = SCRIPT_DIR / "token.txt"
TIMESHIFT_FILE = SCRIPT_DIR / "timeshift.txt"

# Servidores NTP ordenados por velocidad y confiabilidad
NTP_SERVERS = [
    "time.google.com",
    "time.cloudflare.com",
    "time.windows.com",
    "pool.ntp.org",
    "time.nist.gov"
]

# ============================================================================
# FUNCIONES AUXILIARES
# ============================================================================

def clear_screen():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Muestra el encabezado del script"""
    print(f"{COL_C}{'='*70}")
    print(f"{COL_M}  🔓 XIAOMI BOOTLOADER UNLOCK REQUEST OPTIMIZER v2.1")
    print(f"{COL_C}{'='*70}{Fore.RESET}\n")

def print_separator():
    """Imprime un separador visual"""
    print(f"{COL_C}{'-'*70}{Fore.RESET}")

def read_config_line(file_path: Path, line_number: int) -> Optional[str]:
    """Lee una línea específica de un archivo de configuración"""
    try:
        if not file_path.exists():
            print(f"{COL_R}❌ Archivo no encontrado: {file_path}{Fore.RESET}")
            print(f"{COL_Y}💡 Asegúrate de que el archivo esté en: {file_path.parent}{Fore.RESET}")
            return None
        
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if line_number > len(lines):
                print(f"{COL_R}❌ Línea {line_number} no existe en {file_path.name}{Fore.RESET}")
                print(f"{COL_Y}💡 El archivo solo tiene {len(lines)} línea(s){Fore.RESET}")
                return None
            return lines[line_number - 1].strip()
    except Exception as e:
        print(f"{COL_R}❌ Error leyendo {file_path.name}: {e}{Fore.RESET}")
        return None

def generate_device_id() -> str:
    """Genera un Device ID aleatorio único"""
    random_data = f"{random.random()}-{time.time()}-{random.randint(1000, 9999)}"
    return hashlib.sha1(random_data.encode('utf-8')).hexdigest().upper()

# ============================================================================
# SINCRONIZACIÓN NTP
# ============================================================================

def get_ntp_time() -> Optional[datetime]:
    """
    Obtiene la hora exacta de Pekín mediante NTP
    Prueba múltiples servidores para mayor confiabilidad
    """
    client = ntplib.NTPClient()
    beijing_tz = pytz.timezone("Asia/Shanghai")
    
    for server in NTP_SERVERS:
        try:
            print(f"{COL_Y}⏱️  Sincronizando con {server}...{Fore.RESET}", end=' ')
            response = client.request(server, version=3, timeout=3)
            ntp_time = datetime.fromtimestamp(response.tx_time, timezone.utc)
            beijing_time = ntp_time.astimezone(beijing_tz)
            
            # Calcular precisión aproximada
            delay_ms = response.delay * 1000
            print(f"{COL_G}✓ (latencia: {delay_ms:.1f}ms){Fore.RESET}")
            print(f"{COL_G}📅 Hora Pekín: {beijing_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}{Fore.RESET}")
            
            return beijing_time
        except Exception as e:
            print(f"{COL_R}✗ ({str(e)[:30]}){Fore.RESET}")
            continue
    
    print(f"{COL_R}❌ Error crítico: No se pudo sincronizar con ningún servidor NTP{Fore.RESET}")
    return None

def get_synchronized_time(start_time: datetime, start_timestamp: float) -> datetime:
    """Calcula la hora actual basándose en la sincronización inicial"""
    elapsed = time.time() - start_timestamp
    return start_time + timedelta(seconds=elapsed)

# ============================================================================
# SESIÓN HTTP OPTIMIZADA
# ============================================================================

class OptimizedHTTPSession:
    """
    Sesión HTTP/1.1 optimizada para requests de alta velocidad
    Características:
    - Keep-Alive persistente
    - Timeouts agresivos
    - Pool de conexiones precalentadas
    - Sin auto-retry (control manual)
    """
    
    def __init__(self):
        # Timeouts ultra-agresivos: 1.5s connect, 2s read
        self.http = urllib3.PoolManager(
            maxsize=10,
            retries=urllib3.Retry(total=0),  # Sin auto-retry
            timeout=urllib3.Timeout(connect=1.5, read=2.0),
            headers={'Connection': 'keep-alive'}
        )
    
    def make_request(self, method: str, url: str, headers: dict = None, body: bytes = None):
        """
        Realiza una petición HTTP con manejo de timeouts
        Retorna: response object, "TIMEOUT", o None
        """
        try:
            req_headers = headers or {}
            req_headers['Content-Type'] = 'application/json; charset=utf-8'
            
            if method == 'POST':
                if body is None:
                    body = b'{"is_retry":true}'
                req_headers.update({
                    'Content-Length': str(len(body)),
                    'Accept-Encoding': 'gzip, deflate',
                    'User-Agent': 'okhttp/4.12.0',
                    'Connection': 'keep-alive'
                })
            
            response = self.http.request(
                method, 
                url, 
                headers=req_headers, 
                body=body, 
                preload_content=False
            )
            return response
            
        except urllib3.exceptions.ReadTimeoutError:
            return "TIMEOUT"
        except Exception as e:
            return None

# ============================================================================
# VALIDACIÓN DE CUENTA
# ============================================================================

def check_unlock_status(session: OptimizedHTTPSession, cookie: str, device_id: str) -> bool:
    """
    Verifica el estado de elegibilidad de la cuenta
    Retorna True si se puede continuar, False si debe salir
    """
    try:
        url = f"{API_BASE_URL}/user/bl-switch/state"
        headers = {
            "Cookie": f"new_bbs_serviceToken={cookie};versionCode=500411;versionName=5.4.11;deviceId={device_id};"
        }
        
        print(f"{COL_Y}🔍 Consultando estado de la cuenta...{Fore.RESET}")
        response = session.make_request('GET', url, headers=headers)
        
        if not response or response == "TIMEOUT":
            print(f"{COL_R}❌ Error de conexión al verificar estado{Fore.RESET}")
            return False

        response_data = json.loads(response.data.decode('utf-8'))
        response.release_conn()

        code = response_data.get("code")
        
        # Token inválido o expirado
        if code == 100004:
            print(f"{COL_R}❌ Token caducado o inválido{Fore.RESET}")
            print(f"{COL_Y}💡 Obtén un nuevo token desde la web de Xiaomi{Fore.RESET}")
            return False

        data = response_data.get("data", {})
        is_pass = data.get("is_pass")
        button_state = data.get("button_state")
        deadline = data.get("deadline_format", "")

        print_separator()
        
        # Ya desbloqueado previamente
        if is_pass == 1:
            print(f"{COL_G}✓ Desbloqueo ya autorizado hasta: {deadline}{Fore.RESET}")
            print(f"{COL_Y}💡 Tu cuenta ya tiene permiso de desbloqueo{Fore.RESET}")
            return False
        
        # Elegible para solicitud
        elif is_pass == 4:
            if button_state == 1:
                print(f"{COL_G}✓ Cuenta elegible para solicitar desbloqueo{Fore.RESET}")
                print_separator()
                return True
            else:
                print(f"{COL_Y}⚠️  Bloqueo temporal activo hasta: {deadline}{Fore.RESET}")
                force = input(f"{COL_Y}¿Intentar de todos modos? (s/n): {Fore.RESET}").lower()
                return force == 's'
        
        # Otros estados
        else:
            print(f"{COL_Y}⚠️  Estado desconocido: is_pass={is_pass}{Fore.RESET}")
            print(f"{COL_Y}Respuesta completa: {response_data}{Fore.RESET}")
            force = input(f"{COL_Y}¿Continuar de todos modos? (s/n): {Fore.RESET}").lower()
            return force == 's'

    except Exception as e:
        print(f"{COL_R}❌ Error al verificar estado: {e}{Fore.RESET}")
        return False

# ============================================================================
# ESPERA SINCRONIZADA
# ============================================================================

def wait_until_target_time(start_time: datetime, start_timestamp: float, feed_shift: float):
    """
    Espera hasta el momento exacto objetivo (00:00:00 - feed_shift)
    Muestra countdown en tiempo real
    """
    # Calcular el próximo día a las 00:00:00
    next_day = start_time + timedelta(days=1)
    target_time = next_day.replace(hour=0, minute=0, second=0, microsecond=0)
    target_time -= timedelta(seconds=feed_shift)
    
    print(f"\n{COL_C}{'='*70}{Fore.RESET}")
    print(f"{COL_Y}⏳ CONFIGURACIÓN DE TIMING{Fore.RESET}")
    print(f"{COL_C}{'='*70}{Fore.RESET}")
    print(f"{COL_G}📍 Desfase de red: {feed_shift*1000:.2f} ms{Fore.RESET}")
    print(f"{COL_G}🎯 Hora objetivo:  {target_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}{Fore.RESET}")
    print(f"{COL_C}{'='*70}{Fore.RESET}\n")
    
    print(f"{COL_Y}⏰ Esperando momento crítico... (mantén esta ventana abierta){Fore.RESET}\n")
    
    last_print = 0
    while True:
        current_time = get_synchronized_time(start_time, start_timestamp)
        time_diff = target_time - current_time
        seconds_left = time_diff.total_seconds()
        
        # Mostrar countdown cada segundo
        if seconds_left > 2 and int(seconds_left) != last_print:
            last_print = int(seconds_left)
            hours = int(seconds_left // 3600)
            minutes = int((seconds_left % 3600) // 60)
            secs = int(seconds_left % 60)
            print(f"\r{COL_Y}⏱️  Tiempo restante: {hours:02d}:{minutes:02d}:{secs:02d}  {Fore.RESET}", end='', flush=True)
        
        # Ajustar sleep según cercanía al objetivo
        if seconds_left > 60:
            time.sleep(5)  # Lejos: sleep largo
        elif seconds_left > 10:
            time.sleep(1)  # Medio: 1 segundo
        elif seconds_left > 0.1:
            time.sleep(0.01)  # Cerca: 10ms
        elif current_time >= target_time:
            print(f"\r{COL_G}🚀 ¡MOMENTO CRÍTICO ALCANZADO!{' '*50}{Fore.RESET}")
            break

# ============================================================================
# BOMBARDEO DE REQUESTS
# ============================================================================

def execute_unlock_requests(session: OptimizedHTTPSession, cookie: str, device_id: str, 
                           start_time: datetime, start_timestamp: float) -> bool:
    """
    Ejecuta ráfagas de peticiones de desbloqueo
    Retorna True si tuvo éxito, False si no
    """
    url = f"{API_BASE_URL}/apply/bl-auth"
    headers = {
        "Cookie": f"new_bbs_serviceToken={cookie};versionCode=500411;versionName=5.4.11;deviceId={device_id};"
    }
    
    print(f"\n{COL_C}{'='*70}{Fore.RESET}")
    print(f"{COL_Y}🔥 INICIANDO RÁFAGA DE PETICIONES{Fore.RESET}")
    print(f"{COL_C}{'='*70}{Fore.RESET}\n")
    
    attempt = 0
    success = False
    
    try:
        while True:
            attempt += 1
            response = session.make_request('POST', url, headers=headers)
            
            # Timeout - reintento inmediato
            if response == "TIMEOUT":
                print(f"{COL_R}[{attempt:03d}] ⏱️  Timeout - Reintentando...{Fore.RESET}")
                continue
            
            # Error de conexión - reintento
            if response is None:
                print(f"{COL_R}[{attempt:03d}] ❌ Error de conexión - Reintentando...{Fore.RESET}")
                time.sleep(0.1)
                continue
            
            # Respuesta recibida - procesar
            response_time = get_synchronized_time(start_time, start_timestamp)
            print(f"{COL_G}[{attempt:03d}] ✓ Respuesta a las: {response_time.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}")
            
            try:
                raw_data = response.data
                response.release_conn()
                json_data = json.loads(raw_data.decode('utf-8'))
                code = json_data.get("code")
                data = json_data.get("data", {})
                
                # ÉXITO - Autorización concedida
                if code == 0:
                    result = data.get("apply_result")
                    
                    if result == 1:
                        print(f"\n{COL_G}{'='*70}")
                        print(f"  🎉 ¡AUTORIZACIÓN CONCEDIDA!")
                        print(f"{'='*70}{Fore.RESET}\n")
                        success = True
                        break
                    
                    elif result in [3, 4]:
                        deadline = data.get("deadline_format", "Indefinido")
                        print(f"\n{COL_Y}⚠️  Cuota global agotada{Fore.RESET}")
                        print(f"{COL_Y}📅 Próximo intento disponible: {deadline}{Fore.RESET}")
                        break
                
                # Código 100003 - Verificar estado asíncrono
                elif code == 100003:
                    print(f"{COL_Y}🔄 Código 100003 - Verificando autorización asíncrona...{Fore.RESET}")
                    time.sleep(1)
                    if check_unlock_status(session, cookie, device_id):
                        success = True
                    break
                
                # Código inesperado
                else:
                    print(f"{COL_R}⚠️  Código API inesperado: {code}{Fore.RESET}")
                    print(f"{COL_Y}Respuesta: {json_data}{Fore.RESET}")
                    break
                
            except json.JSONDecodeError as e:
                print(f"{COL_R}❌ Error decodificando respuesta: {e}{Fore.RESET}")
                continue
            except Exception as e:
                print(f"{COL_R}❌ Error procesando respuesta: {e}{Fore.RESET}")
                continue
    
    except KeyboardInterrupt:
        print(f"\n{COL_Y}⚠️  Interrumpido por el usuario{Fore.RESET}")
        return False
    
    return success

# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """Función principal del script"""
    
    # Mostrar encabezado
    print_header()
    
    # Verificar y mostrar rutas de archivos
    print(f"{COL_B}📂 Buscando archivos de configuración en:{Fore.RESET}")
    print(f"   {SCRIPT_DIR}\n")
    print_separator()
    
    # Validar archivos de configuración
    if not TOKEN_FILE.exists():
        print(f"{COL_R}❌ No se encontró: {TOKEN_FILE.name}{Fore.RESET}")
        print(f"{COL_Y}💡 Crea el archivo token.txt en la misma carpeta que el script{Fore.RESET}")
        print(f"{COL_Y}💡 Ruta completa: {TOKEN_FILE}{Fore.RESET}")
        return
    else:
        print(f"{COL_G}✓ Encontrado: {TOKEN_FILE.name}{Fore.RESET}")
    
    if not TIMESHIFT_FILE.exists():
        print(f"{COL_R}❌ No se encontró: {TIMESHIFT_FILE.name}{Fore.RESET}")
        print(f"{COL_Y}💡 Crea el archivo timeshift.txt en la misma carpeta que el script{Fore.RESET}")
        print(f"{COL_Y}💡 Ruta completa: {TIMESHIFT_FILE}{Fore.RESET}")
        return
    else:
        print(f"{COL_G}✓ Encontrado: {TIMESHIFT_FILE.name}{Fore.RESET}")
    
    print_separator()
    print()
    
    # Solicitar número de línea del token
    try:
        token_number = int(input(f"{COL_G}📋 Número de línea del token: {Fore.RESET}"))
        if token_number < 1:
            raise ValueError("Debe ser mayor a 0")
    except (ValueError, KeyboardInterrupt):
        print(f"\n{COL_R}❌ Número inválido{Fore.RESET}")
        return
    
    clear_screen()
    print_header()
    print(f"{COL_M}📌 Token #{token_number}{Fore.RESET}\n")
    print_separator()
    
    # Leer configuración
    token = read_config_line(TOKEN_FILE, token_number)
    if not token:
        print(f"{COL_R}❌ No se pudo leer el token (línea {token_number}){Fore.RESET}")
        return
    
    timeshift_str = read_config_line(TIMESHIFT_FILE, token_number)
    if not timeshift_str:
        print(f"{COL_R}❌ No se pudo leer el timeshift (línea {token_number}){Fore.RESET}")
        return
    
    try:
        feedtime_ms = float(timeshift_str)
        feed_shift = feedtime_ms / 1000  # Convertir a segundos
    except ValueError:
        print(f"{COL_R}❌ Timeshift inválido: '{timeshift_str}'{Fore.RESET}")
        return
    
    print(f"{COL_G}✓ Configuración cargada correctamente{Fore.RESET}")
    print_separator()
    
    # Generar Device ID
    device_id = generate_device_id()
    print(f"{COL_B}🔑 Device ID: {device_id[:16]}...{Fore.RESET}\n")
    
    # Crear sesión HTTP
    session = OptimizedHTTPSession()
    
    # Verificar estado de la cuenta
    if not check_unlock_status(session, token, device_id):
        return
    
    # Sincronizar hora NTP
    print(f"\n{COL_Y}⏱️  SINCRONIZACIÓN NTP{Fore.RESET}")
    print_separator()
    start_time = get_ntp_time()
    if not start_time:
        return
    
    start_timestamp = time.time()
    print_separator()
    
    # Precalentamiento TLS
    print(f"\n{COL_Y}🔥 PRECALENTAMIENTO DE CONEXIÓN{Fore.RESET}")
    print_separator()
    print(f"{COL_Y}🌐 Estableciendo túnel TLS con {API_BASE_URL.split('/')[2]}...{Fore.RESET}")
    
    warmup_url = f"{API_BASE_URL}/user/bl-switch/state"
    warmup_headers = {"Cookie": f"new_bbs_serviceToken={token};deviceId={device_id};"}
    warmup_response = session.make_request('GET', warmup_url, headers=warmup_headers)
    
    if warmup_response and warmup_response != "TIMEOUT":
        warmup_response.release_conn()
        print(f"{COL_G}✓ Conexión HTTP/1.1 Keep-Alive establecida{Fore.RESET}")
    else:
        print(f"{COL_Y}⚠️  Precalentamiento falló (no crítico){Fore.RESET}")
    
    print_separator()
    
    # Esperar hasta el momento objetivo
    wait_until_target_time(start_time, start_timestamp, feed_shift)
    
    # Ejecutar peticiones
    success = execute_unlock_requests(session, token, device_id, start_time, start_timestamp)
    
    # Verificar estado final
    if success:
        print(f"\n{COL_Y}🔍 Verificando estado final...{Fore.RESET}")
        check_unlock_status(session, token, device_id)

# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{COL_Y}⚠️  Script interrumpido por el usuario{Fore.RESET}")
    except Exception as e:
        print(f"\n{COL_R}❌ Error crítico inesperado: {e}{Fore.RESET}")
        import traceback
        traceback.print_exc()
    finally:
        print(f"\n{COL_C}{'='*70}{Fore.RESET}")
        input(f"{COL_G}✓ Presiona Enter para cerrar...{Fore.RESET}")