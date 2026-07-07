import logging

# Configuración del sistema de registro de eventos (logging).
# Todos los mensajes generados por la aplicación se almacenarán
# en el archivo "logs.txt".
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Crea una instancia del logger para ser utilizada
# en los diferentes módulos del proyecto.
logger = logging.getLogger(__name__)