# Pygame Sorting Algorithm Visualizer

Aplicação interativa desenvolvida em **Python** utilizando a biblioteca **Pygame** para visualização gráfica em tempo real de algoritmos de ordenação clássicos.

---

## 🚀 Sobre o Projeto

Este projeto une a teoria de estruturas de dados e análise de complexidade à programação gráfica, permitindo observar visualmente o comportamento, as trocas e a eficiência de diferentes algoritmos de ordenação:
* **Visualização Gráfica Dinâmica:** Representação por colunas/barras cujas alturas correspondem aos valores numéricos, coloridas dinamicamente consoante o estado de comparação ou troca.
* **Algoritmos Implementados:** Comparação visual de desempenho entre abordagens de complexidade $O(n^2)$ (como Bubble Sort e Insertion Sort) e $O(n \log n)$ (como Merge Sort ou Quick Sort).
* **Controlo de Execução:** Gestão de loops de renderização fluidos usando o relógio do Pygame para garantir controlabilidade da velocidade de animação.

---

## 🛠️ Stack Tecnológica

* **Linguagem:** Python
* **Biblioteca Gráfica:** Pygame
* **Conceitos de Engenharia:** Algoritmos de Ordenação, Complexidade Computacional ($O$), Computação Gráfica 2D e Gestão de Eventos/Loops de Jogo

---

## 📊 Arquitetura e Funcionamento

1. **Geração de Dados:** Criação de um array pseudo-aleatório de valores numéricos mapeados para a janela de renderização.
2. **Loop de Eventos:** Tratamento de entradas do utilizador (como iniciar a ordenação, pausar ou reiniciar o array).
3. **Renderização por Frames:** Atualização visual imediata a cada operação de comparação ou troca de elementos no array.

---

## ⚙️ Como Executar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/Lucas-IudiCG/Pygame-Sorting-algorithm.git](https://github.com/Lucas-IudiCG/Pygame-Sorting-algorithm.git)
   cd Pygame-Sorting-algorithm
