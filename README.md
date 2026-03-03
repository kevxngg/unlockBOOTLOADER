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
**💡 TIP PRO: Ejecución Múltiple (Estrategia de 4 Tokens)**
> 
> Ya que tienes 4 tokens configurados en tu archivo `token.txt` y 4 valores de latencia escalonados en `timeshift.txt`, puedes maximizar tus probabilidades de éxito ejecutándolos al mismo tiempo:
> 
> 1. Repite los pasos 1 al 3 para abrir **4 ventanas de CMD distintas**.
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
