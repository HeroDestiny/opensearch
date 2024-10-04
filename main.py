import json
from opensearchpy import OpenSearch
from opensearchpy.helpers import bulk

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
# Criação do índice, se não existir
if not client.indices.exists(index=index_name):
    client.indices.create(index=index_name)
    print(f"Índice '{index_name}' criado.")
else:
    print(f"Índice '{index_name}' já existe.")

file_path = 'data.json'
# Lendo os dados do arquivo JSON
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)  # Carrega os dados do JSON

# Preparando os documentos para inserção
documents = [
    {'_index': 'contato', '_source': document} for document in data
]

# Inserindo os documentos em massa
success, _ = bulk(client, documents)
print(f"{success} documentos inseridos com sucesso.")

