from bs4 import BeautifulSoup

html ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemplos de Classes, IDs e Links</title>

    <style>
        .destaque{
            color: blue;
            font-size: bold;
        }

        #paragrafo {
            background-color: lightgrey;
            padding: 10px;
        }

    </style>

</head>
<body>

    <h1>Exemplo de Classes, IDs e Links</h1>

    <p>Aqui está um <span class="destaque">texto em destaque</span>.</p>

    <p id="paragrafo">Este é um paragrafo com ID. Ele tem um fundo cinza claro.</p>

    <p>Visite o <a href="http://www.exemplo.com">Exemplo.com</a>Para mais informações</p>
    
</body>
</html>
"""


# Encontrar texto em destaque

html_parsed = BeautifulSoup(html, "html.parser")
html_parsed.find(class_= "destaque")
