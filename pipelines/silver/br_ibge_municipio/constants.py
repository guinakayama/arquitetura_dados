import dotenv , os
from pathlib import Path

caminho = Path(__file__).resolve().parent.parent.parent.parent / ".env"

dotenv.load_dotenv(caminho)

TOKEN = os.getenv("TOKEN")

SOURCE_URL = "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2025/Brasil/BR_Municipios_2025.zip"

DOWNLOAD_DIR = "data/"
FILE_NAME = "br_ibge_municipio.zip"

TABLE_NAME = "br_ibge_municipio"