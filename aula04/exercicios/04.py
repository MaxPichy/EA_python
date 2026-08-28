import pandas as p
import numpy
import matplotlib.pyplot as mpl

res_time = numpy.random.randint(100, 525, 50)

serie = p.Series(res_time)
frequencia = serie.value_counts().sort_index()

print(frequencia)
mpl.hist(res_time, bins = 15)
mpl.show()
