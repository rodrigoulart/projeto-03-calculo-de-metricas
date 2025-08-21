import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc
from sklearn.preprocessing import label_binarize

# Carregando o dataset de dígitos (0-9)
digits = load_digits()
X = digits.data      # Features (64 pixels por imagem 8x8)
y = digits.target    # Labels (0-9)

# Dividindo em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Treinando um classificador
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Fazendo previsões
y_pred = clf.predict(X_test)

# Calculando a matriz de confusão
matriz_confusao = confusion_matrix(y_test, y_pred)

# Plotando a matriz de confusão
plt.figure(figsize=(8,6))
sns.heatmap(matriz_confusao, annot=True, fmt="d", cmap="Blues")
plt.title("Matriz de Confusão - Dígitos 0-9")
plt.ylabel("Classe Real")
plt.xlabel("Classe Predita")
plt.show()

# Calculando métricas gerais
acuracia = accuracy_score(y_test, y_pred)
precisao = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("===== Métricas de Avaliação =====")
print(f"Acurácia: {acuracia:.2f}")
print(f"Precisão (média ponderada): {precisao:.2f}")
print(f"Sensibilidade / Recall (média ponderada): {recall:.2f}")
print(f"F1-Score (média ponderada): {f1:.2f}")

# Preparando para curva ROC multiclasses
# Binarizando os labels
y_test_bin = label_binarize(y_test, classes=np.arange(10))
y_score = clf.predict_proba(X_test)

# Plotando curva ROC para cada classe
plt.figure(figsize=(10,8))
for i in range(10):
    fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_score[:, i])
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, lw=2, label=f'Classe {i} (AUC = {roc_auc:.2f})')

plt.plot([0, 1], [0, 1], color='red', lw=2, linestyle='--', label='Aleatório')
plt.xlabel('Taxa de Falsos Positivos (FPR)')
plt.ylabel('Taxa de Verdadeiros Positivos (TPR / Recall)')
plt.title('Curva ROC Multiclasse - Dígitos 0-9')
plt.legend(loc="lower right")
plt.grid(True)
plt.show()
