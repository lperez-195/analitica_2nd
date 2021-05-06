# %%
import numpy as np
import pandas as pd
import seaborn as sns
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
print(df)

def histograma(nombre):
    return sns.histplot(
    x=nombre,
    data = df
    )

def cajaBigotes(nombre):
    sns.boxplot(x=nombre,
    data=df
    )
def mapaCalor():
    df.corr()
    sns.heatmap(df.corr(), annot=True)

nombres = ["customer", "order","total_items","discount%","weekday","hour","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]
# %%
cajaBigotes(nombres[0])
# %%
cajaBigotes(nombres[1])
# %%
cajaBigotes(nombres[2])
# %%
cajaBigotes(nombres[3])
# %%
cajaBigotes(nombres[4])
# %%
cajaBigotes(nombres[5])
# %%
cajaBigotes(nombres[6])
# %%
cajaBigotes(nombres[7])
# %%
cajaBigotes(nombres[8])
# %%
cajaBigotes(nombres[9])
# %%
cajaBigotes(nombres[10])
# %%
cajaBigotes(nombres[11])
# %%
cajaBigotes(nombres[12])
# %%
cajaBigotes(nombres[13])


# %%
histograma(nombres[0])
# %%
histograma(nombres[1])
# %%
histograma(nombres[2])
# %%
histograma(nombres[3])
# %%
histograma(nombres[4])
# %%
histograma(nombres[5])
# %%
histograma(nombres[6])
# %%
histograma(nombres[7])
# %%
histograma(nombres[8])
# %%
histograma(nombres[9])
# %%
histograma(nombres[10])
# %%
histograma(nombres[11])
# %%
histograma(nombres[12])
# %%
histograma(nombres[13])
# %%
mapaCalor()
# %%
