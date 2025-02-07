import math
import streamlit as st
import matplotlib.pyplot as plt

def symulacja_rzutu(v0, angle, dt=0.01):
    g = 9.81  
    angle_rad = math.radians(angle)
    vx = v0 * math.cos(angle_rad)
    vy = v0 * math.sin(angle_rad)
    
    x, y = 0, 0
    x_values = [x]
    y_values = [y]
    
    while y >= 0:
        x += vx * dt
        vy -= g * dt
        y += vy * dt
        if y < 0:
            break
        x_values.append(x)
        y_values.append(y)
    
    return x_values, y_values


st.title("Symulacja rzutu ukośnego")

v0 = st.slider("Prędkość początkowa (m/s)", 0, 100, 20)
angle = st.slider("Kąt rzutu (°)", 0, 90, 45)

x_vals, y_vals = symulacja_rzutu(v0, angle)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label=f"v0={v0} m/s, kąt={angle}°")
ax.set_xlabel("Odległość (m)")
ax.set_ylabel("Wysokość (m)")
ax.set_title("Symulacja rzutu ukośnego")
ax.legend()
ax.grid()

ax.set_xlim(0, 250)
ax.set_ylim(0, 100)

st.pyplot(fig)

