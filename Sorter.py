from collections.abc import Sequence
import os, time
from shutil import move
from pathlib import Path
from typing import Literal
from win11toast import toast

user_home: str = os.path.expanduser('~')
descargas_dir: str = 'Downloads'
root: str = os.path.join(user_home, descargas_dir)
video_dir : str = os.path.join(root, 'Videos')
img_dir : str = os.path.join(root, 'Imagenes')
doc_dir : str = os.path.join(root, 'Documentos')
pdf_dir : str = os.path.join(root, 'Pdf')
zip_dir : str = os.path.join(root, 'Zip')
exl_dir : str = os.path.join(root, 'Excel')
Pp_dir : str = os.path.join(root, 'Presentaciones')
app_dir : str = os.path.join(root, 'Ejecutables')
other : str = os.path.join(root, 'OtrosArchivos')
vid: tuple[str, ...] = ('.mp3', 'mkv', '.mov', '.m4a', '.mp4')
img: tuple[str, ...] = ('.png', '.jpeg', '.jpg', '.gif', '.svg', '.ico')
doc: tuple[str, ...] = ('.doc', '.txt', '.docx')
pdf: Literal['.pdf'] = ('.pdf')
Pp: tuple[str, ...] = ('.ppt', '.pptx', '.pps', '.ppsx')
exl: tuple[str, ...] = ('.xls', '.xlsx')
com: tuple[str, ...] = ('.zip', '.rar')
app: Literal['.exe'] = ('.exe')
vidLen:int = 0
picLen:int = 0
docLen:int = 0
pdfLen:int = 0
PpLen:int = 0
exlLen:int = 0
compLen:int = 0
appLen:int = 0
otherLen:int = 0
files:list[str] = []
dirs: list[str] = [video_dir, img_dir, doc_dir, pdf_dir, zip_dir, exl_dir, Pp_dir, app_dir, other]

def renombrar(src: str, filed: str, dst: str ) -> None:
    filename, file_extension = os.path.splitext(filed)
    count = 1
    new_filename = filename + str(count) + file_extension


    while os.path.exists(os.path.join(dst, new_filename)):
        count += 1
        new_filename = filename+ str(count) + file_extension

    os.rename(src, os.path.join(dst,new_filename))



def list_files() -> list[str]:


    return [f for f in os.listdir(root)  
                        if not f.startswith('.') and not f == __file__
                        and os.path.join(root,f) not in dirs]


def ordenar()->None:
    global vidLen,docLen,pdfLen,PpLen,compLen,picLen,exlLen,appLen,otherLen
    for file in files:

        try:

            if file.endswith(vid):
                vidLen += 1
                move(root+'\\' + file, video_dir)
            elif file.endswith(img):
                picLen += 1
                move(root+'\\' + file, img_dir)
            elif file.endswith(doc):
                docLen += 1
                move(root+'\\' + file, doc_dir)
            elif file.endswith(pdf):
                pdfLen += 1
                move(root+'\\' + file, pdf_dir)
            elif file.endswith(Pp):
                PpLen += 1
                move(root+'\\' + file, Pp_dir)
            elif file.endswith(exl):
                exlLen += 1
                move(root+'\\' + file, exl_dir)
            elif file.endswith(com):
                compLen += 1
                move(root+'\\' + file, zip_dir)
            elif file.endswith(app):
                appLen += 1
                move(root+'\\'+file, app_dir)
            else:
                otherLen += 1
                move(root+'\\'+file, other)
        except OSError as e:
            if file.endswith(vid):
                renombrar(os.path.join(root, file),file, video_dir)
            elif file.endswith(img):
                renombrar(os.path.join(root, file),file, img_dir)
            elif file.endswith(doc):
                renombrar(os.path.join(root, file),file, doc_dir)
            elif file.endswith(pdf):
                renombrar(os.path.join(root, file),file, pdf_dir)
            elif file.endswith(Pp):
                renombrar(os.path.join(root, file),file, Pp_dir)
            elif file.endswith(exl):
                renombrar(os.path.join(root, file),file, exl_dir)
            elif file.endswith(com):
                renombrar(os.path.join(root, file),file, zip_dir)
            elif file.endswith(app):
                renombrar(os.path.join(root, file),file, app_dir)
            else:
                renombrar(os.path.join(root, file),file, other)
            continue
    toast('Se ordenaron las descargas')

def crear_folders()->None:
    for folder in [video_dir, img_dir, doc_dir, zip_dir, pdf_dir, exl_dir, Pp_dir, app_dir, other]:
        if not os.path.exists(folder):
            toast(f'Creando folder: {folder}....')
            os.mkdir(folder)


def checar_y_organizar()->None:

    crear_folders()
    list_files()
    
    if len(files) >= 1:
        try:
            ordenar()
        except OSError as e:
            toast(f'Error: {e}')
            time.sleep(500)            
        finally: 
            files.clear()

    


def inicio()->None:
    while True:
        checar_y_organizar()
        time.sleep(250)


if __name__ == "__main__":
    inicio()

