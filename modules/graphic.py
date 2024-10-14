from pandas import *
from matplotlib.pyplot import *

def create_graphic(value, color, title, count_value):
    data = DataFrame(value)
    graphic = data.plot.bar(color = color)
    graphic.set_title(title)
    savefig('graphic.png', dpi = 300)
    show()
    