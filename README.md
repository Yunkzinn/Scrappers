# Ferramenta de Obtenção de Informações sobre ASN

Esta ferramenta permite obter informações sobre Números de Sistemas Autônomos (ASNs) associados a uma empresa específica a partir do site [bgp.he.net](https://bgp.he.net/).

## Como Usar

1. **Clone o repositório para o seu ambiente local:**

   ```
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Instale as dependências:**

   ```
   pip install -r requirements.txt
   ```

3. **Execute o script:**

   ```
   python scrapper.py
   ```

Siga as instruções para inserir o nome da empresa e a ferramenta retornará os números de ASN associados.

O resultado será salvo em um arquivo de texto chamado `<NomeDaEmpresa>_ASNs.txt`

## Dependências

* Beautiful Soup
* Requests

## Contribuição
Sinta-se à vontade para contribuir para este projeto. Se encontrar problemas ou tiver sugestões de melhorias, abra uma issue ou envie um pull request.
