import ExtracaoBancoOracle as ex

ext = ex.ExtracaoBancoOracle(caminhoSQL_TXT='C:\\Users\\id_teste\\Downloads', 
                             nomeTXT_SQL='teste.sql', 
                             caminhoSalvarArquivo='C:\\Users\\id_teste\\Downloads', 
                             nomeArquivo='testeExtracao.csv')
ext.extrairSalvarArquivo()