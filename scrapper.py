import requests
from bs4 import BeautifulSoup

# Função para imprimir o desenho ASCII "ASN GRABBER"
def imprimir_banner():
    banner = """
            _____ _   _       _____ _____            ____  ____  ______ _____  
     /\    / ____| \ | |     / ____|  __ \     /\   |  _ \|  _ \|  ____|  __ \ 
    /  \  | (___ |  \| |    | |  __| |__) |   /  \  | |_) | |_) | |__  | |__) |
   / /\ \  \___ \| . ` |    | | |_ |  _  /   / /\ \ |  _ <|  _ <|  __| |  _  / 
  / ____ \ ____) | |\  |    | |__| | | \ \  / ____ \| |_) | |_) | |____| | \ \ 
 /_/    \_\_____/|_| \_|     \_____|_|  \_\/_/    \_\____/|____/|______|_|  \_|
 
 Developed by Yunkzinn                                                                                                                                                             
    """

    print(banner)

def obter_informacoes_asn(nome_empresa):
    # URL do site
    url = f"https://bgp.he.net/search?search%5Bsearch%5D={nome_empresa}&commit=Search"

    # Enviar uma requisição GET para o site
    response = requests.get(url)

    if response.status_code == 200:
        # Parsear o conteúdo da página usando BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar as informações sobre ASN na página
        asn_infos = []
        for row in soup.find_all('tr'):
            cells = row.find_all('td')

            # Verificar se a linha contém informações sobre ASN
            if len(cells) == 3:
                tipo = cells[1].text.strip()
                descricao = cells[2].text.strip()

                # Verificar se a descrição contém o nome da empresa e o tipo é ASN
                if nome_empresa.lower() in descricao.lower() and tipo == 'ASN':
                    asn = cells[0].text.strip()
                    asn_infos.append({'ASN': asn, 'Tipo': tipo, 'Descricao': descricao})

        return asn_infos
    else:
        print(f"Erro ao acessar o site. Código de status: {response.status_code}")
        return None

# Imprimir o banner quando o script é executado
imprimir_banner()

# Solicitar nome da empresa ao usuário
nome_empresa = input("Digite o nome da empresa: ")

# Obter informações sobre ASN
informacoes_asn = obter_informacoes_asn(nome_empresa)

if informacoes_asn:
    # Salvar os números das ASNs em um arquivo de texto
    nome_arquivo = f"{nome_empresa}_ASNs.txt"
    with open(nome_arquivo, 'w') as arquivo:
        for info in informacoes_asn:
            linha = f"{info['ASN']}\n"
            arquivo.write(linha)

    print(f"Os números das ASNs foram salvos em {nome_arquivo}.")
else:
    print("Não foi possível obter informações sobre ASN.")
