# Optimizacion-de-carteras-de-inversion-diversificadas
Este proyecto consiste en la elaboración de carteras eficientes a través de 12 de los índices bursátiles más relevantes a nivel global. Uno de los principales propósitos ha sido elaborar carteras diversificadas con el fin de eliminar el mayor riesgo posible, tanto el específico como el riesgo país. 

La metodología seguida en este proyecto ha sido la siguiente:

    -   Extraccion de historico de cotizaciones diarias de los últimos diez años de los 12 índices con los que se ha trabajado(IBEX 35, S&P 500, Dow Jones, NASDAQ COMPOSITE, NASDAQ 100, FTSE, CAC, EUROSTOXX 50, GDA, NIKKEI 225, NIFTY 50, HANGSENG).
    -   Limpieza de datos. Me he quedado con las fechas y cotización ajustada de cierre.
    -   He pintado graficos de lineas temporales de los índices por separado y conjuntamente a traves de matplotlib para ver su evolución.
    -   Calculo de rendimiento y riesgo.
    -   Correlaciones y covarianzas.
    -   Creación de carteras aleatorias.
    -   Cálculo de la frontera eficiente.



## Estructura del Proyecto

- **scripts**: Aquí se encuentra el script en Python(PROYECTO_FINAL) utilizado para extraer, limpiar y transformar los datos. Adjunta también la función para calcular la frontera eficiente.
- **output**: Los datos transformados en formato excell.
- **visualizations**: Archivo PowerBi donde se ha realizado la visualización.
- **presentation**: Archivo Power point de la presentación del proyecto.
- **grafs**: Visualizaciones y graficos en formato png.


## Requisitos

- Visual Studio Code
- Python (versión 3.9.13)
- Biblioteca Pandas (versión 1.4.4)
- Biblioteca Numpy
- Más bilbiotecas: yfinance, matplotlib, seaborn
- Módulos: random
- Power BI (versión 36257.0)

![Captura](https://github.com/Lorensou/Optimizacion-de-carteras-de-inversion-diversificadas/grafs/Carteras_aleatorias.png)
![Captura](https://github.com/Lorensou/Optimizacion-de-carteras-de-inversion-diversificadas/grafs/Frontera_eficiente.png)
