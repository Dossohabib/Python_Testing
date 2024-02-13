import json
import os.path

def ajouter_ticket(nom_club, nom_competition, nb_ticket):
    # Nom du fichier JSON
    fichier_json = "tickets.json"

    # Vérifier si le fichier JSON existe
    if os.path.exists(fichier_json):
        # Si le fichier existe, on le charge
        with open(fichier_json, "r") as f:
            data = json.load(f)
        
        # Vérifier si le club a déjà des tickets pour cette compétition
        for club in data:
            if club["nom"] == nom_club and club["competition"] == nom_competition:
                # Si oui, ajouter le nombre de tickets si la limite n'est pas dépassée
                if club["nb_ticket"] + nb_ticket <= 12:
                    club["nb_ticket"] += nb_ticket
                    # Enregistrer les données mises à jour dans le fichier JSON
                    with open(fichier_json, "w") as f:
                        json.dump(data, f, indent=4)
                    return True  # Succès : ajout des tickets effectué
                else:
                    return False  # Échec : limite de tickets dépassée
                break
        else:
            # Si non, ajouter une nouvelle entrée si la limite n'est pas dépassée
            if nb_ticket <= 12:
                data.append({"nom": nom_club, "competition": nom_competition, "nb_ticket": nb_ticket})
                # Enregistrer les données mises à jour dans le fichier JSON
                with open(fichier_json, "w") as f:
                    json.dump(data, f, indent=4)
                return True  # Succès : ajout des tickets effectué
            else:
                return False  # Échec : limite de tickets dépassée
    else:
        # Si le fichier n'existe pas, créer une nouvelle liste de clubs avec leurs tickets si la limite n'est pas dépassée
        if nb_ticket <= 12:
            data = [{"nom": nom_club, "competition": nom_competition, "nb_ticket": nb_ticket}]
            # Enregistrer les données dans un nouveau fichier JSON
            with open(fichier_json, "w") as f:
                json.dump(data, f, indent=4)
            return True  # Succès : ajout des tickets effectué
        else:
            return False  # Échec : limite de tickets dépassée

