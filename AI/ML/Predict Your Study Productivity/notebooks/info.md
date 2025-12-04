## 1. Fundamentos: Tipos de Aprendizaje

Antes de elegir un algoritmo, es crucial identificar el tipo de problema.

| Tipo | Descripción | Palabra Clave | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Supervisado** | El modelo aprende de datos etiquetados (tenemos la respuesta correcta `y` para cada entrada `x`). | **Predicción** | Predecir precio de casa (Regresión) o si es spam (Clasificación). |
| **No Supervisado** | El modelo trabaja con datos sin etiquetar. Busca estructuras o patrones ocultos. | **Patrones** | Agrupar clientes (Clustering). |
| **Semi-supervisado** | Combina pocos datos etiquetados con muchos sin etiquetar. | **Eficiencia** | Clasificación de imágenes médicas. |
| **Por Refuerzo** | Un agente aprende tomando decisiones y recibiendo recompensas/castigos. | **Acción** | Robot aprendiendo a caminar. |

---

## 2. Preprocesamiento y Conceptos Clave

### Recomendaciones de Preprocesamiento
* **Limpieza:** Imputar valores nulos (media/mediana/KNN), eliminar duplicados.
* **Encoding:**
    * *One-Hot:* Para categorías nominales (sin orden).
    * *Label Encoding:* Para categorías ordinales (con orden, ej: Bajo, Medio).
* **Escalado (Scaling):** Crucial para algoritmos de distancia (KNN, SVM, K-Means).
    * *StandardScaler:* Media 0, Desviación 1.
    * *MinMaxScaler:* Escala entre 0 y 1.

### Overfitting vs. Underfitting
* **Underfitting (Sesgo alto):** Modelo muy simple, no captura la tendencia.
* **Overfitting (Varianza alta):** Modelo "memoriza" el ruido, falla con datos nuevos.
* **Regularización:** Penaliza la complejidad para evitar overfitting.
    * **L1 (Lasso):** Selección de features (lleva coeficientes a 0).
    * **L2 (Ridge):** Reduce magnitud de coeficientes.

---

## 3. Catálogo de Algoritmos

### A. Aprendizaje Supervisado (Regresión)

#### 1. Regresión Lineal (Linear Regression)
* **Tipo:** Supervisado (Regresión).
* **Descripción:** Ajusta una línea recta (o hiperplano) que minimiza el error cuadrático entre la variable dependiente e independientes.
* **Casos de uso:**
    1. Predicción de ventas según inversión.
    2. Estimación de precios inmobiliarios.
* **Ventajas:** Simple, interpretable, rápido.
* **Desventajas:** Asume linealidad estricta, sensible a outliers.
* **Requerimientos:** Relación lineal, sin multicolinealidad, normalidad en residuos.
* **Librerías:** `sklearn.linear_model.LinearRegression`

---

### B. Aprendizaje Supervisado (Clasificación)

#### 2. Regresión Logística (Logistic Regression)
* **Tipo:** Supervisado (Clasificación).
* **Descripción:** Estima la probabilidad de pertenencia a una clase usando la función sigmoide.
* **Casos de uso:**
    1. Scoring crediticio (Riesgo: Sí/No).
    2. Tasa de conversión (Click vs No Click).
* **Ventajas:** Salida probabilística, eficiente.
* **Desventajas:** Asume relación lineal con el logit, sufre con relaciones no lineales complejas.
* **Requerimientos:** Target binario (generalmente), muestra grande.
* **Librerías:** `sklearn.linear_model.LogisticRegression`

#### 3. K-Vecinos Más Cercanos (KNN)
* **Tipo:** Supervisado (Clasificación/Regresión).
* **Descripción:** Algoritmo "perezoso". Asigna la clase mayoritaria de los 'K' puntos más cercanos.
* **Casos de uso:**
    1. Sistemas de recomendación simples.
    2. Reconocimiento de patrones básicos.
* **Ventajas:** Simple, sin asunciones de distribución.
* **Desventajas:** Lento en predicción, sensible a outliers y escala.
* **Requerimientos:** **Escalado obligatorio**.
* **Librerías:** `sklearn.neighbors.KNeighborsClassifier`

#### 4. Árboles de Decisión (Decision Trees)
* **Tipo:** Supervisado (Clasificación/Regresión).
* **Descripción:** Divide datos mediante reglas (sí/no) para maximizar la pureza de los nodos.
* **Casos de uso:**
    1. Diagnóstico médico.
    2. Aprobación de préstamos (reglas de negocio).
* **Ventajas:** Interpretable, no requiere escalado, maneja no-linealidad.
* **Desventajas:** Propenso a **Overfitting** (inestable).
* **Requerimientos:** Ninguno específico de preprocesamiento.
* **Librerías:** `sklearn.tree.DecisionTreeClassifier`

#### 5. Random Forest
* **Tipo:** Supervisado (Ensemble - Bagging).
* **Descripción:** Múltiples árboles de decisión entrenados con subconjuntos aleatorios. Promedia los resultados.
* **Casos de uso:**
    1. Detección de fraude.
    2. Predicción de Churn (abandono).
* **Ventajas:** Robusto, reduce overfitting, alta precisión.
* **Desventajas:** "Caja negra", más lento que un árbol simple.
* **Requerimientos:** Pocos.
* **Librerías:** `sklearn.ensemble.RandomForestClassifier`

#### 6. Support Vector Machines (SVM)
* **Tipo:** Supervisado (Clasificación/Regresión).
* **Descripción:** Busca el hiperplano que maximiza el margen entre clases. Usa kernels para datos no separables linealmente.
* **Casos de uso:**
    1. Clasificación de texto/sentimientos.
    2. Reconocimiento de escritura.
* **Ventajas:** Efectivo en alta dimensionalidad.
* **Desventajas:** Lento con muchos datos, difícil de tunear.
* **Requerimientos:** **Escalado obligatorio**.
* **Librerías:** `sklearn.svm.SVC`

---

### C. Aprendizaje No Supervisado

#### 7. K-Means Clustering
* **Tipo:** No Supervisado (Clustering).
* **Descripción:** Agrupa datos en 'K' clusters minimizando distancia a los centroides.
* **Casos de uso:**
    1. Segmentación de clientes.
    2. Compresión de imágenes.
* **Ventajas:** Rápido y escalable.
* **Desventajas:** Requiere definir 'K', sensible a inicialización.
* **Requerimientos:** Escalado recomendado.
* **Librerías:** `sklearn.cluster.KMeans`

#### 8. PCA (Principal Component Analysis)
* **Tipo:** No Supervisado (Reducción Dimensionalidad).
* **Descripción:** Transforma variables en Componentes Principales ortogonales para reducir dimensiones manteniendo varianza.
* **Casos de uso:**
    1. Visualización 2D/3D.
    2. Reducción de ruido.
* **Ventajas:** Elimina multicolinealidad, reduce complejidad.
* **Desventajas:** Pérdida de interpretabilidad semántica.
* **Requerimientos:** Variables numéricas y escaladas.
* **Librerías:** `sklearn.decomposition.PCA`

---

### D. Deep Learning

#### 9. Redes Neuronales (MLP)
* **Tipo:** Supervisado (generalmente).
* **Descripción:** Capas de neuronas conectadas que aprenden representaciones jerárquicas no lineales.
* **Casos de uso:**
    1. Problemas complejos (visión, NLP).
    2. Tablas masivas de datos.
* **Ventajas:** Potencia de aprendizaje muy alta.
* **Desventajas:** Requiere muchos datos y cómputo (GPU), caja negra.
* **Requerimientos:** Escalado, gran volumen de datos.
* **Librerías:** `TensorFlow`, `PyTorch`.

---

## 4. Métricas de Evaluación

### Regresión
* **MSE:** Penaliza errores grandes.
* **MAE:** Robusto a outliers.
* **R²:** Porcentaje de varianza explicada.

### Clasificación
* **Accuracy:** % total de aciertos (cuidado con desbalance).
* **Precision:** Calidad de los positivos (pocos falsos positivos).
* **Recall:** Cantidad de positivos detectados (pocos falsos negativos).
* **F1-Score:** Balance entre Precision y Recall.
* **ROC-AUC:** Capacidad de distinguir clases.

---

## 5. Recursos Adicionales

* **Libros:**
    * *Hands-On Machine Learning* (Aurélien Géron).
    * *Pattern Recognition and Machine Learning* (Bishop).
* **Datasets:** Kaggle, UCI Repository.
* **Doc:** Scikit-learn User Guide.

### Ejemplo Rápido (Python)

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# Carga y Split
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)

# Modelo
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Predicción
print(f"Accuracy: {accuracy_score(y_test, model.predict(X_test)):.2f}")