

def solution_station_5(name):
    #since it's only first names, there are some duplicates. Womp womp.
    name_lt = {'Aya': 5, 'Bissola': 1, 'Shriya': 5, 'Ava': 1,
               'Sean': 2, 'Maja': 2, 'Gadis': 3, 'Dorottya': 4,
               'Lotte': 4, 'Gabriella': 3, 'Alejandro': 3,
               'Emma': 2, 'Rasmus': 1, 'Lumi': 5, 'Christal': 1,
               'Irene': 2, 'Anouk': 5, 'Volodymyr': 4, 'Catherin': 1,
               'Alva': 4, 'Roy': 3, 'Nikko': 3, 'Ana': 2, 'Walter': 5,
               'Brendan': 4, 'Joeben': 5, 'Philine': 1, 'Maria': 1,
               'Farah': 1, 'Alexandru': 2, 'Wentao': 3, 'Felicia': 3,
               'Jacco': 2, 'Callum': 4, 'Ömer': 2, 'Kimiya': 2,
               'mirre': 1, 'Davide': 5, 'Leon': 5, 'Micay': 3,
               'Andre': 2, 'Calson': 5, 'Adam': 1, 'Elnara': 3,
               'Angela': 4, 'Mana': 3, 'Khushi': 4, 'Regina': 4,
               'Ilias': 5, 'Danielius': 4, 'Sophia': 5, 'Scarlett': 1,
               'Sina': 3, 'Anna': 1, 'Markus': 5, 'Maximilian': 1,
               'Tadas': 3, 'Akira': 4, 'Jamie': 2, 'Daniel': 3,
               'David': 1, 'Noel': 4, 'Yujia': 2, 'Gabriela': 4,
               'Rafael': 1, 'Josy': 1, 'Kazuya': 4, 'Lucas': 5,
               'Koyo': 2, 'Alexia': 3, 'Viktor': 3, 'Dasha': 5,
               'Clement': 3, 'Viggo': 2, 'Thaïss': 5, 'Diogo': 3,
               'Gaspar': 3, 'Abhijit': 1, 'Asjfaaq': 4, 'Alexandra': 3,
               'Cem': 4, 'Federico': 2, 'Nia': 1, 'Melody': 2, 'Bianka': 5,
               'Porter': 1, 'Nojus': 1, 'Emilie': 5, 'Lucia': 2, 'Mark': 3,
               'Antonín': 4, 'Niki': 4, 'Antonio': 4, 'Merijn': 3,
               'Juliette': 2, 'Bey': 5, 'Weizhao': 2, 'Collins': 1,
               'Wu': 5, 'Derrick': 2, 'Sihun': 3, 'In': 2,
               'Shuting': 4, 'Marwan': 4, 'Meng': 1, 'Fleming': 5}
    return name_lt[name]
    
