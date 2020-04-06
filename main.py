import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

un_panda = [100, 5, 20, 80]
un_panda_numpy = np.array(un_panda)


print(un_panda_numpy/2)


famille_panda = [
    [100, 5, 20, 80],  # maman panda
    [50, 2.5, 10, 40],  # bébé panda
    [110, 6, 22, 80]  # papa panda
]

famille_panda_numpy = np.array(famille_panda)

print("Famille panda")
print(famille_panda)
print(famille_panda[2][0])

print("Famille panda numpy")
print(famille_panda_numpy)
print(famille_panda_numpy[2, 0])


# : signifie "tous"
print("tous les pandas")
pattes = famille_panda_numpy[:, 0]
print(pattes)
# somme des elements d'un array
print("Somme des éléments d'un array")
print(pattes.sum())

# Utilisation de la librairie panda
famille_panda_df = pd.DataFrame(famille_panda_numpy, index=[
                                'maman', 'bebe', 'papa'], columns=['pattes', 'poils', 'queue', 'ventre'])


print(famille_panda_df)

print("affichage de la queue pour chaque membre de la famille panda")
print(famille_panda_df.queue)

print("Affichage de chaque panda de la famille")
for ligne in famille_panda_df.iterrows():
    index_ligne = ligne[0]
    contenu_ligne = ligne[1]
    print("Voici le panda %s :" % index_ligne)
    print(contenu_ligne)
    print("--------------------")

# Avec iloc(), indexation positionnelle
print(famille_panda_df.iloc[2])
# pattes    110.0
# poil        6.0
# queue      22.0
# ventre     80.0
# Name: papa, dtype: float64

# Avec loc(), indexation par label
print(famille_panda_df.loc["papa"])
# pattes    110.0
# poil        6.0
# queue      22.0
# ventre     80.0
# Name: papa, dtype: float64

# Lire fichier csv
mps = pd.read_csv("current_mps.csv", sep=";")

# affichage de la première ligne du fichier csv
# print(mps.iloc[0])


# Classe de députés
class SetOfParliamentMembers:
    def __init__(self, name):
        self.name = name

    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";")

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def total_mps(self):
        return len(self.dataframe)

    def display_chart(self):
        data = self.dataframe
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]

        counts = [len(female_mps), len(male_mps)]
        counts = np.array(counts)
        nb_mps = counts.sum()
        proportions = counts / nb_mps

        labels = ["Female ({})".format(counts[0]),
                  "Male ({})".format(counts[1])]

        fig, ax = plt.subplots()
        ax.axis("equal")
        ax.pie(
            proportions,
            labels=labels,
            autopct="%1.1f pourcents"
        )
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()

    def split_by_political_party(self):
        result = {}
        data = self.dataframe

        all_parties = data["parti_ratt_financier"].dropna().unique()

        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers(
                'MPs from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result


def launch_analysis(data_file, by_party=False, info=False):
    sopm = SetOfParliamentMembers("All MPs")
    sopm.data_from_csv(os.path.join("data", data_file))
    sopm.display_chart()

    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()

    if info:
        print(sopm.total_mps())


launch_analysis("current_mps.csv")
