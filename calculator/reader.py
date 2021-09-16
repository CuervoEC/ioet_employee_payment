def read_file(file_name: str) -> list:
    """Loads and format input data from a file"""
    with open(f'{file_name}', 'r') as data:
        data_list = [''.join(d.split('\n')) for d in data]
        data.close()
        return data_list

