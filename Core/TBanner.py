from colorama import Fore



_banner = '''
'''



def banner(host, port):
    print(Fore.RED + _banner)
    print(f'http://{host}:{port}')