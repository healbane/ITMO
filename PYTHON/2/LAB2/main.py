import os
from typing import Dict, Union, Any
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import seaborn as sns


# ============================================================
# 1. СОЗДАНИЕ И ОБРАБОТКА МАССИВОВ
# ============================================================

def create_vector() -> np.ndarray:
    """
    Создать массив от 0 до 9.

    Returns:
        np.ndarray: Массив чисел от 0 до 9 включительно.
    """
    return np.arange(10)


def create_matrix() -> np.ndarray:
    """
    Создать матрицу 5x5 со случайными числами [0,1].

    Returns:
        np.ndarray: Матрица 5x5 со случайными значениями от 0 до 1.
    """
    return np.random.rand(5, 5)


def reshape_vector(vec: np.ndarray) -> np.ndarray:
    """
    Преобразовать массив формы (10,) в форму (2, 5).

    Args:
        vec (np.ndarray): Входной массив формы (10,).

    Returns:
        np.ndarray: Преобразованный массив формы (2, 5).
    """
    return vec.reshape(2, 5)


def transpose_matrix(mat: np.ndarray) -> np.ndarray:
    """
    Транспонирование матрицы.

    Args:
        mat (np.ndarray): Входная матрица.

    Returns:
        np.ndarray: Транспонированная матрица.
    """
    return mat.T


# ============================================================
# 2. ВЕКТОРНЫЕ ОПЕРАЦИИ
# ============================================================

def vector_add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Сложение векторов одинаковой длины (векторизация без циклов).

    Args:
        a (np.ndarray): Первый вектор.
        b (np.ndarray): Второй вектор.

    Returns:
        np.ndarray: Результат поэлементного сложения.
    """
    return a + b


def scalar_multiply(vec: np.ndarray, scalar: Union[float, int]) -> np.ndarray:
    """
    Умножение вектора на число.

    Args:
        vec (np.ndarray): Входной вектор.
        scalar (float | int): Число для умножения.

    Returns:
        np.ndarray: Результат умножения вектора на скаляр.
    """
    return vec * scalar


def elementwise_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Поэлементное умножение массивов.

    Args:
        a (np.ndarray): Первый вектор/матрица.
        b (np.ndarray): Второй вектор/матрица.

    Returns:
        np.ndarray: Результат поэлементного умножения.
    """
    return a * b


def dot_product(a: np.ndarray, b: np.ndarray) -> Any:
    """
    Скалярное произведение векторов.

    Args:
        a (np.ndarray): Первый вектор.
        b (np.ndarray): Второй вектор.

    Returns:
        Any: Скалярное произведение векторов.
    """
    return np.dot(a, b)


# ============================================================
# 3. МАТРИЧНЫЕ ОПЕРАЦИИ
# ============================================================

def matrix_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Умножение матриц.

    Args:
        a (np.ndarray): Первая матрица.
        b (np.ndarray): Вторая матрица.

    Returns:
        np.ndarray: Результат матричного умножения.
    """
    return a @ b


def matrix_determinant(a: np.ndarray) -> float:
    """
    Вычисление определителя квадратной матрицы.

    Args:
        a (np.ndarray): Квадратная матрица.

    Returns:
        float: Определитель матрицы.
    """
    return float(np.linalg.det(a))


def matrix_inverse(a: np.ndarray) -> np.ndarray:
    """
    Вычисление обратной матрицы.

    Args:
        a (np.ndarray): Квадратная матрица.

    Returns:
        np.ndarray: Обратная матрица.
    """
    return np.linalg.inv(a)


def solve_linear_system(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Решение системы линейных уравнений Ax = b.

    Args:
        a (np.ndarray): Матрица коэффициентов A.
        b (np.ndarray): Вектор свободных членов b.

    Returns:
        np.ndarray: Вектор решений x.
    """
    return np.linalg.solve(a, b)


# ============================================================
# 4. СТАТИСТИЧЕСКИЙ АНАЛИЗ
# ============================================================

def load_dataset(path: str = "data/students_scores.csv") -> np.ndarray:
    """
    Загрузка CSV файла и возврат данных в виде массива NumPy.

    Args:
        path (str): Путь к CSV файлу.

    Returns:
        np.ndarray: Загруженные данные в виде массива.
    """
    return pd.read_csv(path).to_numpy()


def statistical_analysis(data: np.ndarray) -> Dict[str, float]:
    """
    Оценка статистических показателей одномерного массива данных.

    Args:
        data (np.ndarray): Одномерный массив данных.

    Returns:
        dict: Словарь со статистическими показателями.
    """
    return {
        "mean": float(np.mean(data)),
        "median": float(np.median(data)),
        "std": float(np.std(data)),
        "min": float(np.min(data)),
        "max": float(np.max(data)),
        "percentile_25": float(np.percentile(data, 25)),
        "percentile_75": float(np.percentile(data, 75))
    }


def normalize_data(data: np.ndarray) -> np.ndarray:
    """
    Min-Max нормализация массива данных.

    Args:
        data (np.ndarray): Входной массив данных.

    Returns:
        np.ndarray: Нормализованный массив данных в диапазоне [0, 1].
    """
    min_val = np.min(data)
    max_val = np.max(data)
    return (data - min_val) / (max_val - min_val)


# ============================================================
# 5. ВИЗУАЛИЗАЦИЯ
# ============================================================

# Настройка стиля seaborn для всех графиков
sns.set_theme(style="whitegrid")




def plot_histogram(data: np.ndarray) -> None:
    """
    Построить и сохранить гистограмму распределения данных.

    Args:
        data (np.ndarray): Данные для построения гистограммы.
    """
    os.makedirs("plots", exist_ok=True)

    if data.ndim > 1:
        data = data.flatten()

    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=5, color="skyblue", edgecolor="black", alpha=0.7)

    plt.title("Гистограмма распределения")
    plt.xlabel("Значение")
    plt.ylabel("Частота")
    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig("plots/histogram.png", dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()


def plot_heatmap(matrix: np.ndarray) -> None:
    """
    Построить и сохранить тепловую карту корреляции.

    Args:
        matrix (np.ndarray): Матрица корреляции (квадратная).
    """
    os.makedirs("plots", exist_ok=True)

    plt.figure(figsize=(10, 8))
    sns.heatmap(
        matrix,
        annot=True,
        fmt=".2f",
        cmap="YlGnBu",
        center=0,
        square=True,
        linewidths=1.5,
        linecolor="white",
        cbar_kws={"label": "Корреляция"},
    )

    plt.title("Тепловая карта корреляции", fontsize=16, fontweight="bold", pad=20)
    plt.xlabel("Признаки", fontsize=12)
    plt.ylabel("Признаки", fontsize=12)

    plt.xticks(rotation=0, ha="right", fontsize=10)
    plt.yticks(rotation=0, fontsize=10)

    plt.tight_layout()
    plt.savefig("plots/heatmap.png", dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()


def plot_line(x: np.ndarray, y: np.ndarray) -> None:
    """
    Построить и сохранить линейный график: студент → оценка.

    Args:
        x (np.ndarray): Номера студентов (ось X).
        y (np.ndarray): Оценки студентов (ось Y).
    """
    os.makedirs("plots", exist_ok=True)

    width = max(12, len(x) * 0.5)
    plt.figure(figsize=(width, 6))

    plt.plot(
        x,
        y,
        marker="o",
        linestyle="-",
        color="steelblue",
        markersize=5,
        linewidth=1,
        markerfacecolor="red",
        markeredgecolor="darkred",
        label="Оценка по математике",
    )

    plt.title(
        "Зависимость оценки по математике от номера студента",
        fontsize=14,
        fontweight="bold",
        pad=15,
    )
    plt.xlabel("Номер студента", fontsize=12)
    plt.ylabel("Оценка", fontsize=12)

    plt.grid(True, alpha=0.3, linestyle="--")
    plt.legend(fontsize=10)

    n_students = len(x)
    if n_students <= 25:
        plt.xticks(x, rotation=0, ha="right", fontsize=9)
    elif n_students <= 50:
        plt.xticks(x, rotation=90, fontsize=8)
    else:
        step = max(1, n_students // 25)
        plt.xticks(x[::step], rotation=0, ha="right", fontsize=9)

    plt.tight_layout()
    plt.savefig("plots/line_plot.png", dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()


if __name__ == "__main__":
    # 1. Загружаем все данные
    full_data = load_dataset()

    # 2. Выделяем оценки по математике (первый столбец)
    math_data = full_data[:, 0]
    student_ids = np.arange(1, len(math_data) + 1)

    # 3. Считаем матрицу корреляции
    corr_matrix = np.corrcoef(full_data, rowvar=False)

    # 4. Запуск визуализации с ПРАВИЛЬНЫМИ данными
    plot_line(student_ids, math_data)
    plot_histogram(math_data)
    plot_heatmap(corr_matrix)
