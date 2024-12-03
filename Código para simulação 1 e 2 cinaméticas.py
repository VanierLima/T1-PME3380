import numpy as np
import matplotlib.pyplot as plt

# Definindo os parâmetros com x = 0 e y = 0
x = 0  # valor específico para x
y = 0  # valor específico para y
z = 1  # z agora é constante igual a 1
phi = 0  # valor inicial de phi
psi = 0  # valor inicial de psi

# Parâmetros de variação de theta
amplitude_theta = np.radians(30)  # 30 graus em radianos
frequencia_theta = 3  # frequência de 3 rad/s

# Definindo o tempo com mais espaçamento entre os pontos
tempo = np.linspace(0, 2, 50)  # 2 segundos com 50 pontos

# Função senoidal para theta variando entre +30° e -30°
theta = amplitude_theta * np.sin(frequencia_theta * tempo)

# Cálculo dos comprimentos (módulos dos vetores S1 a S6) conforme a imagem
S1 = np.sqrt(
    (np.abs(-0.433013 + 0.216506 * np.cos(theta) * np.cos(psi) - 0.125 * (np.cos(psi) * np.sin(phi)* np.sin(theta) - np.cos(phi) * np.sin(psi)) + x))**2 +
    (np.abs(0.25 - 0.216506 * np.cos(theta) * np.sin(psi) - 0.125 * (-np.cos(phi) * np.cos(psi) + np.sin(phi) * np.sin(psi)* np.sin(theta)) + y))**2 +
    (np.abs(0.216506 * np.sin(theta) - 0.125 * np.cos(theta) * np.sin(phi) + z))**2
)

S2 = np.sqrt(
    (np.abs(-0.433013 + 0.25 * (np.cos(psi) * np.sin(theta) * np.sin(phi) - np.cos(phi) * np.sin(psi)) + x))**2 +
    (np.abs(0.25 + 0.25 * (-np.cos(phi) * np.cos(psi) + np.sin(phi) * np.sin(psi)) + y))**2 +
    (np.abs(0.25* np.cos(theta) * np.sin(phi) + z))**2
)

S3 = np.sqrt(
    (np.abs(0.433013 + 0.25 * (np.cos(psi) * np.sin(theta) * np.sin(phi) - np.cos(phi) * np.sin(psi)) + x))**2 +
    (np.abs(0.25 + 0.25 * (-np.cos(phi) * np.cos(psi) + np.sin(phi) * np.sin(psi)) + y))**2 +
    (np.abs(0.25* np.cos(theta) * np.sin(phi) + z))**2
)

S4 = np.sqrt(
    (np.abs(0.433013 - 0.216506 * np.cos(theta) * np.cos(psi) - 0.125 * (np.cos(psi) * np.sin(theta) * np.sin(phi) - np.cos(phi) * np.sin(psi)) + x))**2 +
    (np.abs(0.25 + 0.216506 * np.cos(theta) * np.sin(psi) - 0.125 * (-np.cos(phi) * np.cos(psi) + np.sin(phi) * np.sin(psi) * np.sin(theta)) + y))**2 +
    (np.abs(-0.216506 * np.sin(theta) - 0.125 * np.cos(theta) * np.sin(phi) + z))**2
)

S5 = np.sqrt(
    (np.abs(0.216506 * np.cos(theta) * np.cos(psi) - 0.125 * (np.cos(psi) * np.sin(phi)* np.sin(theta) - np.cos(phi) * np.sin(psi)) + x))**2 +
    (np.abs(-0.5 - 0.216506 * np.cos(theta) * np.sin(psi) - 0.125 * (-np.cos(phi) * np.cos(psi) + np.sin(phi)* np.sin(theta)*np.sin(psi)) + y))**2 +
    (np.abs(-0.216506 * np.sin(theta) - 0.125 * np.cos(theta) * np.sin(phi) + z))**2
)

S6 = np.sqrt(
    (-np.abs(0.216506 * np.cos(theta) * np.cos(psi) - 0.125 * (np.cos(psi) * np.sin(phi)* np.sin(theta) - np.cos(phi) * np.sin(psi)) + x))**2 +
    (np.abs(-0.5 - 0.216506 * np.cos(theta) * np.sin(psi) - 0.125 * (-np.cos(phi) * np.cos(psi) + np.sin(phi)* np.sin(theta)*np.sin(psi)) + y))**2 +
    (np.abs(0.216506 * np.sin(theta) - 0.125 * np.cos(theta) * np.sin(phi) + z))**2
)

# Plot de z pelo tempo (agora constante)
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(tempo, z * np.ones_like(tempo), linestyle='-', marker='o', markersize=8, label='z(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('z (m)')
plt.title(f'Posição de z pelo tempo (x={x}, y={y}) com z constante')
plt.grid(True)
plt.legend()

# Plot de phi, theta e psi pelo tempo
plt.subplot(3, 1, 2)
plt.plot(tempo, phi * np.ones_like(tempo), linestyle='-', marker='s', markersize=8, label='phi(t)')
plt.plot(tempo, theta, linestyle='-', marker='^', markersize=8, label='theta(t)')
plt.plot(tempo, psi * np.ones_like(tempo), linestyle='-', marker='x', markersize=8, label='psi(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulos (rad)')
plt.title('Ângulos phi, theta, psi pelo tempo')
plt.grid(True)
plt.legend()

# Plot dos comprimentos S1 a S6 pelo tempo
plt.subplot(3, 1, 3)
plt.plot(tempo, S1, linestyle='-', marker='o', markersize=8, label='S1(t)')
plt.plot(tempo, S2, linestyle='-', marker='s', markersize=8, label='S2(t)')
plt.plot(tempo, S3, linestyle='-', marker='^', markersize=8, label='S3(t)')
plt.plot(tempo, S4, linestyle='-', marker='x', markersize=8, label='S4(t)')
plt.plot(tempo, S5, linestyle='-', marker='d', markersize=8, label='S5(t)')
plt.plot(tempo, S6, linestyle='-', marker='*', markersize=8, label='S6(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('Comprimento (m)')
plt.title('Comprimentos dos vetores S1 a S6 pelo tempo')
plt.grid(True)
plt.legend()

# Ajustando o layout
plt.tight_layout()
plt.show()
