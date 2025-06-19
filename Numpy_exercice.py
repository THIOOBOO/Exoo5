import numpy as np

# Ouvrir le fichier CSV avec open() et le passer à genfromtxt
with open('Loan_prediction_dataset.csv', 'r', encoding='utf-8') as f:
    data = np.genfromtxt(f, delimiter=',', skip_header=1, dtype=str)

# Extraire la colonne LoanAmount (index 8) et convertir en float si possible
loan_amounts = []
for row in data:
    try:
        loan_amounts.append(float(row[8]))
    except ValueError:
        continue  # Ignorer les valeurs manquantes ou non numériques

loan_amounts = np.array(loan_amounts)

# Calculs statistiques
mean_loan = np.mean(loan_amounts)
median_loan = np.median(loan_amounts)
std_loan = np.std(loan_amounts)

# Affichage
print("Moyenne des prêts :", mean_loan)
print("Médiane des prêts :", median_loan)
print("Écart type des prêts :", std_loan)
