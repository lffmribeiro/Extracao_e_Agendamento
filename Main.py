import ExtracaoBancoOracle as ex

#Agendamento
import schedule
import time

#Instanciando a classe que fará a extracao
ext = ex.ExtracaoBancoOracle(caminhoSQL_TXT='C:\\Users\\id_teste\\Downloads', 
                             nomeTXT_SQL='teste.sql', 
                             caminhoSalvarArquivo='C:\\Users\\id_teste\\Downloads', 
                             nomeArquivo='testeExtracao.csv')

#Agendamento
schedule.every.day.at('00:00').do(ext.extrairSalvarArquivo())

while True:
    schedule.run_pending()
    time.sleep(1)