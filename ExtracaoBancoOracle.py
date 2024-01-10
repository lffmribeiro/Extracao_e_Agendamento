import pandas as pd 
import oracledb
import dotenv 
import os

class ExtracaoBancoOracle:
    def __init__(self, caminhoSQL_TXT, nomeTXT_SQL, caminhoSalvarArquivo, nomeArquivo):
        #caminho do arquivo SQL/TXT
        self.pathSQL_TXT = caminhoSQL_TXT + "\\" + nomeTXT_SQL
        #caminho para salvar o df
        self.pathSalvar = caminhoSalvarArquivo + "\\" + nomeArquivo
        #arquivo que nos tras as variáveis para a conexão
        dotenv.load_dotenv(override=True)
        self.password = os.getenv('password')
        self.server = os.getenv('server')
        self.user = os.getenv('user')
        self.port = os.getenv('port')


    #função que faz a leitura do select que será extraido
    def lerArquivoSQL_TXT(self):
        with open(self.pathSQL_TXT, 'r') as arquivo:
            self.query = arquivo.read()
        return self.query
    
    def ajustarData(self):
        pass

    def gerarDataFrame(self):
        with oracledb.connect(user=self.user, password=self.password, dsn=self.server, port=self.port) as conexao:
            self.df = pd.read_sql(self.query, conexao)
        return self.df

    def limparExtracaoAnterior(self):
        if os.path.exists(self.pathSalvar):
            os.remove(self.pathSalvar)

    def salvarDataFrame(self):
        self.df.to_csv(self.pathSalvar, sep=';')

    def extrairSalvarArquivo(self):
        self.lerArquivoSQL_TXT()
        self.gerarDataFrame()
        #self.limparExtracaoAnterior()
        self.salvarDataFrame()
