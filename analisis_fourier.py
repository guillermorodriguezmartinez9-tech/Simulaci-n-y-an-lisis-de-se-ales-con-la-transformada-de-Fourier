"""
Actividad Formativa 2: Simulación y Análisis de Señales con la Transformada de Fourier
Lenguaje: Python 3
Librerías: NumPy, Matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# CONFIGURACIÓN GENERAL DE MUESTREO
# =============================================================================
Fs = 1000.0             # Frecuencia de muestreo (Hz)
Ts = 1.0 / Fs           # Periodo de muestreo (s)
t = np.arange(-1.0, 1.0, Ts)
N = len(t)
freqs = np.fft.fftshift(np.fft.fftfreq(N, Ts))


def calcular_fft(x):
    """Calcula magnitud y fase de la FFT normalizada."""
    X = np.fft.fftshift(np.fft.fft(x))
    mag = np.abs(X) / N
    phase = np.angle(X)
    umbral = 1e-4 * np.max(mag)
    phase[mag < umbral] = 0.0
    return mag, phase


# =============================================================================
# 1. SEÑALES ELEMENTALES
# =============================================================================

# Senoidal (10 Hz)
f0 = 10.0
x_sin = np.sin(2 * np.pi * f0 * t)
mag_sin, phase_sin = calcular_fft(x_sin)

# Pulso Rectangular (tau = 0.2 s)
tau = 0.2
x_rect = np.where(np.abs(t) <= (tau / 2), 1.0, 0.0)
mag_rect, phase_rect = calcular_fft(x_rect)

# Escalón Unitario
x_step = np.where(t >= 0, 1.0, 0.0)
mag_step, phase_step = calcular_fft(x_step)

fig1, axes = plt.subplots(3, 3, figsize=(10, 7))
plt.subplots_adjust(hspace=0.45, wspace=0.35)

# Fila 1: Senoidal
axes[0, 0].plot(t, x_sin, 'b')
axes[0, 0].set_title('Senoidal (10 Hz)')
axes[0, 0].grid(True)

axes[0, 1].plot(freqs, mag_sin, 'r')
axes[0, 1].set_title('Magnitud')
axes[0, 1].set_xlim([-30, 30])
axes[0, 1].grid(True)

axes[0, 2].plot(freqs, phase_sin, 'g')
axes[0, 2].set_title('Fase')
axes[0, 2].set_xlim([-30, 30])
axes[0, 2].grid(True)

# Fila 2: Pulso Rectangular
axes[1, 0].plot(t, x_rect, 'b')
axes[1, 0].set_title('Pulso Rectangular (0.2s)')
axes[1, 0].grid(True)

axes[1, 1].plot(freqs, mag_rect, 'r')
axes[1, 1].set_title('Magnitud (Sinc)')
axes[1, 1].set_xlim([-30, 30])
axes[1, 1].grid(True)

axes[1, 2].plot(freqs, phase_rect, 'g')
axes[1, 2].set_title('Fase')
axes[1, 2].set_xlim([-30, 30])
axes[1, 2].grid(True)

# Fila 3: Escalón Unitario
axes[2, 0].plot(t, x_step, 'b')
axes[2, 0].set_title('Escalón u(t)')
axes[2, 0].grid(True)

axes[2, 1].plot(freqs, mag_step, 'r')
axes[2, 1].set_title('Magnitud')
axes[2, 1].set_xlim([-30, 30])
axes[2, 1].grid(True)

axes[2, 2].plot(freqs, phase_step, 'g')
axes[2, 2].set_title('Fase')
axes[2, 2].set_xlim([-30, 30])
axes[2, 2].grid(True)

plt.suptitle('Señales Elementales y su Transformada de Fourier', fontsize=12, fontweight='bold')
plt.show()

# =============================================================================
# 2. PROPIEDADES DE FOURIER
# =============================================================================

# Propiedad 1: Linealidad
x1 = np.sin(2 * np.pi * 5 * t)
x2 = np.sin(2 * np.pi * 15 * t)
a = 2.0
b = 3.0
X_comb = np.fft.fftshift(np.fft.fft(a * x1 + b * x2))
X_teor = a * np.fft.fftshift(np.fft.fft(x1)) + b * np.fft.fftshift(np.fft.fft(x2))
error_linealidad = float(np.max(np.abs(X_comb - X_teor)))
print(f"[Linealidad] Error máximo: {error_linealidad:.2e}")

# Propiedad 2: Desplazamiento en el Tiempo
t0 = 0.05
x_desp = np.sin(2 * np.pi * f0 * (t - t0))
mag_desp, phase_desp = calcular_fft(x_desp)

fig2, ax = plt.subplots(1, 2, figsize=(9, 4))
ax[0].plot(freqs, mag_sin, 'r', label='Original')
ax[0].plot(freqs, mag_desp, 'k--', label='Desplazada')
ax[0].set_title('Magnitud (Invariante)')
ax[0].set_xlim([-25, 25])
ax[0].legend()
ax[0].grid(True)

ax[1].plot(freqs, phase_sin, 'g', label='Fase Original')
ax[1].plot(freqs, phase_desp, 'm--', label='Fase Desplazada')
ax[1].set_title('Fase (Pendiente)')
ax[1].set_xlim([-25, 25])
ax[1].legend()
ax[1].grid(True)

plt.suptitle('Propiedad: Desplazamiento en el Tiempo', fontsize=12, fontweight='bold')
plt.show()

# Propiedad 3: Escalamiento
x_angosto = np.where(np.abs(t) <= 0.05, 1.0, 0.0)
mag_angosto, _ = calcular_fft(x_angosto)

fig3 = plt.figure(figsize=(8, 4))
plt.plot(freqs, mag_rect, 'b', label='Pulso Ancho (0.2s)')
plt.plot(freqs, mag_angosto, 'r', label='Pulso Estrecho (0.1s)')
plt.title('Propiedad: Escalamiento (Compresión = Expansión espectral)')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.xlim([-40, 40])
plt.legend()
plt.grid(True)
plt.show()
