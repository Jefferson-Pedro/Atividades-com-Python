import psycopg2

class BancoDeDados:

    def __init__(self):
        self.conexao()

    def conexao(self):
        conn = psycopg2.connect(database="Exercicio_Avaliativo_AV",user="postgres",password="123456",port="5432")
        print("Conexão com o Banco de Dados aberta com sucesso!")
        comando = conn.cursor()

        try:
            comando.execute(
                """ CREATE TABLE IF NOT EXISTS teste.tb_users(
                    id integer NOT NULL,
                    nome character varying(50) COLLATE pg_catalog."default" NOT NULL,
                    email character varying(50) COLLATE pg_catalog."default" NOT NULL,
                    telefone character varying(12) COLLATE pg_catalog."default" NOT NULL,
                    username character varying(50) COLLATE pg_catalog."default" NOT NULL,
                    senha character varying(50) COLLATE pg_catalog."default" NOT NULL,
                    CONSTRAINT tb_users_pkey PRIMARY KEY (id)); """
            )
            conn.commit()
            print("Tabela criada com sucesso no BD!!!")
        except  ConnectionError:
            print('Erro ao criar a tabela.')
        finally:
            conn.close()

    def inserirDados(self, nome, email,telefone, username, senha):
        conn = psycopg2.connect(database="Exercicio_Avaliativo_AV", user="postgres", password="123456", port="5432")
        comando = conn.cursor()
        try:
            comando_sql =   """ INSERT INTO teste.tb_users(nome, email, telefone, username, senha) 
                                VALUES (%s, %s, %s, %s, %s); """
            valores = (nome,email,telefone,username,senha)
            comando.execute(comando_sql, valores)
            conn.commit()
        except  ConnectionError:
            print('Erro ao inserir dados.')
        finally:
            conn.close()

    def lerDados(self):
        conn = psycopg2.connect(database="Exercicio_Avaliativo_AV", user="postgres", password="123456", port="5432")
        comando = conn.cursor()
        try:
            comando.execute('SELECT "id", nome, email, username, telefone FROM teste.tb_users')
            #comando.execute('SELECT * FROM teste.tb_users')
            read_db = comando.fetchall()
            conn.commit()
            for line in read_db:
                print('Resultado:', line)
            return read_db # Retorna os dados obtidos da consulta

        except Exception as e:
            print(f'Erro ao retornar com os dados: {str(e)}')
            return []  # Retorna uma lista vazia em caso de erro
        finally:
            conn.close()

    def atualizarDados(self, nome, email, telefone, username, senha, id):
        conn = psycopg2.connect(database="Exercicio_Avaliativo_AV", user="postgres", password="123456", port="5432")
        comando = conn.cursor()
        try:
            comando_sql = """UPDATE teste.tb_users SET nome= %s, email= %s, telefone= %s, username= %s, senha= %s
                            WHERE "id" = %s """
            valores = (nome, email, telefone, username, senha, id)
            comando.execute(comando_sql, valores)
            conn.commit()
        except  ConnectionError:
            print('Erro ao atualizar dados. Verifique os dados passados e tente novamente.')
        finally:
            conn.close()

    def deletarDados(self, id):
        if id:
            conn = psycopg2.connect(database="Exercicio_Avaliativo_AV", user="postgres", password="123456", port="5432")
            comando = conn.cursor()
            try:
                comando_sql = 'DELETE FROM teste.tb_users WHERE "id" = %s'
                valores = (id,)
                comando.execute(comando_sql, valores)
                conn.commit()
            except  ConnectionError:
                print('Erro ao excluir dados. Verifique se o mesmo existe')
            finally:
                conn.close()
        else:
            print("ID inválido. Não foi possível excluir o registro.")


banco = BancoDeDados()
banco.lerDados()