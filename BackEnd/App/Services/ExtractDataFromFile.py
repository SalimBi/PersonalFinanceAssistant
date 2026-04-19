import pandas as pd
import pdfplumber
from pathlib import Path

    
#lecture du fichier a partir de son path
def parser_fichier(chemin: Path) -> pd.DataFrame:
    # Ensure file_path is a Path object
    chemin = Path(chemin) if not isinstance(chemin, Path) else chemin
    ext = chemin.suffix.lower()
    try:
        if ext == ".csv":
            return pd.read_csv(chemin)
        elif ext in [".xlsx", ".xls"]:
            return pd.read_excel(chemin)
        elif ext == ".pdf":
            return parse_pdf(chemin)

        # fallback si pas d'extension
        try:
            return pd.read_csv(chemin)
        except:
            try:
                return pd.read_excel(chemin)
            except:
                raise ValueError("Format de fichier non reconnu")
    except Exception as e:
        raise ValueError(f"Erreur lors de la lecture du fichier: {e}")

def parse_pdf(chemin: path): # parser un fichier pdf en data frame
    data = []
    with pdfplumber.open(chemin) as pdf:
        for page in pdf.pages:
            data.extend(page.extract_table() or [])

    if not data:
        raise ValueError("Aucune table trouvée dans le fichier PDF")

    return pd.DataFrame(data[1:], columns=data[0])


# Verifier que le fichier fonctionne
# determoiner le type du fichier
