import os
from shutil import move
from pathlib import Path
from win11toast import toast


user_home = os.path.expanduser('~')
descargas_dir = 'Downloads'
root = os.path.join(user_home, descargas_dir)
video_dir = os.path.join(root, 'Videos')
img_dir = os.path.join(root, 'Imagenes')
doc_dir = os.path.join(root, 'Documentos')
pdf_dir = os.path.join(root, 'Pdf')
zip_dir = os.path.join(root, 'Zip')
exl_dir = os.path.join(root, 'Excel')
Pp_dir = os.path.join(root, 'Presentaciones')
app_dir = os.path.join(root, 'Ejecutables')
other = os.path.join(root, 'OtrosArchivos')
vid = ('.mp3', 'mkv', '.mov', '.m4a', '.mp4')
img = ('.png', '.jpeg', '.jpg', '.gif', '.svg', '.ico')
doc = ('.doc', '.txt', '.docx')
pdf = ('.pdf')
Pp = ('.ppt', '.pptx', '.pps', '.ppsx')
exl = ('.xls', '.xlsx')
com = ('.zip', '.rar')
app = ('.exe')
vidLen = 0
picLen = 0
docLen = 0
pdfLen = 0
PpLen = 0
exlLen = 0
compLen = 0
appLen = 0
otherLen = 0
files = []
def renombrar(src, filed, dst):
    filename, file_extension = os.path.splitext(filed)
    count = 1
    new_filename = filename + str(count) + file_extension


    while os.path.exists(os.path.join(dst, new_filename)):
        count += 1
        new_filename = filename+ str(count) + file_extension

    os.rename(src, os.path.join(dst,new_filename))

def list_files():


    for f in os.listdir(root):
        if not f.startswith('.') and not f.__eq__(__file__):
            # Verificar si f es una carpeta que debe ser ignorada
            folder_path = os.path.join(root, f)
        if folder_path in [video_dir, img_dir, doc_dir, pdf_dir, zip_dir, exl_dir, Pp_dir, app_dir, other]:
            continue
        files.append(f)


def ordenar():
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

def crear_folders():
    for folder in [video_dir, img_dir, doc_dir, zip_dir, pdf_dir, exl_dir, Pp_dir, app_dir, other]:
        if not os.path.exists(folder):
            toast(f'Creando folder: {folder}....')
            os.mkdir(folder)


def inicio():

    crear_folders()
    list_files()
    ordenar()
    return 1


inicio()
