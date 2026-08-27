from random import shuffle
import pandas as p
import matplotlib.pyplot as mpl

so = ['Windows'] * 22 + ['Linux'] * 14  + ['macOS'] * 8 + ['Android'] * 5 + ['iOS'] * 1
shuffle(so)

users = {
    'SO': so,
    'User': ['Korra', 'Toph', 'Kiyoshi', 'Aang', 'Zuko', 'Katara', 'Azula', 'Iroh', 'Vaatu', 'Raava', 'Ko', 'Sokka', 'Maomao', 'Jinshi', 'Jade', 'Erza', 'Bahal', 'Natsu', 'Grey', 'Kenshi', 'Itadori', 'Nobara', 'Gokuyou', 'Tania', 'Yuru', 'Edward', 'Alphonse', 'Winry', 'Lakan', 'Levi', 'Himmel', 'Fern', 'Frieren', 'Soifon', 'Ichigo', 'Megumi', 'Yuta', 'Maki', 'Asa', 'Hohenheim', 'Huges', 'Mustang', 'Hawkaye', 'Izumi', 'Armstrong', 'Xing', 'Inousuke', 'Urokodaki', 'Noé', 'Vanitas']
}

df = p.DataFrame(users)