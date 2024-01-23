from pandas import read_csv, concat

X = concat([
    read_csv('winequality-red.csv', sep=';').assign(red=True),
    read_csv('winequality-white.csv', sep=';').assign(red=False)
], axis=0)

X.columns = [
    'kwasowość',
    'lotna kwasowość',
    'kwas cytrynowy',
    'pozostały cukier',
    'wolne chlorki',
    'dwutlenek siarki',
    'dwutlenek siarki całkowity',
    'gęstość',
    'pH',
    'siarczany',
    'alkohol',
    'jakość',
    'czerwone'
]

X.to_csv('wino.csv', index=False)