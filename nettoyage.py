import pandas as pd
df = pd.read_csv("D:/VS Code/Clone/dc4_nettoyage_fichier_refesse_villain/test.csv")
df = df.drop(columns=['Series_reference', 'Suppressed', 'STATUS', 'UNITS', 'Magnitude', 'Subject', 'Group', 'Series_title_1', 'Series_title_3', 'Series_title_4', 'Series_title_5'])
df = df[df.Series_title_2.isin(["Credit", "Debit", "Services"])]
df.dropna(inplace=True)
df['id'] = range(1, len(df) + 1)
df.to_csv("result.csv", index=False)