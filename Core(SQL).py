import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime
import uuid
import config

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']

from azure.cosmos import CosmosClient, PartitionKey
# Iniciar a conexão
client = CosmosClient(HOST, MASTER_KEY)
# GET banco de dados
database = client.get_database_client(DATABASE_ID)

# GET contêiner
container = database.get_container_client(CONTAINER_ID)

# Dados do documento (sem o campo 'id')
document_data = {
    'id': str(uuid.uuid4()),
    'nome': 'Dener Ottolini',
    'funcao': 'professor'
    
}
# Criar o documento (CREATE)
#created_document = container.create_item(body=document_data)
#print(f'Documento criado! ID: {created_document["id"]}')

#Selecionar os documentos (READ)
#query = "SELECT * FROM alunos"
#query_result = container.query_items(query, enable_cross_partition_query=True)
#for item in query_result:
 #   print(item)


#Atualizar os documentos (UPDATE)

#query = "SELECT * FROM alunos where alunos.nome ='John Doe'"
#query_result = container.query_items(query, enable_cross_partition_query=True)

#print(query_result['nome'])
# Porque dá erro?

#result = next(query_result, None)

#if result:
 #     print(result["nome"])
  #    document_to_update = container.read_item(item=result["id"], partition_key=result["id"])
   #   document_to_update["nome"] = "João das couves"
    #  updated_document = container.replace_item(item=document_to_update, body=document_to_update)
    
    
#else:
 #   print("Nenhum resultado encontrado.")


#Deletar os documentos (READ)
query = "SELECT * FROM alunos where alunos.nome ='João das couves'"
query_result = container.query_items(query, enable_cross_partition_query=True)
result = next(query_result, None)

if result:
      container.delete_item(item=result["id"], partition_key=result["id"])
      
    
    
else:
    print("Nenhum resultado encontrado.")


