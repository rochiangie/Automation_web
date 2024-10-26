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
5. Crear archivo .env con este formato:
smtp_username=tu_email
smtp_password=contrasenia_creada_anteriormente

Pasos para obtener el archivo credentials.json
Accede a Google Cloud Console:

Ve a Google Cloud Console.
Inicia sesión con tu cuenta de Google.
Crear un Proyecto o Seleccionar uno Existente:

Si no tienes un proyecto creado, crea uno nuevo desde el menú superior izquierdo seleccionando "Crear proyecto".
Dale un nombre a tu proyecto y haz clic en Crear.
Habilitar la API de Gmail:

Con el proyecto seleccionado, ve a Biblioteca en el menú de navegación.
Busca Gmail API y haz clic en Habilitar para activarla en tu proyecto.
Configurar la Pantalla de Consentimiento de OAuth:

Dirígete a Credenciales en el menú lateral.
Haz clic en Configurar la pantalla de consentimiento de OAuth y sigue los pasos para configurar la pantalla. En este paso, selecciona Externo como tipo de usuario y llena la información básica (nombre de la aplicación, correo, etc.).
Crear las Credenciales de Cliente OAuth 2.0:

Desde la página de Credenciales, haz clic en Crear credenciales y selecciona ID de cliente de OAuth.
Configura el tipo de aplicación seleccionando Aplicación de escritorio.
Una vez creada, Google te dará la opción de descargar el archivo credentials.json. Descárgalo y guárdalo en el mismo directorio que tu script.
Coloca credentials.json en el Directorio del Script:

Asegúrate de que el archivo credentials.json se encuentra en la misma carpeta que el script de Python.