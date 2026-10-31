import string


def calculer_score(mot_de_passe):
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

    return score


def evaluer_score(score):
    if score <= 2:
        return "A RENFORCER"
    elif score <= 4:
        return "MOYEN"
    else:
        return "CRITERES SATISFAITS"
