
<body>
    <img src="https://raw.githubusercontent.com/guedes2142/url-curta-CLI/main/Screenshot%20from%202023-06-12%2014-07-00.png" alt="">
</body>
</html>
# URL Curta

Este é um programa Python que permite encurtar URLs usando a biblioteca `pyshorteners`. O programa solicita ao usuário uma URL completa, incluindo `http://` ou `https://`, e retorna a versão encurtada da URL usando o serviço TinyURL.

## Requisitos

Antes de executar o programa, certifique-se de ter as seguintes dependências instaladas:

- `pyshorteners`
- `colorama`

Você pode instalar as dependências executando o seguinte comando:

```
pip install pyshorteners colorama
```

## Como usar

Siga as etapas abaixo para executar o programa:

1. Clone o repositório ou faça o download dos arquivos em seu sistema.
2. Certifique-se de ter as dependências instaladas.
3. Execute o arquivo `url_curta.py` usando o Python:

   ```
   python url_curta.py
   ```

4. O programa será iniciado e exibirá o logotipo e o prompt de entrada.
5. Insira a URL completa (incluindo `http://` ou `https://`).
6. O programa irá encurtar a URL usando o serviço TinyURL e exibirá a versão encurtada.
7. O programa irá perguntar se você deseja continuar encurtando URLs. Digite 's' para continuar ou qualquer outra tecla para sair do programa.

## Notas

- O programa detectará automaticamente o sistema operacional em que está sendo executado e usará os comandos corretos para limpar a tela. No entanto, se você encontrar problemas ao limpar a tela, pode ser necessário ajustar o código manualmente para se adequar ao seu sistema operacional.

- Certifique-se de ter uma conexão de internet ativa ao executar o programa, pois ele precisa se comunicar com o serviço TinyURL para encurtar as URLs.

- Este programa foi escrito usando Python 3.

---
