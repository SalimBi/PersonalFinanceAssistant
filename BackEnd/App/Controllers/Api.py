from fastapi import  HTTPException, FastAPI
from BackEnd.App.Services.ExtractDataFromFile import parser_fichier


app = FastAPI() # Create a FastAPI instance
@app.get("/") # Define a GET endpoint at the root URL
def read_root():
    return {"message": "Welcome to the API!"}

@app.get("/getMessage") # Define a GET endpoint at /getMessage
def get_message():
    try:
        return {"message": "Hello, World!"} # Return a JSON response with a message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/getMessage/{name}") # Define a GET endpoint at /getMessage    
def get_message(name=""):
    try:
        return {f"Hello {name.upper()}"} # Return a JSON response with a message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/getFileParsed/{chemin}") # Define a GET endpoint at /getFileParsed
def get_file_parsed(chemin):
    try:
        return parser_fichier(chemin)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
