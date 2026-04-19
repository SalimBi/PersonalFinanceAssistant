#Implement tests for the ExtractDataFromFile service.
import pytest
from PFA.BackEnd.App.Services.ExtractDataFromFile import parser_fichier

class TestExtractDataFromFile:
    #Test case for extracting data from a valid file of a report from bank account statement with different transactions for pdf
   # def test_extract_data_from_valid_pdf_file(self):
      #  file_path = "C:\Users\V3RY23O\Desktop\cv\git\PFA\BackEnd\Tests\Services\TestSample.pdf"  # Replace with actual path to a valid PDF file
     #   try:
            #data = parser_fichier(file_path)
          #  assert data is not None
        #    assert not data.empty  # Ensure that the extracted data is not empty
       # except Exception as e:
       #     pytest.fail(f"Unexpected error occurred: {e}")

    #Test case for extracting data from a valid file of a report from bank account statement with different transactions for xlsx
    def test_extract_data_from_valid_excel_file(self, mocker):
        file_path = "C:\\Users\\V3RY23O\\Desktop\\cv\\git\\PFA\\BackEnd\\Tests\\Services\\TestSample.xlsx"  # Replace with actual path to a valid Excel file
        mock_data = mocker.Mock()
        mock_data.empty = False
        mocker.patch("pandas.read_excel", return_value=mock_data)  # Mock pandas.read_excel
        
        try:
            data = parser_fichier(file_path)
            assert data is not None
            assert not data.empty  # Ensure that the extracted data is not empty
        except Exception as e:
            pytest.fail(f"Unexpected error occurred: {e}")

    #Test case for extracting data from a valid file of a report from bank account statement with different transactions for xls
    def test_extract_data_from_valid_xls_file(self):
        file_path = "C:\\Users\\V3RY23O\\Desktop\\cv\\git\\PFA\\BackEnd\\Tests\\Services\\TestSample.xls"  # Replace with actual path to a valid XLS file
        try:
            data = parser_fichier(file_path)
            assert data is not None
            assert not data.empty  # Ensure that the extracted data is not empty
        except Exception as e:
            pytest.fail(f"Unexpected error occurred: {e}")

    # Test case for extracting data from a valid file of a report from bank account statement with different transactions 
    def test_extract_data_from_valid_file(self):
        file_path = "C:\\Users\\V3RY23O\\Desktop\\cv\\git\\PFA\\BackEnd\\Tests\\Services\\TestSample.csv"  # Replace with actual path to a valid file
        try:
            data = parser_fichier(file_path)
            assert data is not None
            assert not data.empty  # Ensure that the extracted data is not empty
        except Exception as e:
            pytest.fail(f"Unexpected error occurred: {e}")
    
    # Test case for handling an invalid file path 
    def test_extract_data_from_invalid_file_path(self):
        file_path = "path/to/invalid/file.csv"  # Replace with actual path to an invalid file
        with pytest.raises(ValueError, match="Erreur lors de la lecture du fichier"):
            parser_fichier(file_path)
    
    # Test case for handling an unsupported file format
    def test_extract_data_from_unsupported_file_format(self):
        file_path = "C:\\Users\\V3RY23O\\Desktop\\cv\\git\\PFA\\BackEnd\\Tests\\Services\\TestSample.txt"  # Replace with actual path to an unsupported file
        with pytest.raises(ValueError, match="Format de fichier non reconnu"):
            parser_fichier(file_path)
    
    # Test case for handling an empty file
    def test_extract_data_from_empty_file(self):
        file_path = "C:\\Users\\V3RY23O\\Desktop\\cv\\git\\PFA\\BackEnd\\Tests\\Services\\TestSample.csv"  # Replace with actual path to an empty file
        with pytest.raises(ValueError, match="Aucune table trouvée dans le fichier PDF"):
            parser_fichier(file_path)
    
    # Test case for handling a file with no tables (for PDF)
    def test_extract_data_from_pdf_with_no_tables(self):
        file_path = "C:\\Users\\V3RY23O\\Desktop\\cv\\git\\PFA\\BackEnd\\Tests\\Services\\TestSample.pdf"  # Replace with actual path to a PDF with no tables
        with pytest.raises(ValueError, match="Aucune table trouvée dans le fichier PDF"):
            parser_fichier(file_path)

    # Test case for handling a file with invalid content
    def test_extract_data_from_file_with_invalid_content(self):
        file_path = "C:\\Users\\V3RY23O\\Desktop\\cv\\git\\PFA\\BackEnd\\Tests\\Services\\TestSample.csv"  # Replace with actual path to a file with invalid content
        with pytest.raises(ValueError, match="Erreur lors de la lecture du fichier"):
            parser_fichier(file_path)
    

  
     




    