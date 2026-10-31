
import getpass
import string

print("================================")
print("       SECURECHECK v1.0")
print("   Analyse de mot de passe")
print("================================")

mot_de_passe = getpass.getpass("Entrez un mot de passe à tester : ")

score = 0

if len(mot_de_passe) >= 12:
    score += 1

if any(c.islower() for c in mot_de_passe):
    score += 1

if any(c.isupper() for c in mot_de_passe):
    score += 1

if any(c.isdigit() for c in mot_de_passe):
    score += 1

if any(c in string.punctuation for c in mot_de_passe):
    score += 1

print("\n--- Résultat de l'analyse ---")
print("Longueur :", len(mot_de_passe))
print("Critères satisfaits :", score, "/ 5")

if score <= 2:
    print("Évaluation : À RENFORCER")
elif score <= 4:
    print("Évaluation : MOYEN")
else:
    print("Évaluation : CRITÈRES SATISFAITS")

print("Analyse terminée.")
