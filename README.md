Proyecto: Script para marcar correos no leídos como leídos en Gmail
Este script utiliza la API de Gmail para identificar y marcar como leídos todos los correos que estén no leídos en una cuenta de Gmail. Para ejecutar este script, se requiere configurar OAuth 2.0 y obtener permisos de la cuenta de Google. Aquí se detalla cómo configurar la verificación en dos pasos, obtener las credenciales necesarias, e instalar las dependencias para que funcione el script.

Prerrequisitos
Python 3.7 o superior: Asegúrate de tener instalada la versión adecuada de Python.
Cuenta de Gmail con verificación en dos pasos habilitada.
1. Configurar verificación en dos pasos
Para usar la autenticación de Google con la API, primero habilita la verificación en dos pasos en tu cuenta de Gmail. Esto se requiere para habilitar el acceso seguro con OAuth 2.0.

Accede a Tu cuenta de Google.
Ve a la sección Seguridad.
En Iniciar sesión en Google, selecciona Verificación en dos pasos y sigue las instrucciones para habilitarla.
2. Habilitar la API de Gmail en Google Cloud Console
Para usar este script, debes habilitar la API de Gmail y configurar OAuth 2.0 en tu proyecto de Google Cloud Console.

Accede a la Google Cloud Console.
Crea un nuevo proyecto o selecciona uno existente.
Ve a Biblioteca y busca Gmail API.
Haz clic en Habilitar para la API de Gmail.
3. Crear credenciales OAuth 2.0
Para obtener acceso a la API de Gmail, crea credenciales de cliente OAuth 2.0:

En el menú de la izquierda, selecciona Credenciales.
Haz clic en Crear credenciales y selecciona ID de cliente de OAuth.
Configura la pantalla de consentimiento con la información básica solicitada.
En Tipo de aplicación, selecciona Aplicación de escritorio y nómbrala (por ejemplo, "Gmail Script App").
Descarga el archivo credentials.json que contiene tus credenciales de OAuth 2.0 y guárdalo en el mismo directorio que tu script.
4. Instalar dependencias