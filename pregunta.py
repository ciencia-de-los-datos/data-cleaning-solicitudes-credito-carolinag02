"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.drop(['Unnamed: 0'], axis=1, inplace = True)
    df.dropna(inplace = True)
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].apply(lambda x: str(x).replace("-"," ").replace("_"," "))
    df["barrio"] = df["barrio"].str.lower()
    df["barrio"] = df["barrio"].apply(lambda x: str(x).replace("_"," ").replace("-"," "))
    df["estrato"] = df["estrato"].replace('01', 1).astype(int)
    df["comuna_ciudadano"] = df["comuna_ciudadano"].fillna(0).astype(int)
    df["fecha_de_beneficio"] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True, format='mixed')
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x: str(x).strip("$").strip().replace(".00","").replace(",",""))
    df["línea_credito"] = df["línea_credito"].str.lower()
    df["línea_credito"] = df["línea_credito"].apply(lambda x: str(x).replace("-"," ").replace("_"," "))
    
    df.drop_duplicates(inplace = True)
    
    return df
