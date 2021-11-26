import re
import gdb

############################################################################################
# SKELETON FOR PRETTY PRINTING 2D MATRICES
# ITS OPTIONAL TO USE THIS SKELETON.
# Nothing much is given here anyways :p
############################################################################################
class Mat2DPrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        """
        Use the self.val to decode the 2D Matrix into
        the demanded format (check sample output in PS)
        """
        str_list = list()
        rows, cols = (0, 0) # get the rows and columns from val somehow
        rows = self.val.type.range()[1]+1
        cols = self.val.dereference().type.range()[1]+1
        str_list.append(f"ROWS: {rows}")
        str_list.append(f"COLUMNS: {cols}")

        for i in range(rows):
            temprow = "" # get the rows into a temporary string
            for j in range(cols):
                temprow += str((self.val.dereference().dereference().address+i*cols+j).dereference()) + " " 
            str_list.append(temprow)
        
        return '\n' + '\n'.join(str_list) 
        

def array2d_printer(val):
    if bool(re.match(r"^int \[([0-9]+)\]\[([0-9]+)\]$",str(val.type))):  # maybe use regex?
        return Mat2DPrinter(val)
    return None
# 

gdb.pretty_printers.append(array2d_printer)
############################################################################################


"""
█ ▀ █▀▄▀█   █▀█ █▀█ █▀▀ ▀█▀ ▀█▀ █▄█ ▀█
█ ░ █░▀░█   █▀▀ █▀▄ ██▄ ░█░ ░█░ ░█░ ░▄
⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
"""

