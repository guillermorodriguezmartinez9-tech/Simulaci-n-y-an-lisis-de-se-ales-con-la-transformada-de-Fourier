# Actividad Formativa 2: Simulación y Análisis de Señales con la Transformada de Fourier

## Descripción del Proyecto
Este proyecto implementa la simulación y análisis en el dominio del tiempo y de la frecuencia de señales continuas discretizadas mediante la Transformada Rápida de Fourier (FFT) en Python. Se evalúan señales periódicas, aperiódicas y discontinuas, comprobando cuantitativa y cualitativamente las propiedades fundamentales de la Transformada de Fourier.

## Contenido del Repositorio
* `analisis_fourier.py`: Script principal que genera las señales elementales, calcula la FFT normalizada con centrado (`fftshift`) y evalúa las propiedades de Fourier.
* `README.md`: Documentación explicativa del proyecto.

## Señales Analizadas
1. **Función Senoidal (10 Hz):** Representa una señal armónica pura cuyo espectro de magnitud consta de dos impulsos simétricos en ±10 Hz.
2. **Pulso Rectangular (ancho = 0.2 s):** Señal aperiódica cuya transformación en frecuencia corresponde a una función sinc(f).
3. **Escalón Unitario u(t):** Señal con discontinuidad que presenta concentración de energía en bajas frecuencias y componente de nivel continuo (DC en 0 Hz).

## Propiedades de Fourier Comprobadas
* **Linealidad:** La FFT de una combinación lineal de señales equivale a la combinación lineal de sus espectros individuales con un error numérico despreciable (~ 0).
* **Desplazamiento Temporal:** Un retardo en el tiempo conserva invariante el espectro de magnitud y añade una fase lineal decreciente.
* **Escalamiento Temporal:** La compresión en el tiempo (pulso más angosto) genera una expansión proporcional en el espectro de frecuencias.

## Requisitos y Ejecución
Requiere Python 3 con las librerías `numpy` y `matplotlib`:
```bash
pip install numpy matplotlib
python analisis_fourier.py
