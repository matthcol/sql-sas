#!/usr/bin/env python3
"""
Script pour nettoyer les fichiers SVG exportés d'Excalidraw
Remplace les entités HTML non définies par leurs équivalents Unicode
"""

import sys
import re
from pathlib import Path

# Mapping des entités HTML courantes vers leurs codes Unicode
ENTITIES = {
    '&nbsp;': '&#160;',
    '&lt;': '&#60;',
    '&gt;': '&#62;',
    '&amp;': '&#38;',
    '&quot;': '&#34;',
    '&apos;': '&#39;',
}

def clean_svg(input_file, output_file=None):
    """
    Nettoie un fichier SVG en remplaçant les entités HTML
    
    Args:
        input_file: Chemin du fichier SVG à nettoyer
        output_file: Chemin du fichier de sortie (optionnel, écrase l'original si None)
    """
    input_path = Path(input_file)
    
    if not input_path.exists():
        print(f"Erreur: Le fichier {input_file} n'existe pas")
        return False
    
    # Lire le contenu
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Erreur lors de la lecture: {e}")
        return False
    
    # Remplacer les entités
    original_content = content
    for entity, unicode_code in ENTITIES.items():
        content = content.replace(entity, unicode_code)
    
    # Déterminer le fichier de sortie
    if output_file is None:
        output_path = input_path
    else:
        output_path = Path(output_file)
    
    # Écrire le résultat
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        if content != original_content:
            print(f"✓ Nettoyé: {input_path.name}")
            return True
        else:
            print(f"○ Aucune modification nécessaire: {input_path.name}")
            return True
    except Exception as e:
        print(f"Erreur lors de l'écriture: {e}")
        return False

def clean_directory(directory, pattern="*.svg"):
    """
    Nettoie tous les fichiers SVG d'un répertoire
    
    Args:
        directory: Répertoire à traiter
        pattern: Pattern de fichiers (défaut: *.svg)
    """
    dir_path = Path(directory)
    
    if not dir_path.is_dir():
        print(f"Erreur: {directory} n'est pas un répertoire")
        return
    
    svg_files = list(dir_path.glob(pattern))
    
    if not svg_files:
        print(f"Aucun fichier {pattern} trouvé dans {directory}")
        return
    
    print(f"Traitement de {len(svg_files)} fichier(s)...\n")
    
    success = 0
    for svg_file in svg_files:
        if clean_svg(svg_file):
            success += 1
    
    print(f"\n✓ {success}/{len(svg_files)} fichier(s) traité(s) avec succès")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python clean_excalidraw_svg.py fichier.svg")
        print("  python clean_excalidraw_svg.py fichier.svg sortie.svg")
        print("  python clean_excalidraw_svg.py dossier/")
        sys.exit(1)
    
    input_arg = sys.argv[1]
    input_path = Path(input_arg)
    
    if input_path.is_dir():
        # Traiter un répertoire
        clean_directory(input_arg)
    elif input_path.is_file():
        # Traiter un fichier unique
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        clean_svg(input_arg, output_file)
    else:
        print(f"Erreur: {input_arg} n'existe pas")
        sys.exit(1)

if __name__ == "__main__":
    main()