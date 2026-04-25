import os
import re
from collections import Counter

def analyser_logs(chemin_fichier):
    """
    Analyse un fichier de log et retourne des statistiques.
    Supporte le format Common Log Format (CLF).
    """
    if not os.path.exists(chemin_fichier):
        print(f"Erreur : Le fichier {chemin_fichier} n'existe pas.")
        return None

    stats = {
        'total_lignes': 0,
        'ips': Counter(),
        'status_codes': Counter(),
        'pages': Counter()
    }

    # Regex pour extraire IP, code de statut et page
    # Format simplifié : IP - - [Date] "Method Page Protocol" Status Size
    log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?"\w+ (?P<page>.*?) .*?" (?P<status>\d+) \d+')

    try:
        with open(chemin_fichier, 'r') as f:
            for ligne in f:
                stats['total_lignes'] += 1
                match = log_pattern.search(ligne)
                if match:
                    stats['ips'][match.group('ip')] += 1
                    stats['status_codes'][match.group('status')] += 1
                    stats['pages'][match.group('page')] += 1
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None

    return stats
