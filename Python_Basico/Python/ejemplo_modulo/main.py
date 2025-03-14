"""
Maneras de importar
"""

# import edad as ed

# print(ed.calcula_edad("18-02-2000","18-02-2025"))

from edad import calcula_edad as ce
print(range.__doc__)
if __name__ == "__main__": # Bloquea el fichero y no se puede importar el fichero desde otro lado
    print(ce("18-02-2000","18-02-2025"))
    print(ce.__doc__) # doc es una funcion preparada en python que muestra los comentarios de la funcion