import psycopg2

# Substitua pelos valores reais do seu ambiente Cosmos DB PostgreSQL
host = "c-brqpostgres.m3t2qhoxklh24n.postgres.cosmos.azure.com"
database = "brq"
user = "citus"
password = "BRQ@1234"

#

#CREATE TABLE users ( id SERIAL PRIMARY KEY, username VARCHAR(100), nome VARCHAR(100), funcao VARCHAR(100));
def connect():
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        return connection
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Criar o documento (CREATE)
def create_user(username, nome, funcao):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            insert_query = "INSERT INTO users (username, nome, funcao) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (username, nome, funcao))
            connection.commit()
            print("Usuário criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
    finally:
        if connection:
            connection.close()

# Criar o documento (READ)
def read_users():
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            select_query = "SELECT * FROM users"
            cursor.execute(select_query)
            users = cursor.fetchall()
            for user in users:
                print(user)
    except Exception as e:
        print(f"Erro ao ler usuários: {e}")
    finally:
        if connection:
            connection.close()

# Criar o documento (UPDATE)
def update_funcao(username, new_funcao):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            update_query = "UPDATE users SET funcao = %s WHERE username = %s"
            cursor.execute(update_query, (new_funcao, username))
            connection.commit()
            print("Usuário atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
    finally:
        if connection:
            connection.close()

# Criar o documento (DELETE)
def delete_user(username):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            delete_query = "DELETE FROM users WHERE username = %s"
            cursor.execute(delete_query, (username,))
            connection.commit()
            print("Usuário excluído com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir usuário: {e}")
    finally:
        if connection:
            connection.close()

#Testando nosso código:
#create_user("couveloka89","João das couves", "professor")
read_users()
#escreva uma função que faz a seleção por ID
#update_funcao("couveloka89", "aluno")
#delete_user("couveloka89")