# 🔓 unlockBOOTLOADER

<div align="center">

![Banner](https://img.shields.io/badge/unlockBOOTLOADER-v2.1.0-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.7+-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-purple?style=for-the-badge)

**Xiaomi Bootloader Unlock Request Timing Optimizer**

*Herramienta automatizada para optimizar el timing de solicitudes de desbloqueo del bootloader*

[🇪🇸 Español](#-español) | [🇬🇧 English](#-english)

</div>

---

## 🇪🇸 Español

### 📖 ¿Qué es unlockBOOTLOADER?

**unlockBOOTLOADER** es una herramienta de línea de comandos que automatiza y optimiza el proceso de solicitud de desbloqueo del bootloader en dispositivos Xiaomi. 

Utiliza:
- ⏰ Sincronización NTP ultra-precisa con servidores atómicos
- 🚀 Optimizaciones de red avanzadas (TLS pre-warming, Keep-Alive)
- 🎯 Timing perfecto para maximizar probabilidades de éxito

### ✨ Características

| Característica | Descripción |
|----------------|-------------|
| 🎯 **Sincronización NTP** | Servidores atómicos: Google, Cloudflare, NIST, Windows |
| ⚡ **Optimización Red** | TLS pre-warming, HTTP/1.1 Keep-Alive, timeouts agresivos |
| 🔥 **Ráfaga Automática** | Múltiples peticiones en el momento exacto (00:00:00 Pekín) |
| 📊 **Countdown Real-Time** | Visualización HH:MM:SS hasta el momento crítico |
| 🎨 **UI Profesional** | Interfaz colorida con emojis y ASCII art |
| 📝 **Logging Detallado** | Timestamps con precisión de milisegundos |
| 🛡️ **Error Handling** | Recuperación automática de fallos de red |
| 📁 **Rutas Automáticas** | Funciona desde cualquier ubicación |

### 🚀 Instalación

#### Requisitos Previos
```bash
- Python 3.7 o superior
- pip (incluido con Python)
- Nevegador Firefox
- Navegador Google Chrome
- Conexión a Internet estable
```

#### Descarga
1. Descarga `unlockBOOTLOADER.zip` desde [Releases](https://github.com/kevxngg/unlockBOOTLOADER/releases)
2. Descomprime el archivo 

### 📝 Guía de Uso Completa

#### Paso 1: Crear Archivos de Configuración

En la **carpeta** que se creo cuando descomprimiste `unlockBOOTLOADER.zip`, crea estos dos archivos:

```
token.txt
timeshift.txt
```

#### Paso 2: Obtener tus Tokens de Sesión

Hay **DOS métodos** para extraer los tokens necesarios:

##### Firefox: Con la extensión Cookie-Editor

1. Abre Firefox e instala la extensión "[Cookie Editor](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)"
   <img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/380832c4-b82c-420d-b3d7-736f11a0dc78" />
   Le das en **Add to Firefox**
   
   <img width="404" height="274" alt="image" src="https://github.com/user-attachments/assets/08297eb1-d535-4491-98f2-5b12cfc583d3" />
   
   Luego le das en **Añadir**


   Una vez añadido te saldra esta **Barra Lateral** de opciones
   <img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/7fae826d-a40c-45af-889c-f9c1636925bd" />

   

3. Ve a: **https://c.mi.com/global/**
4. Inicia sesión con tu cuenta Mi y espera a que cargue todo el contenido
5. Abre Cookie Editor (ícono en la barra lateral izquierda)
6. Busca la cookie: `new_bbs_serviceToken`
7. Copia el **valor completo** (será muy largo)

##### Google Chrome: Funcion Javascript

1. Ve a: **https://c.mi.com/global/**
2. Inicia sesión con tu cuenta Mi y espera a que cargue todo tu contenido
3. Pega este código **en la barra de direcciones (URL)**:

```javascript
javascript :(function(){var token=document.cookie.match(/serviceToken=([^;]+)/);if(token){prompt("Copia tu token:", token[1]);}else{alert("Token no encontrado. Asegúrate de estar logueado.");}})()
```

4. **⚠️ IMPORTANTE**: Elimina el espacio entre `javascript` y `:` 
5. Presiona **Enter**
6. Copia el token del popup

### ⚙️ Configuración del Timeshift

El `timeshift` es **CRÍTICO** para el éxito. Ajústalo según tu ubicación:

| Ubicación/Conexión | Latencia Típica | Timeshift Recomendado | Notas |
|-------------------|-----------------|----------------------|-------|
| 🌎 América Latina (Wi-Fi) | 120-200ms | **300-320ms** | Valor por defecto |
| 🌎 América Latina (Fibra) | 80-120ms | **280-300ms** | Conexión rápida |
| 🌍 Europa | 150-250ms | **320-350ms** | Más lejos de Asia |
| 🌏 Asia | 20-80ms | **240-260ms** | Cerca de servidores |
| 🏢 Conexión Corporativa | Variable | **300-350ms** | Por seguridad |

**🎯 Cómo Ajustar:**
- Si **siempre llegas tarde** → Reduce 20ms (ej: 300 → 280)
- Si **siempre llegas temprano** → Aumenta 20ms (ej: 300 → 320)
- El script muestra la **latencia NTP** - úsala como referencia


#### Paso 3: Ejecutar el Script

```bash
# En la carpeta del script
python unlockBOOTLOADER.py
```

#### Paso 4: Seguir las Instrucciones

1. Ingresa el **número de línea** del token (generalmente `1`)
2. El script mostrará:
   - ✅ Estado de la cuenta
   - ⏰ Sincronización NTP
   - 📊 Countdown hasta medianoche Pekín
   - 🚀 Resultado de las peticiones


### 📸 Vista Previa

```
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║            unlockBOOTLOADER - Xiaomi Bootloader Unlock Optimizer     ║
║                                                                       ║
╠═══════════════════════════════════════════════════════════════════════╣
║   Version:     v2.1.0                                                 ║
║   Author:      @kevxngg                                               ║
║   GitHub:      https://github.com/kevxngg/unlockBOOTLOADER           ║
║   Socials:     GitHub/Facebook/Instagram/Telegram: @kevxngg          ║
╚═══════════════════════════════════════════════════════════════════════╝

📂 Directorio de trabajo: C:\Users\Usuario\unlockBOOTLOADER

----------------------------------------------------------------------
✓ Encontrado: token.txt
✓ Encontrado: timeshift.txt
----------------------------------------------------------------------

📋 Número de línea del token: 1

----------------------------------------------------------------------
✓ Configuración cargada
----------------------------------------------------------------------

🔑 Device ID: A1B2C3D4E5F67890...

🔍 Consultando estado de la cuenta...
----------------------------------------------------------------------
✓ Cuenta elegible para solicitar desbloqueo
----------------------------------------------------------------------

╔═══════════════════════════════════════════════════════════════════╗
║  ⏱️  SINCRONIZACIÓN NTP                                            ║
╚═══════════════════════════════════════════════════════════════════╝
⏱️  Sincronizando con time.google.com... ✓ (latencia: 45.2ms)
📅 Hora Pekín: 2026-03-03 23:45:15.234

╔═══════════════════════════════════════════════════════════════════╗
║  ⏳ CONFIGURACIÓN DE TIMING                                        ║
╚═══════════════════════════════════════════════════════════════════╝
📍 Desfase de red: 300.00 ms
🎯 Hora objetivo:  2026-03-04 00:00:00.700

⏰ Esperando momento crítico... (mantén esta ventana abierta)

⏱️  Tiempo restante: 00:14:42
```

### ❓ Preguntas Frecuentes (FAQ)

<details>
<summary><b>¿Este script desbloquea mi bootloader directamente?</b></summary>

**No.** Este script solo optimiza el **timing** de la solicitud de autorización a los servidores de Xiaomi. Después de recibir autorización, aún necesitas usar la **Mi Unlock Tool** oficial para desbloquear físicamente el bootloader.
</details>

<details>
<summary><b>¿Por qué necesito un timeshift?</b></summary>

Xiaomi resetea las cuotas diarias a las **00:00:00 hora de Pekín**. Debido a la latencia de red (tu ubicación → servidores en Asia), tu petición tarda en llegar. El timeshift compensa ese retraso para que llegue exactamente a las 00:00:00.
</details>

<details>
<summary><b>¿Cuántos intentos tengo?</b></summary>

Generalmente **uno por día** por cuenta. Si fallas, espera 24 horas. Algunos usuarios reportan bloqueos de 168 horas (7 días) si se abusa.
</details>

<details>
<summary><b>¿Funciona en todos los dispositivos Xiaomi?</b></summary>

Sí, siempre que el dispositivo sea elegible para desbloqueo según las políticas de Xiaomi. Verifica en la web oficial de Mi Unlock.
</details>

<details>
<summary><b>¿Es seguro usar este script?</b></summary>

El código es **open-source** y puedes revisarlo. No contiene malware. Sin embargo, usar herramientas no oficiales puede violar los ToS de Xiaomi. **Usa bajo tu propio riesgo.**
</details>

<details>
<summary><b>Mi token dice "caducado". ¿Qué hago?</b></summary>

Los tokens expiran. Simplemente obtén uno nuevo siguiendo la [guía de extracción](#paso-1-obtener-tu-token-de-sesión).
</details>

### ⚠️ Advertencias y Descargo de Responsabilidad

```
⚠️  IMPORTANTE - LEE ANTES DE USAR

✗ Este script NO desbloquea tu bootloader directamente
✗ Solo optimiza el timing de la solicitud de autorización
✓ Aún necesitas usar Mi Unlock Tool oficial después
✗ Puede violar los Términos de Servicio de Xiaomi
✗ NO garantiza éxito - solo maximiza probabilidades
✗ Xiaomi puede banear cuentas que detecte usando automatización
✗ Desbloquear el bootloader BORRA todos tus datos
✗ Puede invalidar tu garantía
✗ Uso completamente bajo tu PROPIO RIESGO

El autor (@kevxngg) NO se hace responsable de:
- Cuentas baneadas
- Datos perdidos
- Garantías invalidadas
- Problemas con dispositivos
```

### 🛠️ Troubleshooting

| Problema | Solución |
|----------|----------|
| ❌ "Archivo token.txt no encontrado" | Crea `token.txt` en la **misma carpeta** que el script |
| ❌ "Token caducado" | Obtén un nuevo token (expiran cada pocas horas) |
| ❌ "No se pudo sincronizar NTP" | Verifica tu conexión a Internet / Firewall |
| ❌ Siempre llega tarde | **Reduce** el timeshift en 20ms |
| ❌ Siempre llega temprano | **Aumenta** el timeshift en 20ms |
| ❌ "Cuota global agotada" | Espera 24 horas e intenta de nuevo |
| ❌ Script no encuentra archivos en VSCode | Usa la versión v2.1 que tiene fix de rutas |

### 🤝 Contribuir

¡Las contribuciones son bienvenidas! 

1. **Fork** este repositorio
2. Crea una **Feature Branch** (`git checkout -b feature/MejoraNueva`)
3. **Commit** tus cambios (`git commit -m 'Agregar MejoraNueva'`)
4. **Push** a la Branch (`git push origin feature/MejoraNueva`)
5. Abre un **Pull Request**

#### Ideas para Contribuir:
- 🌐 Traducciones a otros idiomas
- 📊 Estadísticas de éxito por región
- 🎨 Mejoras en la UI
- 🐛 Reportar/corregir bugs
- 📝 Mejorar documentación

### 📜 Changelog

#### v2.1.0 (2026-03-03)
- ✅ Fix de rutas relativas (funciona desde cualquier ubicación)
- ✅ Banner profesional ASCII art
- ✅ Guía integrada de extracción de tokens
- ✅ Mejoras en mensajes de error
- ✅ Display de directorio de trabajo

#### v2.0.0 (2026-03-01)
- ✅ Refactorización completa del código
- ✅ Type hints en funciones
- ✅ Countdown en tiempo real
- ✅ Múltiples servidores NTP
- ✅ Display de latencia
- ✅ UI con colores y emojis

### 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Ver archivo [LICENSE](LICENSE) para más detalles.

```
MIT License

Copyright (c) 2026 kevxngg

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y archivos de documentación asociados (el "Software"), para 
utilizar el Software sin restricciones...
```

### 👤 Autor

<div align="center">

**kevxngg**

[![GitHub](https://img.shields.io/badge/GitHub-kevxngg-black?style=for-the-badge&logo=github)](https://github.com/kevxngg)
[![Facebook](https://img.shields.io/badge/Facebook-kevxngg-blue?style=for-the-badge&logo=facebook)](https://facebook.com/kevxngg)
[![Instagram](https://img.shields.io/badge/Instagram-kevxngg-purple?style=for-the-badge&logo=instagram)](https://instagram.com/kevxngg)
[![Telegram](https://img.shields.io/badge/Telegram-kevxngg-blue?style=for-the-badge&logo=telegram)](https://t.me/kevxngg)

</div>

### 🌟 Agradecimientos

Si este proyecto te ayudó, considera:
- ⭐ Darle una **estrella** en GitHub
- 🐛 Reportar **bugs** o sugerir **mejoras**
- 🤝 Contribuir con **código** o **documentación**
- 📢 Compartirlo con otros que lo necesiten

### 📊 Estadísticas del Proyecto

![GitHub stars](https://img.shields.io/github/stars/kevxngg/unlockBOOTLOADER?style=social)
![GitHub forks](https://img.shields.io/github/forks/kevxngg/unlockBOOTLOADER?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/kevxngg/unlockBOOTLOADER?style=social)

---

## 🇬🇧 English

### 📖 What is unlockBOOTLOADER?

**unlockBOOTLOADER** is a command-line tool that automates and optimizes the Xiaomi bootloader unlock request process using ultra-precise NTP synchronization and advanced network optimizations.

### ✨ Features

- 🎯 Ultra-precise NTP sync with atomic servers
- ⚡ Advanced network optimizations (TLS pre-warming, Keep-Alive)
- 🔥 Automated request burst at the exact critical moment
- 📊 Real-time countdown display
- 🎨 Professional colorful UI
- 📝 Millisecond-precision logging
- 🛡️ Robust error handling

### 🚀 Quick Start

```bash
git clone https://github.com/kevxngg/unlockBOOTLOADER.git
cd unlockBOOTLOADER
pip install -r requirements.txt
python unlockBOOTLOADER.py
```

For detailed instructions, see the Spanish section above.

### 📄 License

MIT License - See [LICENSE](LICENSE) file

### 👤 Author

**kevxngg** - [@kevxngg](https://github.com/kevxngg)

---

<div align="center">

**Made with ❤️ by kevxngg**

*If this project helped you, give it a ⭐ on GitHub!*

</div>
