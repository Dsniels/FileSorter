from genericpath import isfile
import os
from pydoc import doc
from shutil import move
from pathlib import Path
from turtle import st
from unratedwriting import typewrite


def inicio():
    try:
        typewrite('Iniciando programa')

        root = r"C:\Users\Dsnie\Downloads"
        video_dir = r"C:\Users\Dsnie\Downloads\Videos"
        img_dir = r"C:\Users\Dsnie\Downloads\Imagenes"
        doc_dir = r"C:\Users\Dsnie\Downloads\Documentos"
        pdf_dir = r"C:\Users\Dsnie\Downloads\Pdf"
        zip_dir = r"C:\Users\Dsnie\Downloads\Zip"
        exl_dir = r"C:\Users\Dsnie\Downloads\Excel"
        Pp_dir = r"C:\Users\Dsnie\Downloads\Presentaciones"
        app_dir = r"C:\Users\Dsnie\Downloads\apps"
        other = r"C:\Users\Dsnie\Downloads\otrosArchivos"

        for folder in [video_dir, img_dir, doc_dir, zip_dir, pdf_dir, exl_dir, Pp_dir, app_dir, other]:
            if not os.path.exists(folder):
                print(f'Creando folder: {folder}....')
                os.mkdir(folder)

        vid = ('.mp4', 'mkv', '.mov', '.m4a')
        img = ('.png', '.jpeg', '.jpg', '.gif', '.svg', '.ico')
        doc = ('.doc', '.txt', '.docx')
        pdf = ('.pdf')
        Pp = ('.ppt', '.pptx', '.pps')
        exl = ('.xls', '.xlsx')
        com = ('.zip', '.rar')
        app = ('.exe')

        files = []

        for f in os.listdir(root):
            if not f.startswith('.') and not f.__eq__(__file__):
            # Verificar si f es una carpeta que debe ser ignorada
                folder_path = os.path.join(root, f)
            if folder_path in [video_dir, img_dir, doc_dir, pdf_dir, zip_dir, exl_dir, Pp_dir, app_dir, other]:
                continue
            files.append(f)


        vidLen = 0
        picLen = 0
        docLen = 0
        pdfLen = 0
        PpLen = 0
        exlLen = 0
        compLen = 0
        appLen = 0
        otherLen = 0

        for file in files:

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

        if not vidLen == 0:
            typewrite('Se movieron ' + str(vidLen) + ' videos!')
        if not picLen == 0:
            typewrite('Se movieron ' + str(picLen)+' fotos!')
        if not pdfLen == 0:
            typewrite('Se movieron ' + str(pdfLen)+' Pdf!')
        if not docLen == 0:
            typewrite('Se movieron ' + str(docLen)+' Documentos!')
        if not PpLen == 0:
            typewrite('Se movieron ' + str(PpLen)+' Presentaciones!')
        if not exlLen == 0:
            typewrite('Se movieron ' + str(exlLen)+' Excel!')
        if not compLen == 0:
            typewrite('Se movieron ' + str(compLen)+' comprimidos!')

        total = vidLen + picLen + pdfLen + docLen + \
            exlLen + PpLen + compLen + appLen + otherLen

        print('Se movieron un total de ' + str(total) + 'archivos')
        typewrite('El programa se ejecuto sin errores')
        return 1
    except OSError as e:
        print("Error:", e.strerror)
        return 0


inicio()
