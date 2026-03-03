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

## Paso 1: Crear Archivos de Configuración

En la **carpeta** que se creo cuando descomprimiste `unlockBOOTLOADER.zip`, crea estos dos archivos:

```
token.txt
timeshift.txt
```
El archivo **token.txt** lo abriras con el **Bloc de Notas** y lo vas a editar de la siguiente forma
```texto
1
2
3
4
```
Pondras esas filas de numeros

Y el archivo **timeshift.txt** tambien lo abriras y lo editaras de la siguiente manera
```texto
300
280
260
240
```

## Paso 2: Obtener tus Tokens de Sesión

Hay **DOS métodos** para extraer los tokens necesarios:

## Firefox: Con la extensión Cookie-Editor

1. Abre Firefox e instala la extensión "[Cookie Editor](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)"
   <div align="left">
     <img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/380832c4-b82c-420d-b3d7-736f11a0dc78" />
   </div>
Le das en **Add to Firefox**
   <div align="left">
     <img width="404" height="274" alt="image" src="https://github.com/user-attachments/assets/08297eb1-d535-4491-98f2-5b12cfc583d3" />
   </div>
   
   Luego le das en **Añadir**

   Una vez añadido te saldra esta **Barra Lateral** de opciones
   <div align="left">
     <img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/7fae826d-a40c-45af-889c-f9c1636925bd" />
   </div>

3. Ve a: **https://c.mi.com/global/**

4. Inicia sesión con tu cuenta Mi y espera a que cargue todo el contenido
   <div align="left">
     <img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/8e8eb1db-ee62-4bf7-b665-03898716e17e" />
   </div>

5. Abre Cookie Editor (ícono en la barra lateral izquierda)
   <div align="left">
     <img width="396" height="713" alt="image" src="https://github.com/user-attachments/assets/bda73b2d-5734-4f05-96be-2a974669ff31" />
   </div>

6. Busca la cookie: `new_bbs_serviceToken`
   <div align="left">
     <img width="395" height="248" alt="image" src="https://github.com/user-attachments/assets/c3ae3942-0480-41aa-a428-e9445904653d" />
     <br><br>
     <img width="413" height="411" alt="image" src="https://github.com/user-attachments/assets/c8f79815-f26e-488a-a28d-014702e88443" />
   </div>

7. Copia el **valor completo** (será muy largo)
   <div align="left">
     <img width="397" height="414" alt="image" src="https://github.com/user-attachments/assets/e8e5d781-ff30-4792-a165-e05a1f38d51e" />
   </div>
   
   Click derecho sobre el valor, luego le das **Ctrl + A** para selecionar todo y luego **Ctrl + C** para copiar

8. Ahora vas a abrir el archivo **token.txt** y vas a pegar ese **token** en la linea **1** y **3**, (elimina el numero de linea) te deberia quedar algo asi:
```
token_ejemplo_firefox4Gf22VTTk5JjpZa8%2FxhO6XTUVNKLEMfatx2Uovt877noKGTU7%2Fjvx%
2
token_ejemplo_firefox4Gf22VTTk5JjpZa8%2FxhO6XTUVNKLEMfatx2Uovt877noKGTU7%2Fjvx%
4
```
Le das **Ctrl + G** y guardas

## Google Chrome: Funcion Javascript

1. Ve a: **https://c.mi.com/global/**
2. Inicia sesión con tu cuenta Mi, **acepta todas las Cookies** y espera a que cargue todo tu contenido
3. Pega este código **en la barra de direcciones (URL)**:

```javascript
javascript :(function(){var token=document.cookie.match(/popRunToken=([^;]+)/);if(token){prompt("Copy the token:", token[1]);}else{alert("Token not found");}})()
```
<div align="left">
  <img width="1411" height="853" alt="image" src="https://github.com/user-attachments/assets/67f00ff1-6297-4648-91ac-ac04a7b1f7cf" />
</div>

4. **⚠️ IMPORTANTE**: Elimina el espacio entre `javascript` y `:` 
5. Presiona **Enter**
   
   <div align="left">
      <img width="469" height="211" alt="image" src="https://github.com/user-attachments/assets/86ac3903-c097-45a8-a501-9a15c0634e15" />
   </div>

7. Dale **Ctrl + C** y copia el token del popup
8. Ahora ese **token** lo vas a pegar en el archivo **token.txt** en la linea **2** y **4** (elimina el numero de linea) y te quedaria algo asi:
```
token_ejemplo_firefox4Gf22VTTk5JjpZa8%2FxhO6XTUVNKLEMfatx2Uovt877noKGTU7%2Fjvx%
token_ejemplo_googleNiTl2rmQWNdB7pABjG7Ac1twOzL%2F%2BD6nbR1D%2BUwg%2BTbJ%2B8H%2
token_ejemplo_firefox4Gf22VTTk5JjpZa8%2FxhO6XTUVNKLEMfatx2Uovt877noKGTU7%2Fjvx%
token_ejemplo_googleNiTl2rmQWNdB7pABjG7Ac1twOzL%2F%2BD6nbR1D%2BUwg%2BTbJ%2B8H%2
```

### ⚙️ Configuración del Timeshift

El `timeshift` es **CRÍTICO** para el éxito. Si tienes múltiples cuentas/tokens (ej. 4 tokens), te recomendamos usar una estrategia de "ráfaga escalonada" para maximizar tus probabilidades. 

Pon estos 4 valores en tu archivo `timeshift.txt` (un valor por línea en el mismo orden) ajustándolos según tu ubicación:

| Ubicación/Conexión | Latencia Típica | Valores Recomendados (timeshift.txt) | Notas |
|-------------------|-----------------|--------------------------------------|-------|
| 🌎 América Latina (Wi-Fi) | 120-200ms | **340, 320, 300, 280** | Cubre variaciones de ping por Wi-Fi |
| 🌎 América Latina (Fibra) | 80-120ms | **300, 280, 260, 240** | Óptimo para conexiones muy rápidas |
| 🌍 Europa | 150-250ms | **360, 340, 320, 300** | Compensa la distancia física a Asia |
| 🌏 Asia | 20-80ms | **260, 240, 220, 200** | Valores bajos por proximidad a servidores |
| 🏢 Conexión Corporativa | Variable | **350, 330, 310, 290** | Compensa el retraso de Firewalls/VPNs |

**🎯 El mejor truco para ajustar tu estrategia:**
Cuando ejecutes el script, observa atentamente esta línea en tu consola:
> `⏱️ Sincronizando con time.google.com... ✓ (latencia: 290.5ms)`

Utiliza ese número como tu punto central. Si la consola muestra **290ms**, deberías crear un bloque que lo rodee, por ejemplo: **310, 300, 290, 280**.

**🛠️ Corrección de Errores:**
- Si el servidor te dice "cuota agotada" pero tu respuesta llegó **antes** de las 00:00:00 → Estás disparando muy temprano. **Resta 20ms** a todo tu bloque de valores.
- Si llegas a las 00:00:00 pero alguien te gana el puesto → Estás llegando tarde. **Suma 20ms** a todo tu bloque de valores.

## Paso 3: Ejecutar el Script desde Windows

La forma más rápida y sencilla de ejecutar el script es abriendo la consola de comandos (CMD) directamente desde la carpeta del proyecto.

1. Abre el Explorador de Archivos y ve a la carpeta donde descargaste y descomprimiste el proyecto (donde están los archivos `unlockBOOTLOADER.py`, `token.txt` y `timeshift.txt`).
2. Haz clic en la **barra de direcciones** en la parte superior (donde se ve la ruta de la carpeta, que quedará seleccionada en azul).
3. Borra toda esa ruta, escribe la palabra **`cmd`** y presiona la tecla **Enter**.
   <div align="left">
     <img width="1125" height="667" alt="image" src="https://github.com/user-attachments/assets/9a84af0a-ac0f-4be0-9d23-607ef41d27c9" />
   </div>

4. Se abrirá una ventana negra de la consola (Símbolo del sistema) ya ubicada exactamente en esa carpeta.
   <div align="left">
     <img width="979" height="646" alt="image" src="https://github.com/user-attachments/assets/fd0980ae-068e-4cb5-b99d-761d8f499703" />
   </div>

5. Para iniciar el programa, simplemente escribe el siguiente comando y presiona **Enter**:

   ```bash
   python unlockBOOTLOADER.py
   ```
   
> **💡 TIP PRO: Ejecución Múltiple (Estrategia de 4 Tokens)**
> 
> Ya que tienes 4 tokens configurados en tu archivo `token.txt` y 4 valores de latencia escalonados en `timeshift.txt`, puedes maximizar tus probabilidades de éxito ejecutándolos al mismo tiempo:
> 
> 1. Repite el [Paso 3](https://github.com/kevxngg/unlockBOOTLOADER/blob/main/README.md#paso-3-ejecutar-el-script-desde-windows) para abrir **4 ventanas de CMD distintas**.
> 2. Escribe `python unlockBOOTLOADER.py` y presiona Enter en cada una de ellas.
> 3. Cuando el script te solicite el **"Número de línea del token"**, ingresa `1` en la primera ventana, `2` en la segunda, `3` en la tercera y `4` en la cuarta.
> 
> De esta manera, tendrás 4 procesos corriendo en paralelo esperando la medianoche. El script disparará las 4 peticiones automáticas con los 4 tiempos de desfase diferentes que configuraste, cubriendo perfectamente todos los márgenes posibles de tu conexión y asegurando que alguna llegue en el milisegundo exacto.

## Paso 4: Seguir las Instrucciones

1. Ingresa el **número de línea** del token
2. El script mostrará:
   - ✅ Estado de la cuenta
   - ⏰ Sincronización NTP
   - 📊 Countdown hasta medianoche Pekín
   - 🚀 Resultado de las peticiones


### 📸 Vista Previa
<img width="983" height="959" alt="image" src="https://github.com/user-attachments/assets/a1da14ae-ba8d-4eae-bde9-3fd61e3a2c1f" />


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
<summary><b>¿Funciona en todos los dispositivos Xiaomi / Redmi / POCO?</b></summary>

Sí, pero debido a las **nuevas políticas de seguridad de Xiaomi (HyperOS)**, debes cumplir requisitos muy estrictos y seguir un orden específico:

1. **Antigüedad de la cuenta:** Tu Cuenta Mi debe haber sido creada hace **más de 30 días** y estar activa de forma continua.
2. **Región Global:** Este script aplica para cuentas y dispositivos de la región **Global**. (La ROM China tiene un sistema diferente que requiere Nivel 5 en su foro).
3. **Orden correcto del proceso:**
   * **Paso 1 (Autorización):** Usas este script para conseguir el cupo en los servidores de Xiaomi a la medianoche.
   * **Paso 2 (Vinculación):** Una vez el script te marque "🎉 ¡AUTORIZACIÓN CONCEDIDA!", vas a tu teléfono (*Ajustes > Opciones de Desarrollador > Estado de Mi Unlock*) y **vinculas** tu cuenta al dispositivo.
   * **Paso 3 (Desbloqueo):** Usas la herramienta oficial *Mi Unlock Tool* en tu PC para realizar el desbloqueo físico del bootloader (es posible que la herramienta te pida esperar 72 horas o más después de vincular).

Si no tienes los 30 días en tu cuenta o intentas vincular el teléfono antes de conseguir la autorización con el script, los servidores de Xiaomi te rechazarán.
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

![unnamed](https://github.com/user-attachments/assets/e6ad8e36-80b7-4f97-86fb-56fcbf84ee5f)


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

**unlockBOOTLOADER** is a command-line tool that automates and optimizes the Xiaomi bootloader unlock request process. 

It uses:
- ⏰ Ultra-precise NTP synchronization with atomic servers
- 🚀 Advanced network optimizations (TLS pre-warming, Keep-Alive)
- 🎯 Perfect timing to maximize success probabilities

### ✨ Features

| Feature | Description |
|----------------|-------------|
| 🎯 **NTP Synchronization** | Atomic servers: Google, Cloudflare, NIST, Windows |
| ⚡ **Network Optimization** | TLS pre-warming, HTTP/1.1 Keep-Alive, aggressive timeouts |
| 🔥 **Automated Burst** | Multiple requests at the exact moment (00:00:00 Beijing) |
| 📊 **Real-Time Countdown** | HH:MM:SS display until the critical moment |
| 🎨 **Professional UI** | Colorful interface with emojis and ASCII art |
| 📝 **Detailed Logging** | Timestamps with millisecond precision |
| 🛡️ **Error Handling** | Automatic recovery from network failures |
| 📁 **Automatic Paths** | Works from any location |

### 🚀 Installation

#### Prerequisites
```bash
- Python 3.7 or higher
- pip (included with Python)
- Firefox Browser
- Google Chrome Browser
- Stable Internet connection
```

#### Download
1. Download `unlockBOOTLOADER.zip` from [Releases](https://github.com/kevxngg/unlockBOOTLOADER/releases)
2. Unzip the file 

### 📝 Complete Usage Guide

## Step 1: Create Configuration Files

In the **folder** created when you unzipped `unlockBOOTLOADER.zip`, create these two files:

```
token.txt
timeshift.txt
```
You will open the **token.txt** file with **Notepad** and edit it as follows:
```text
1
2
3
4
```
You will put those rows of numbers.

And you will also open the **timeshift.txt** file and edit it like this:
```text
300
280
260
240
```

## Step 2: Obtain your Session Tokens

There are **TWO methods** to extract the necessary tokens:

## Firefox: With the Cookie-Editor extension

1. Open Firefox and install the "[Cookie Editor](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)" extension
   <div align="left">
     <img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/380832c4-b82c-420d-b3d7-736f11a0dc78" />
   </div>
Click on **Add to Firefox**
   <div align="left">
     <img width="404" height="274" alt="image" src="https://github.com/user-attachments/assets/08297eb1-d535-4491-98f2-5b12cfc583d3" />
   </div>
   
   Then click on **Add**

   Once added, this options **Sidebar** will appear
   <div align="left">
     <img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/7fae826d-a40c-45af-889c-f9c1636925bd" />
   </div>

3. Go to: **https://c.mi.com/global/**

4. Log in with your Mi account and wait for all the content to load
   <div align="left">
     <img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/8e8eb1db-ee62-4bf7-b665-03898716e17e" />
   </div>

5. Open Cookie Editor (icon on the left sidebar)
   <div align="left">
     <img width="396" height="713" alt="image" src="https://github.com/user-attachments/assets/bda73b2d-5734-4f05-96be-2a974669ff31" />
   </div>

6. Search for the cookie: `new_bbs_serviceToken`
   <div align="left">
     <img width="395" height="248" alt="image" src="https://github.com/user-attachments/assets/c3ae3942-0480-41aa-a428-e9445904653d" />
     <br><br>
     <img width="413" height="411" alt="image" src="https://github.com/user-attachments/assets/c8f79815-f26e-488a-a28d-014702e88443" />
   </div>

7. Copy the **complete value** (it will be very long)
   <div align="left">
     <img width="397" height="414" alt="image" src="https://github.com/user-attachments/assets/e8e5d781-ff30-4792-a165-e05a1f38d51e" />
   </div>
   
   Right-click on the value, then press **Ctrl + A** to select all and then **Ctrl + C** to copy

8. Now you are going to open the **token.txt** file and paste that **token** on lines **1** and **3**, (delete the line number) it should look something like this:
```
token_example_firefox4Gf22VTTk5JjpZa8%2FxhO6XTUVNKLEMfatx2Uovt877noKGTU7%2Fjvx%
2
token_example_firefox4Gf22VTTk5JjpZa8%2FxhO6XTUVNKLEMfatx2Uovt877noKGTU7%2Fjvx%
4
```
Press **Ctrl + S** and save

## Google Chrome: Javascript Function

1. Go to: **https://c.mi.com/global/**
2. Log in with your Mi account, **accept all Cookies** and wait for all your content to load
3. Paste this code **into the address bar (URL)**:

```javascript
javascript :(function(){var token=document.cookie.match(/popRunToken=([^;]+)/);if(token){prompt("Copy the token:", token[1]);}else{alert("Token not found");}})()
```
<div align="left">
  <img width="1411" height="853" alt="image" src="https://github.com/user-attachments/assets/67f00ff1-6297-4648-91ac-ac04a7b1f7cf" />
</div>

4. **⚠️ IMPORTANT**: Remove the space between `javascript` and `:` 
5. Press **Enter**
   
   <div align="left">
      <img width="469" height="211" alt="image" src="https://github.com/user-attachments/assets/86ac3903-c097-45a8-a501-9a15c0634e15" />
   </div>

7. Press **Ctrl + C** and copy the token from the popup
8. Now you will paste that **token** into the **token.txt** file on lines **2** and **4** (delete the line number) and it would look something like this:
```
token_example_firefox4Gf22VTTk5JjpZa8%2FxhO6XTUVNKLEMfatx2Uovt877noKGTU7%2Fjvx%
token_example_googleNiTl2rmQWNdB7pABjG7Ac1twOzL%2F%2BD6nbR1D%2BUwg%2BTbJ%2B8H%2
token_example_firefox4Gf22VTTk5JjpZa8%2FxhO6XTUVNKLEMfatx2Uovt877noKGTU7%2Fjvx%
token_example_googleNiTl2rmQWNdB7pABjG7Ac1twOzL%2F%2BD6nbR1D%2BUwg%2BTbJ%2B8H%2
```

### ⚙️ Timeshift Configuration

The `timeshift` is **CRITICAL** for success. If you have multiple accounts/tokens (e.g. 4 tokens), we recommend using a "staggered burst" strategy to maximize your chances. 

Put these 4 values in your `timeshift.txt` file (one value per line in the same order) adjusting them according to your location:

| Location/Connection | Typical Latency | Recommended Values (timeshift.txt) | Notes |
|-------------------|-----------------|--------------------------------------|-------|
| 🌎 Latin America (Wi-Fi) | 120-200ms | **340, 320, 300, 280** | Covers Wi-Fi ping variations |
| 🌎 Latin America (Fiber) | 80-120ms | **300, 280, 260, 240** | Optimal for very fast connections |
| 🌍 Europe | 150-250ms | **360, 340, 320, 300** | Compensates physical distance to Asia |
| 🌏 Asia | 20-80ms | **260, 240, 220, 200** | Low values due to server proximity |
| 🏢 Corporate Connection | Variable | **350, 330, 310, 290** | Compensates Firewall/VPN delays |

**🎯 The best trick to adjust your strategy:**
When you run the script, pay close attention to this line in your console:
> `⏱️ Sincronizando con time.google.com... ✓ (latencia: 290.5ms)`

Use that number as your center point. If the console shows **290ms**, you should create a block surrounding it, for example: **310, 300, 290, 280**.

**🛠️ Troubleshooting:**
- If the server tells you "quota exhausted" but your response arrived **before** 00:00:00 → You are shooting too early. **Subtract 20ms** from your entire block of values.
- If you arrive at 00:00:00 but someone beats you to the spot → You are arriving late. **Add 20ms** to your entire block of values.

## Step 3: Run the Script from Windows

The fastest and easiest way to run the script is by opening the command prompt (CMD) directly from the project folder.

1. Open File Explorer and go to the folder where you downloaded and unzipped the project (where the `unlockBOOTLOADER.py`, `token.txt`, and `timeshift.txt` files are).
2. Click on the **address bar** at the top (where the folder path is seen, it will be highlighted in blue).
3. Delete that entire path, type the word **`cmd`** and press the **Enter** key.
   <div align="left">
     <img width="1125" height="667" alt="image" src="https://github.com/user-attachments/assets/9a84af0a-ac0f-4be0-9d23-607ef41d27c9" />
   </div>

4. A black console window (Command Prompt) will open, already located exactly in that folder.
   <div align="left">
     <img width="979" height="646" alt="image" src="https://github.com/user-attachments/assets/fd0980ae-068e-4cb5-b99d-761d8f499703" />
   </div>

5. To start the program, simply type the following command and press **Enter**:

   ```bash
   python unlockBOOTLOADER.py
   ```
   
> **💡 PRO TIP: Multiple Execution (4 Token Strategy)**
> 
> Since you have 4 tokens configured in your `token.txt` file and 4 staggered latency values in `timeshift.txt`, you can maximize your chances of success by running them at the same time:
> 
> 1. Repeat [Step 3](https://github.com/kevxngg/unlockBOOTLOADER/blob/main/README.md#step-3-run-the-script-from-windows) to open **4 different CMD windows**.
> 2. Type `python unlockBOOTLOADER.py` and press Enter in each of them.
> 3. When the script prompts you for the **"Token line number"**, enter `1` in the first window, `2` in the second, `3` in the third, and `4` in the fourth.
> 
> This way, you will have 4 processes running in parallel waiting for midnight. The script will fire the 4 automatic requests with the 4 different offset times you configured, perfectly covering all possible margins of your connection and ensuring that one arrives at the exact millisecond.

## Step 4: Follow the Instructions

1. Enter the token **line number**
2. The script will show:
   - ✅ Account status
   - ⏰ NTP Synchronization
   - 📊 Countdown to Beijing midnight
   - 🚀 Request results


### 📸 Preview
<img width="983" height="959" alt="image" src="https://github.com/user-attachments/assets/a1da14ae-ba8d-4eae-bde9-3fd61e3a2c1f" />


### ❓ Frequently Asked Questions (FAQ)

<details>
<summary><b>Does this script unlock my bootloader directly?</b></summary>

**No.** This script only optimizes the authorization request **timing** to Xiaomi's servers. After receiving authorization, you still need to use the official **Mi Unlock Tool** to physically unlock the bootloader.
</details>

<details>
<summary><b>Why do I need a timeshift?</b></summary>

Xiaomi resets daily quotas at **00:00:00 Beijing time**. Due to network latency (your location → servers in Asia), your request takes time to arrive. The timeshift compensates for that delay so it arrives exactly at 00:00:00.
</details>

<details>
<summary><b>How many attempts do I have?</b></summary>

Generally **one per day** per account. If you fail, wait 24 hours. Some users report 168-hour (7 days) bans if abused.
</details>

<details>
<summary><b>Does it work on all Xiaomi / Redmi / POCO devices?</b></summary>

Yes, but due to **Xiaomi's new security policies (HyperOS)**, you must meet very strict requirements and follow a specific order:

1. **Account age:** Your Mi Account must have been created **more than 30 days ago** and be continuously active.
2. **Global Region:** This script applies to **Global** region accounts and devices. (The Chinese ROM has a different system requiring Level 5 in their forum).
3. **Correct process order:**
   * **Step 1 (Authorization):** Use this script to secure the spot on Xiaomi servers at midnight.
   * **Step 2 (Binding):** Once the script shows "🎉 AUTHORIZATION GRANTED!", go to your phone (*Settings > Developer Options > Mi Unlock Status*) and **bind** your account to the device.
   * **Step 3 (Unlocking):** Use the official *Mi Unlock Tool* on your PC to perform the physical bootloader unlock (the tool might ask you to wait 72 hours or more after binding).

If you don't have the 30 days on your account or try to bind the phone before getting authorization with the script, Xiaomi servers will reject you.
</details>

<details>
<summary><b>Is it safe to use this script?</b></summary>

The code is **open-source** and you can review it. It contains no malware. However, using unofficial tools may violate Xiaomi's ToS. **Use at your own risk.**
</details>

<details>
<summary><b>My token says "expired". What do I do?</b></summary>

Tokens expire. Simply get a new one following the extraction guide.
</details>

### ⚠️ Warnings and Disclaimer

```
⚠️  IMPORTANT - READ BEFORE USING

✗ This script DOES NOT unlock your bootloader directly
✗ It only optimizes the authorization request timing
✓ You still need to use official Mi Unlock Tool afterwards
✗ May violate Xiaomi's Terms of Service
✗ DOES NOT guarantee success - only maximizes probabilities
✗ Xiaomi may ban accounts detected using automation
✗ Unlocking the bootloader ERASES all your data
✗ May void your warranty
✗ Use completely at your OWN RISK

The author (@kevxngg) is NOT responsible for:
- Banned accounts
- Lost data
- Voided warranties
- Device issues
```

### 🛠️ Troubleshooting

| Problem | Solution |
|----------|----------|
| ❌ "token.txt file not found" | Create `token.txt` in the **same folder** as the script |
| ❌ "Expired token" | Get a new token (they expire every few hours) |
| ❌ "Could not sync NTP" | Check your Internet connection / Firewall |
| ❌ Always arrives late | **Decrease** the timeshift by 20ms |
| ❌ Always arrives early | **Increase** the timeshift by 20ms |
| ❌ "Global quota exhausted" | Wait 24 hours and try again |
| ❌ Script can't find files in VSCode | Use version v2.1 which has path fixes |

### 🤝 Contributing

Contributions are welcome! 

1. **Fork** this repository
2. Create a **Feature Branch** (`git checkout -b feature/NewImprovement`)
3. **Commit** your changes (`git commit -m 'Add NewImprovement'`)
4. **Push** to the Branch (`git push origin feature/NewImprovement`)
5. Open a **Pull Request**

#### Ideas for Contributing:
- 🌐 Translations to other languages
- 📊 Success statistics by region
- 🎨 UI improvements
- 🐛 Report/fix bugs
- 📝 Improve documentation

### 📜 Changelog

#### v2.1.0 (2026-03-03)
- ✅ Relative paths fix (works from any location)
- ✅ Professional ASCII art banner
- ✅ Integrated token extraction guide
- ✅ Error message improvements
- ✅ Working directory display

#### v2.0.0 (2026-03-01)
- ✅ Complete code refactoring
- ✅ Type hints in functions
- ✅ Real-time countdown
- ✅ Multiple NTP servers
- ✅ Latency display
- ✅ UI with colors and emojis

### 📄 License

This project is under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

```
MIT License

Copyright (c) 2026 kevxngg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

### 👤 Author

<div align="center">

![unnamed](https://github.com/user-attachments/assets/e6ad8e36-80b7-4f97-86fb-56fcbf84ee5f)


[![GitHub](https://img.shields.io/badge/GitHub-kevxngg-black?style=for-the-badge&logo=github)](https://github.com/kevxngg)
[![Facebook](https://img.shields.io/badge/Facebook-kevxngg-blue?style=for-the-badge&logo=facebook)](https://facebook.com/kevxngg)
[![Instagram](https://img.shields.io/badge/Instagram-kevxngg-purple?style=for-the-badge&logo=instagram)](https://instagram.com/kevxngg)
[![Telegram](https://img.shields.io/badge/Telegram-kevxngg-blue?style=for-the-badge&logo=telegram)](https://t.me/kevxngg)

</div>

### 🌟 Acknowledgments

If this project helped you, consider:
- ⭐ Giving it a **star** on GitHub
- 🐛 Reporting **bugs** or suggesting **improvements**
- 🤝 Contributing **code** or **documentation**
- 📢 Sharing it with others who might need it

### 📊 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/kevxngg/unlockBOOTLOADER?style=social)
![GitHub forks](https://img.shields.io/github/forks/kevxngg/unlockBOOTLOADER?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/kevxngg/unlockBOOTLOADER?style=social)

---
