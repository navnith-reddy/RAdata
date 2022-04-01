import os

list = os.listdir('Data')

for x in list:
    x = 'Data/' + x
    new = x + 'x'
    os.rename(x, new)
    

    


