

try: 
    import django
    message = f'current version : {django.__version__}'
    print(message)
except ImportError as error:
    print(error)