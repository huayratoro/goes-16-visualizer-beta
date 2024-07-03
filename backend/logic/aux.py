import numpy as np

def encontrar_valor_mas_cercano(array, numero):
    """
    Encuentra el valor más cercano en un array al número dado.

    Args:
        array (numpy.ndarray): El array de valores.
        numero (float): El número para el cual queremos encontrar el valor más cercano.

    Returns:
        float: El valor más cercano en el array al número dado.
    """
    # Calcula las diferencias entre los valores del array y el número dado
    diferencias = np.abs(array - numero)
    
    # Encuentra el índice del valor más cercano
    indice_mas_cercano = np.argmin(diferencias)
    
    # Devuelve el valor más cercano
    return array[indice_mas_cercano]

def goes(ax, goes_path, ln, ls, lw, le):

    import xarray as xr
    import matplotlib.pyplot as plt
    from barra_goes16_IR import loadCPT
    from matplotlib.colors import LinearSegmentedColormap
    import geopandas as gpd
    import pandas as pd

    # Converts the CPT file to be used in Python
    cpt = loadCPT('backend/logic/IR4AVHRR6.cpt')
    # Makes a linear interpolation with the CPT file
    cmap_goes = LinearSegmentedColormap('cpt', cpt)

    sudam = gpd.read_file("backend/db/sudamerica.geojson")

    data = xr.open_dataset(goes_path)

    data.tbrillo.plot(ax = ax, add_colorbar=False, vmin = 170, vmax = 378, cmap = cmap_goes)

    sudam.plot(facecolor="None", edgecolor = "blue", lw = 0.2, ax = ax)

    ax.scatter(-69.585802, -35.461653, marker = "*", s = 50, color = "goldenrod", edgecolors = "black")

    # Para gestionar las horas

    year = str(pd.to_datetime(data.tbrillo.time.values[0]).year)
    month = "%02d" % pd.to_datetime(data.tbrillo.time.values[0]).month
    day = "%02d" % pd.to_datetime(data.tbrillo.time.values[0]).day
    
    hora = "%02d" % pd.to_datetime(data.tbrillo.time.values[0]).hour
    minutes = "%02d" %  pd.to_datetime(data.tbrillo.time.values[0]).minute
    hora_min = '{}-{}-{} T {}:{} UTC'.format(year, month, day, hora, minutes)
    ax.set_title(hora_min)

    ax.set_xlim(lw, le)
    ax.set_ylim(ls, ln)

    return ax

