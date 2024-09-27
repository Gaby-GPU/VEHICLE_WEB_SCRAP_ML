import pandas as pd
import os

def export_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    current_directory = os.getcwd()
    print(f'Datos exportados a {os.path.join(current_directory, filename)}')


def export_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    current_directory = os.getcwd()
    print(f'Datos exportados a {os.path.join(current_directory, filename)}')