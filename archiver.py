import os
import shutil
from datetime import datetime

def archiver_log(chemin_source, dossier_backup):
    """
    Déplace le fichier log traité vers le dossier d'archivage.
    """
    try:
        if not os.path.exists(dossier_backup):
            os.makedirs(dossier_backup)

        nom_fichier = os.path.basename(chemin_source)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_archive = f"{timestamp}_{nom_fichier}"
        chemin_destination = os.path.join(dossier_backup, nom_archive)

        shutil.move(chemin_source, chemin_destination)
        print(f"Fichier archivé dans : {chemin_destination}")
        return True
    except Exception as e:
        print(f"Erreur lors de l'archivage : {e}")
        return False
