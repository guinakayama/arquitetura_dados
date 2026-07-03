import tasks

def br_ibge_municipio():
    
    print('Downloading data...')
    tasks.download_data()
    
    print('Unzipping file...')
    file_path = tasks.unzip_file()
    
    print('Loading data to MotherDuck...')
    tasks.load_data(extension='spatial', file_path=file_path)

    print('Building dbt models...')
    tasks.build_models()
    
if __name__ == "__main__":
    br_ibge_municipio()