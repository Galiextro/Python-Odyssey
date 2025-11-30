import streamlit as st
import numpy as np
import joblib

st.title("Predicción de Productividad")

model_reg = joblib.load("modelo_regresion.pkl")
model_clf = joblib.load("modelo_clasificacion.pkl")

st.subheader("Introduce tus datos:")

horas_sueño = st.number_input("Horas de sueño", 0, 12, 7)
tiempo_estudio = st.number_input("Tiempo de estudio (min)", 0, 600, 120)
distraccion = st.slider("Distracción (0–10)", 0, 10, 3)
energia = st.slider("Energía (1–5)", 1, 5, 4)
dificultad = st.slider("Dificultad (1–5)", 1, 5, 3)
uso_movil = st.slider("Uso del móvil (min)", 0, 300, 10)
ruido = st.slider("Ruido ambiente (0–10)", 0, 10, 2)
descanso = st.radio("¿Descansaste previamente?", ["sí", "no"])
estado = st.slider("Estado de ánimo (1–5)", 1, 5, 4)

if st.button("Predecir"):
    x = np.array([[
        horas_sueño, tiempo_estudio, distraccion, energia,
        dificultad, uso_movil, ruido,
        1 if descanso == "sí" else 0,
        estado
    ]])

    pred_reg = model_reg.predict(x)[0]
    pred_clf = model_clf.predict(x)[0]

    st.success(f"Predicción numérica: {pred_reg:.2f}")
    st.info(f"Categoría estimada: {pred_clf.upper()}")
