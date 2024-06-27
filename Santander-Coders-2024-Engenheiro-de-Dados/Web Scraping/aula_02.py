from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula 02 - web Scraping</title>
</head>
<body>

    <h1>Título - Aula 02 de web Scraping</h1>
    <h6>Subtitulo</h6>
    <p> Parágrafo 01</p>
    <p> Parágrafo 02</p>

    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>

    <ol>
        <li>Primeira</li>
        <li>Segunda</li>
    </ol>
    
</body>
</html>
'''

html_parsed = BeautifulSoup(html,"html.parser")


html_parsed

print(html_parsed.prettify())

# buscar: find() ou find_all()

html_parsed.find('h1') # Primerio objeto encontrado
html_parsed.find_all('h1') # Lista de Todos os elementos 


