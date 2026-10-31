import getpass
from securecheck_core import calculer_score, evaluer_score

print("================================")
print("       SECURECHECK v1.0")
print("   Analyse de mot de passe")
print("================================")

mot_de_passe = getpass.getpass("Entrez un mot de passe a tester : ")

score = calculer_score(mot_de_passe)

print("\n--- Resultat de l'analyse ---")
print("Longueur :", len(mot_de_passe))
print("Criteres satisfaits :", score, "/ 5")
print("Evaluation :", evaluer_score(score))
print("Analyse terminee.")
