import control
import matplotlib.pyplot as plt

# Coeficientes do numerador e denominador
numerator_coeffs = [
    1, 4, -4.73292, -28.19876, -81.392785623, -111.120971246,
    585.225199126945, 635.419224749945, -408.849948565479
]
denominator_coeffs = [1, 1, -9.24667]

# Criar a função de transferência
G_s = control.TransferFunction(numerator_coeffs, denominator_coeffs)

# Gerar os diagramas de Bode
control.bode(G_s, dB=True)
plt.show()
