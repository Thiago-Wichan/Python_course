# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import aula285
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'desktop')
FOLDER = os.path.join(DESKTOP, 'analises')
NEW_FOLDER = os.path.join(DESKTOP, 'new_folder')
# print(FOLDER)

shutil.rmtree(NEW_FOLDER, ignore_errors=True)
shutil.copytree(FOLDER, NEW_FOLDER)


# os.makedirs(NEW_FOLDER, exist_ok=True)

# for roots, dirs, files in os.walk(FOLDER):
#     stats_size = os.stat(FOLDER).st_size
#     for dir_ in dirs:
#         new_path_dirs = os.path.join(roots.replace(FOLDER, NEW_FOLDER), dir_)
#         # print(new_path_dirs)
#         os.makedirs(new_path_dirs, exist_ok=True)
#     for file in files:
#         path_ = os.path.join(roots, file)
#         new_path_files = os.path.join(roots.replace(FOLDER, NEW_FOLDER), file)
#         print(new_path_files, file, aula285.formata_tamanho(stats_size))
#         shutil.copy(path_, new_path_files)
