# Genetic Algorithm – Sum of Squares Minimization

This project implements a **Genetic Algorithm (GA)** in Python to minimize the mathematical function:

\[
f(x) = sum(xi ^ 2)
\]

The goal is to find the vector **x** where each element is close to 0, which minimizes the overall sum of squares.

---

## 🧠 Algorithm Overview

This GA uses the following steps:

- **Initialization:** Random population within the domain [-5.12, 5.12]
- **Selection:** Binary tournament selection
- **Crossover:** Single-point crossover with 80% probability
- **Mutation:** Random mutation with 20% probability
- **Evaluation:** Fitness = sum of squares

---

## ⚙️ How to Run

Make sure you have Python and `matplotlib` installed. Then run:

```bash
python ga_sum_of_squares.py
```

A plot will be saved to:
```
genetic/output_plot.png
```

---

## 🔧Parameters

You can customize these parameters at the bottom of the script:
```
POP_SIZE = 50          # Number of individuals in the population
LOWER_BOUND = -5.12    # Minimum value of each gene
UPPER_BOUND = 5.12     # Maximum value of each gene
GENERATIONS = 100      # Number of generations
NUM_VARIABLES = 5      # Number of genes in each chromosome
```
---
## 📈Sample Output

```
in generation 100 --> the best fitness in each section: 0.0008, the best chromosome in each section: [0.0031, -0.0012, 0.0005, 0.0007, -0.0020]
```

---



