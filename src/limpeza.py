import pandas as pd

df= pd.read_csv(r'C:\Users\Pedro\Documents\GitHub\analise-criminalidade-rj\data\raw\BaseDPEvolucaoMensalCisp.csv', 
                encoding= 'latin1', 
                sep= ';', 
                dtype='str')

df_limpo= df.melt(id_vars= ["mes", "ano", "munic", "regiao"],
        var_name= "tipo_crime",
        value_vars= ['hom_doloso', 'lesao_corp_morte', 'latrocinio', 'cvli',
                     'hom_por_interv_policial', 'feminicidio', 'letalidade_violenta',
                     'tentat_hom', 'tentativa_feminicidio', 'lesao_corp_dolosa', 'estupro',
                     'hom_culposo', 'lesao_corp_culposa','total_roubos', 'total_furtos', 'registro_ocorrencias'],
        value_name= "quantidade")

df_limpo['mes']= df_limpo['ano']  + '_' + '0' +  df_limpo['mes']

df_limpo.rename(columns= {'mes':'Mes_Ano'}, inplace= True)

df_limpo.drop(columns= 'ano', inplace= True)

df_limpo['quantidade']= df_limpo['quantidade'].fillna(0).astype('int')

df_limpo= df_limpo.groupby(by= ['Mes_Ano', 'munic', 'regiao', 'tipo_crime'], as_index= False).sum()

df_limpo.to_csv(r'C:\Users\Pedro\Documents\GitHub\analise-criminalidade-rj\data\processed\Base_limpo.csv', 
                sep=';', 
                encoding='utf-8', 
                index= False)
