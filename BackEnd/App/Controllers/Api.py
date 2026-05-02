from fastapi import HTTPException, FastAPI,UploadFile, Query, File
from fastapi.responses import Response
from BackEnd.App.Services.ExtractDataFromFile import parser_fichier
from BackEnd.App.Services.AsureBlobServices import azureBlobUpload,azureBlobGet
 
 
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
   
@app.get("/getFileParsed") # Define a GET endpoint at /getFileParsed
def get_file_parsed(chemin: str = Query(..., description="Chemin du fichier à parser")):
    try:
        data = parser_fichier(chemin)
        json_str = data.to_json(orient="records", force_ascii=False)
        return Response(content=json_str, media_type="application/json")
       
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
   
 # create an api to upload file to azure blob storage and return the url of the file
@app.put("/uploadFile") # Define a PUT endpoint at /uploadFile
def upload_file(file: UploadFile = File(...)):
    #put the file in azure blob storage and return the url of the file
    data = azureBlobUpload(file) 
    return data
@app.get("/azureStFiles") # Define a PUT endpoint at /uploadFile
def get_files():
    #put the file in azure blob storage and return the url of the file
    data = azureBlobGet() 
    return data