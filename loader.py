def load_file(file_name):
    with open(f'{file_name}', 'r') as data:
        data_list = [''.join(d.split('\n')) for d in data]
        data.close()
        return data_list

