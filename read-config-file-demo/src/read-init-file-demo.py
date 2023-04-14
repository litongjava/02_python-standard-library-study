import configparser

config = configparser.ConfigParser()

config.read('config.ini')

value = config.get('index', 'index_src_dirs')
print(value)

options = config.items('index')
print(options)
count = options.count()

