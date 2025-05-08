import streamlit as st  
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

wage = pd.read_csv("wage.csv")
st.title("Gráficos de salario")



tab1, tab2 = st.tabs(["Análisis univariado", "Análisis bivariado"])

with tab1:
    st.header("Análisis univariado")
    fig, ax =plt.subplots(1, 4, figsize = (15,5))

    ax[0].set_title("Ganancias por hora promedio", fontsize = 20)
    ax[1].set_title("Años de educación", fontsize = 20)
    ax[2].set_title("Años de experiencia", fontsize = 20)
    ax[3].set_title("Género", fontsize = 20)

    ax[0].hist(wage["Ganancias por hora promedio"])
    ax[1].hist(wage["Años de educación"])
    ax[2].hist(wage["Años de experiencia"])
    conteo = wage["Género"].value_counts()
    ax[3].bar(conteo.index, conteo.values)
    fig.tight_layout()
    st.pyplot(fig)

with tab2:
    fig, ax =plt.subplots(1, 3, figsize = (15,5))


    sns.scatterplot(data=wage, x="Años de educación", y="Ganancias por hora promedio", ax=ax[0])
    sns.scatterplot(data=wage, x="Años de experiencia", y="Ganancias por hora promedio", ax=ax[1])
    sns.violinplot(data=wage, x="Género", y="Ganancias por hora promedio", ax=ax[2])

    st.pyplot(fig)

