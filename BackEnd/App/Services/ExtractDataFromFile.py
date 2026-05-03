import pandas as pd
import pdfplumber
from pathlib import Path
from io import BytesIO

    
#lecture du fichier a partir de son path
def parser_fichier(chemin: Path) -> pd.DataFrame:
    # Ensure file_path is a Path object
    chemin = Path(chemin) if not isinstance(chemin, Path) else chemin
    ext = chemin.suffix.lower()
    try:
        if ext == ".csv":
            df= pd.read_csv(chemin)
        elif ext in [".xlsx", ".xls"]:
            df=pd.read_excel(chemin)
        elif ext == ".pdf":
            df=parse_pdf(chemin)
        else:
        # fallback si pas d'extension
            try:
                return pd.read_csv(chemin)
            except:
                try:
                    return pd.read_excel(chemin)
                except:
                    raise ValueError("Format de fichier non reconnu")
        if df.empty:
            raise ValueError(f"Le fichier {ext} est vide")
        return df  
    except Exception as e:
        raise ValueError(f"Erreur lors de la lecture du fichier: {e}")
    
def parse_pdf(chemin: Path): # parser un fichier pdf en data frame
    data = []
    with pdfplumber.open(chemin) as pdf:
        for page in pdf.pages:
            data.extend(page.extract_table() or [])

    if not data:
        raise ValueError("Aucune table trouvée dans le fichier PDF")
 
    columns = data[0]
    # Dédupliquer les noms de colonnes
    seen = {}
    unique_columns = []
    for col in columns:
        col = str(col) if col else "column"
        if col in seen:
            seen[col] += 1
            unique_columns.append(f"{col}_{seen[col]}")
        else:
            seen[col] = 0
            unique_columns.append(col)

    return pd.DataFrame(data[1:], columns=unique_columns)
    
    
def parser_fichier_bytes(file_content: bytes, filename: str ) -> pd.DataFrame:
    # Ensure file_content is not empty and filename is provided
    if not file_content:
        raise ValueError("Le contenu du fichier est vide")
    if not filename:
        raise ValueError("Le nom du fichier est requis")
    # Determine file extension
    ext = Path(filename).suffix.lower()
    try:
        if ext == ".csv":
            df = pd.read_csv(BytesIO(file_content))
        elif ext in [".xlsx", ".xls"]:
            df=pd.read_excel(BytesIO(file_content))
        elif ext == ".pdf":
            df=parse_pdf_Bytes(BytesIO(file_content))
        else:
        # fallback si pas d'extension
            try:
                return pd.read_csv(BytesIO(file_content))
            except:
                try:
                    return pd.read_excel(BytesIO(file_content))
                except:
                    raise ValueError("Format de fichier non reconnu")
        if df.empty:
            raise ValueError(f"Le fichier {ext} est vide")
        return df  
    except Exception as e:
        raise ValueError(f"Erreur lors de la lecture du fichier: {e}")


def parse_pdf_Bytes(chemin: BytesIO): # parser un fichier pdf en data frame
    data = []
    with pdfplumber.open(chemin) as pdf:
        for page in pdf.pages:
            data.extend(page.extract_table() or [])

    if not data:
        raise ValueError("Aucune table trouvée dans le fichier PDF")
 
    columns = data[0]
    # Dédupliquer les noms de colonnes
    seen = {}
    unique_columns = []
    for col in columns:
        col = str(col) if col else "column"
        if col in seen:
            seen[col] += 1
            unique_columns.append(f"{col}_{seen[col]}")
        else:
            seen[col] = 0
            unique_columns.append(col)

    return pd.DataFrame(data[1:], columns=unique_columns)


# Verifier que le fichier fonctionne
# determoiner le type du fichier
