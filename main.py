
import subprocess
import sys
from pathlib import Path

DOSSIER = Path(__file__).parent

PROGRAMMES = {
    "1": ("Leçon 1 - Variables", "jour01.py"),
    "2": ("Leçon 2 - Types de données", "jour02.py"),
    "3": ("SecureCheck - Sécurité", "securecheck.py"),
    "4": ("Exercice - Boucles", "exercice_boucle.py"),
}

while True:
    print("\n==============================")
    print("   FORMATION DEVSECOPS")
    print("==============================")

    for numero, (titre, fichier) in PROGRAMMES.items():
        print(f"{numero}. {titre}")

    print("0. Quitter")

    choix = input("\nChoisis un programme : ").strip()

    if choix == "0":
        print("À bientôt !")
        break

    if choix not in PROGRAMMES:
        print("Choix invalide. Réessaie.")
        continue

    titre, fichier = PROGRAMMES[choix]
    chemin = DOSSIER / fichier

    if not chemin.is_file():
        print(f"Fichier introuvable : {fichier}")
        continue

    print(f"\nLancement : {titre}\n")
    resultat = subprocess.run([sys.executable, str(chemin)])

    if resultat.returncode != 0:
        print("Le programme s'est terminé avec une erreur.")

    input("\nAppuie sur Entrée pour revenir au menu...")
