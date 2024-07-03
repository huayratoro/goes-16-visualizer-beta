import glob
from aux import goes
import matplotlib.pyplot as plt
import shutil; import os
import argparse
import multiprocessing

## ---- Manejador de argumentos de entrada
def rango_lats(valor):
    valor_int = float(valor)
    if valor_int < -51 or valor_int > -9:
        raise argparse.ArgumentTypeError(f"El valor {valor_int} debe estar en el rango de -50° a -10°")
    return valor_int
def rango_lons(valor):
    valor_int = float(valor)
    if valor_int < -88 or valor_int > -49:
        raise argparse.ArgumentTypeError(f"El valor {valor_int} debe estar en el rango de -88 a -51")
    return valor_int
parser = argparse.ArgumentParser(description="")
parser.add_argument("path", type=str)
parser.add_argument("ln", help="Lat north", type=rango_lats)
parser.add_argument("ls", help="Lat south", type=rango_lats)
parser.add_argument("lw", help="Lon west", type=rango_lons)
parser.add_argument("le", help="Lon east", type=rango_lons)
args = parser.parse_args()
## ----
path_proj = args.path # "../../../../../datos/casos-conv/malargue/proj/"
goes_im = sorted(glob.glob(path_proj + "*"))

## carpeta de guardado de imagenes
shutil.rmtree("backend/assets/goes_images/")
os.mkdir("backend/assets/goes_images/")

##---- generacion de imagenes

def process_image(im):
    f, ax = plt.subplots(1, 1, figsize=(10, 10))

    goes(ax, im, args.ln, args.ls, args.lw, args.le)

    ax.set_xlabel("Lon")
    ax.set_ylabel("Lat")

    nom = im.split("/")[-1].split(".")[0]
    plt.savefig(f"backend/assets/goes_images/{nom}.png", dpi=350, bbox_inches="tight")

if __name__ == "__main__":
    with multiprocessing.Pool(5) as p:
        p.map(process_image, goes_im)