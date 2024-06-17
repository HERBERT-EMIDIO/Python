#pip install pypdf2
#import 
import PyPDF2

#caminho do pdf
caminho_pdf_cv = r"C:\Users\Herbe\OneDrive\Desktop\Currículo\Cv_HerbertEmidioS.pdf"

#abri o arquivo

with open(caminho_pdf_cv, "rb") as arquivo:
    leitor_pdf_cv = PyPDF2.PdfReader(arquivo)
    texto = ""
    for paginas in leitor_pdf_cv.pages:
        texto += paginas.extract_text()
        
 
print("Leitura do PDF")
print(texto)        
