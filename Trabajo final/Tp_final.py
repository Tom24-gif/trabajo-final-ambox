import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leer el csv
datos = pd.read_csv('encuesta_bienestar.csv')
df = pd.DataFrame(datos)

# ver los datos nulos y duplicados
print(df.isnull().sum())
print('--------------------------------------')#barras para separar
print(df.duplicated().sum())
print('--------------------------------------')

# no existen datos duplicados

# hacemos un analisis univariado
 
print(df.info())

# Analisamos las siguientes columnas: edad, sueño, ejercicio y felicidad
# edad:
print('Edad')
print(df['age'].describe().round(2))
print('---------------------------------------')
# sueño:
print('Horas de sueño')
print(df['hours_sleep'].describe().round(2))
print('---------------------------------------')
# ejercicio:
print('Dias de ejercicio')
print(df['exercise_days'].describe().round(2))
print('---------------------------------------')
# felicidad:
print('Nivel de felicidad')
print(df['happiness_level'].describe().round(2))
print('---------------------------------------')

# hacemos un analisis bivariado
# relacion entre edad y sueño:
print('Relacion entre edad y sueño')
relacion_edad_sueño = df.groupby('age')['hours_sleep'].describe().round(2)
print(relacion_edad_sueño)
print('podemos ver que los que tienen mayor edad tienden a dormir un poco mas, siendo el que mas deurme en promedio, los que tienens 63años')
print('---------------------------------------')

# relacion entre edad y felicidad:
print('Relacion entre edad y felicidad')
relacion_edad_felicidad = df.groupby('age')['happiness_level'].describe().round(2)
print(relacion_edad_felicidad)
print('podemos ver que los mas felices en promedio son los de 30 años')
print('---------------------------------------')

# relacion entre edad y ejercicio
print('Relacion entre edad y ejercicio')
relacion_edad_ejercicio = df.groupby('exercise_days')['age'].describe().round(2)
print(relacion_edad_ejercicio)
print('podemos ver que los que hacen mas dias de ejercicio son los que tienen 40 años')
print('---------------------------------------')

# relacion entre felicidad y sueño:
print('Relacion entre felicidad y sueño')
relacion_felicidad_sueño = df.groupby('happiness_level')['hours_sleep'].describe().round(2)
print(relacion_felicidad_sueño)
print('podemos ver que los que hacen meos dias de ejercicio son mas felices')
print('---------------------------------------')

# relacion entre felicidad y ejercicio:
print('Relacion entre felicidad y ejercicio')
relacion_felicidad_ejercicio = df.groupby('exercise_days')['happiness_level'].describe().round(2)
print(relacion_felicidad_ejercicio)
print('podemos ver que los que hacen meos dias de ejercicio son mas felices')
print('---------------------------------------')

# relacion entre sueño y ejercicio:
print('Relacion entre felicidad y ejercicio')
relacion_felicidad_ejercicio = df.groupby('exercise_days')['hours_sleep'].describe().round(2)
print(relacion_felicidad_ejercicio)
print('podemos ver que los que hacen meos dias de ejercicio son mas felices')
print('---------------------------------------')

# Comparamos cuantos hay de cada genero encada pais
genero_pais = df.groupby('country')['gender'].value_counts()
print('Comparacion entre generos')
print(genero_pais)
print('---------------------------------------')

# Creamos indicadores
df["screen_sleep_ratio"] = df["screen_time"] / df["hours_sleep"]
print('Habitos de uso de pantallas a la hora de dormir')
print(df["screen_sleep_ratio"])
print("""
un valor > 1 = mas tiempo frente a pantallas que durmiendo (potencial riesgo)
un valor = 1 -> tiempo balanceado
un valor < 1 = duerme mas tiempo del que pasa en pantallas (ideal)
""")
print('---------------------------------------')

df['screen_stress_ratio'] = df['screen_time'] / df['stress_level']
print('Estres provocado por las pantallas')
print(df['screen_stress_ratio'])
print("""
un valor > 1 = menor tiempo frente a pantallas, mas saludable (ideal)
un valor = 1 -> tiempo balanceado
un valor < 1 = mas tiempo que pasa en pantallas, mayor estres (potencial riesgo)
""")

# Visualizamos relaciones entre variables

# relacion entre edad y estres
sns.scatterplot(x='age', y='stress_level', hue='gender', data=df)
plt.title('Relacion entre edad y estres')
plt.xlabel('edad')
plt.ylabel('estres')
plt.savefig('relacion_edad_estres.png')
plt.show()

# mapa de correlaciones entre variables
df_numerico = df[['age', 'hours_sleep', 'exercise_days', 'happiness_level', 'stress_level']]
corr = df_numerico.corr()
plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Mapa de correlaciones')
plt.savefig('mapa_de_calor.png')
plt.show()

# grafico de barras de nivel de feliciadad
sns.barplot(x='gender', y='happiness_level', data=df)
plt.title('Nivel de felicidad por genero')
plt.xlabel('genero')
plt.ylabel('nivel de felicidad')
plt.savefig('niveles_felicidad.png')
plt.show()

# grafico de barras de nivel de estres
sns.barplot(x='gender', y='stress_level', data=df)
plt.title('Nivel de estres por genero')
plt.xlabel('genero')
plt.ylabel('nivel de felicidad')
plt.savefig('niveles_estres.png')
plt.show()