# Determinación de la carga específica del electrón $e/m$

> **Resumen:** Determinación experimental de la relación carga-masa del electrón ($e/m$) mediante una adaptación del experimento de Bainbridge. Se procesaron 4 series de mediciones utilizando un equipo experimental PASCO (tubo de helio a baja presión y bobinas de Helmholtz), evaluando regímenes a voltaje constante y corriente constante mediante ajustes por regresión lineal en Python.

---

## **Fundamento teórico**

El experimento se basa en la aceleración de electrones emitidos por efecto termoiónico mediante un potencial $V$, los cuales ingresan a una región con campo magnético uniforme $B$ generado por dos bobinas de Helmholtz.

1. **Campo magnético de Helmholtz:**
   $$B = \frac{\mu_0 N I}{\left(\frac{5}{4}\right)^{3/2} a}$$

   Donde $N = 130$ vueltas, $a = 0,15(1) \text{ m}$ es el radio de las bobinas e $I$ es la corriente aplicada.

2. **Conservación de la energía y fuerza de Lorentz:**
   $$\frac{1}{2} m v^2 = e V \quad \land \quad e v B = m \frac{v^2}{R}$$

3. **Relación fundamental:**
   Al combinar ambas ecuaciones se obtiene la relación:
   $$\frac{e}{m} = \frac{2V}{B^2 R^2}$$

---

## **Montaje experimental**

* **Equipo experimental:** PASCO con tubo $e/m$ esférico lleno de Helio a $10^{-2} \text{ mmHg}$.
* **Medición de variables:**
  * **Voltaje $V$:** Voltímetro digital (resolución $0,01 \text{ V}$).
  * **Corriente $I$:** Amperímetro (resolución $0,1 \text{ A}$).
  * **Radio de curvatura $R$:** Determinación visual del haz incandescente sobre regla integrada (resolución $1 \text{ mm}$).

---

## **Metodología y Regresiones Lineales**

Se realizaron 4 series experimentales linealizadas para ajustar por mínimos cuadrados. En cada una de ellas, la pendiente arrojada representó directamente la relación $e/m$:

| Serie | Régimen | Condición | Ajuste lineal | $e/m$ experimental $\left[\text{C/kg}\right]$ |
| :---: | :---: | :---: | :---: | :---: |
| **1** | Potencial constante | $V = 123{,}79(9) \text{ V}$ | $\frac{2V}{R^2}$ vs $B^2$ | $1{,}8(4) \times 10^{11}$ |
| **2** | Potencial constante | $V = 195{,}4(2) \text{ V}$ | $\frac{2V}{R^2}$ vs $B^2$ | $1{,}6(3) \times 10^{11}$ |
| **3** | Corriente constante | $I = 1{,}74(9) \text{ A}$ | $2V$ vs $B^2 R^2$ | $1{,}9(3) \times 10^{11}$ |
| **4** | Corriente constante | $I = 1{,}52(9) \text{ A}$ | $2V$ vs $B^2 R^2$ | $1{,}7(2) \times 10^{11}$ |

**Promedio ponderado global:** $\frac{e}{m} = (1{,}75 \pm 0{,}25) \times 10^{11} \text{ C/kg}$  
**Valor de referencia:** $\left(\frac{e}{m}\right)_{\text{ref}} = 1{,}7588(1) \times 10^{11} \text{ C/kg}$


---

## **Resultados Finales**

* **Promedio ponderado experimental:** $$\frac{e}{m} = (1,75 \pm 0,25) \cdot 10^{11} \text{ C/kg}$$

* **Valor teóricamente aceptado de referencia:** $$\left(\frac{e}{m}\right)_{\text{ref}} = 1,7588(1) \cdot 10^{11} \text{ C/kg}$$

El valor obtenido mediante el promedio ponderado de las cuatro determinaciones resulta compatible dentro de la incertidumbre experimental con el valor tabulado.

---

## **Estructura del Repositorio**

```text
├── Voltajes y corrientes.xlsx  # Mediciones directas (V, I, R)
├── corriente-fija.py           # Script de Python para procesamiento de datos
├── Informe.pdf                 # Informe completo del experimento
├── montaje.jpg                 # Fotografía del setup experimental PASCO
├── Corriente fija.png          # Gráficos de ajuste para I constante
├── Potencial fijo.png          # Gráficos de ajuste para V constante
└── README.md                   # Documentación principal