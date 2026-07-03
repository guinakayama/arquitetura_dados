import duckdb
import requests
import constants as cts
import zipfile
from pathlib import Path
import subprocess

con = duckdb.connect('md:naka_arquitetura', config = {'motherduck_token': cts.TOKEN})

def download_data():
    response = requests.get(cts.SOURCE_URL)

    Path(cts.DOWNLOAD_DIR).mkdir(exist_ok=True)

    with open(f'{cts.DOWNLOAD_DIR}{cts.FILE_NAME}', 'wb') as f:
        f.write(response.content)
    
def unzip_file():
    with zipfile.ZipFile(f'{cts.DOWNLOAD_DIR}{cts.FILE_NAME}', 'r') as zip_ref:
        zip_ref.extractall(cts.DOWNLOAD_DIR)

    file_path = Path(cts.DOWNLOAD_DIR).glob('*.shp')

    return next(file_path, None)  # Return the first .shp file found, or None if not found


def load_data(
    extension = 'xlsx',
    layer = 'bronze',
    file_path = f'{cts.DOWNLOAD_DIR}{cts.FILE_NAME}'
):
    if extension == 'spatial':
        con.execute('INSTALL spatial; LOAD spatial;')
    
    extension_translate = {
        'xlsx': 'read_xlsx',
        'csv': 'read_csv',
        'parquet': 'read_parquet',
        'json': 'read_json',
        'spatial': 'ST_Read'
    }
    
    con.sql(f"""
        CREATE OR REPLACE TABLE {layer}.{cts.TABLE_NAME} AS
        SELECT * FROM {extension_translate[extension]}('{file_path}', {'all_varchar = TRUE' if extension != 'spatial' else "open_options = ['FIELD_TYPES=STRING']"})
    """)

def build_models(select = None):
    subprocess.run(['dbt', 'build'] if select is None else ['dbt', 'build', '--select', select])