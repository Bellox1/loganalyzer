import os
from datetime import datetime

def generer_rapport(stats, nom_log, dossier_sortie):
    """
    Génère un fichier de rapport à partir des statistiques.
    """
    try:
        if not os.path.exists(dossier_sortie):
            os.makedirs(dossier_sortie)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_rapport = f"rapport_{nom_log}_{timestamp}.txt"
        chemin_rapport = os.path.join(dossier_sortie, nom_rapport)

        with open(chemin_rapport, 'w') as f:
            f.write("="*40 + "\n")
            f.write(f" RAPPORT D'ANALYSE DE LOGS : {nom_log}\n")
            f.write(f" Généré le : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*40 + "\n\n")

            f.write(f"Total de lignes traitées : {stats['total_lignes']}\n\n")

            f.write("--- Top 5 des IP ---\n")
            for ip, count in stats['ips'].most_common(5):
                f.write(f"{ip:15} : {count} requêtes\n")
            
            f.write("\n--- Codes de Statut HTTP ---\n")
            for code, count in sorted(stats['status_codes'].items()):
                f.write(f"{code:15} : {count} occurrences\n")

            f.write("\n--- Pages les plus visitées ---\n")
            for page, count in stats['pages'].most_common(5):
                f.write(f"{page:30} : {count} vues\n")

        print(f"Rapport généré avec succès : {chemin_rapport}")
        return True
    except Exception as e:
        print(f"Erreur lors de la génération du rapport : {e}")
        return False
