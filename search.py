from opensearchpy import OpenSearch
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.filterwarnings('ignore', category=InsecureRequestWarning)

# Configurações de conexão
host = 'localhost'  # ou o endereço do seu cluster
port = 9200         # porta padrão
auth = ('admin', 'MyS3cure@Password!')  # se necessário

# Criação do cliente
client = OpenSearch(
    hosts=[{'host': host, 'port': port}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=False  # Para ambientes de desenvolvimento, em produção deve ser True
)

# Verificação da conexão
if client.ping():
    print("Conectado ao OpenSearch!")
else:
    print("Não foi possível conectar ao OpenSearch.")

index_name = 'contato'
print("--------------------")

# Realizando uma busca simples
response = client.search(
    index=index_name, 
    body={
        'query': {
            'match_all': {}
            }
        }
    )
print(f"Total de registros encontrados: {response['hits']['total']['value']}")
print("--------------------")

# Realizando uma busca com filtro
response = client.search(
    index=index_name, 
    body={
        'query': {
            'match': {
                'region': 'São Paulo'
                }
            }
        }
    )
print(f"Total de registros encontrados: {response['hits']['total']['value']}")
print("--------------------")

# Realizando uma inserção
response = client.index(
    index=index_name,
    body={
        'name': 'Luscas Silva',
        'email': 'lucas@gmail.com',
        'phone': '(84) 99999-9999',
        'region': 'Rio Grande do Norte'
        }
)
print(f"Documento inserido com sucesso: {response['_id']}")
print("--------------------")

#Procurando um documento específico
response = client.get(
    index=index_name,
    id=response['_id']
)
print(f"Documento encontrado: {response['_source']}")
print("--------------------")

# Atualizando um documento
response = client.update(
    index=index_name,
    id=response['_id'],
    body={
        'doc': {
            'name': 'Lucas Silva'
        }
    }
)
print(f"Documento atualizado com sucesso: {response['_id']}")
print("--------------------")

# Deletando um documento
response = client.delete(
    index=index_name,
    id=response['_id']
)
print(f"Documento deletado com sucesso: {response['_id']}")
print("--------------------")