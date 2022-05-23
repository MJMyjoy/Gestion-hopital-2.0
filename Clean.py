import os

def clean_it():
        command = "clear"
        if os.name in ('nt', 'dos'):
                command = "cls"
        os.system(command)
