import tkinter as tk
from tkinter import Entry, messagebox
import math

help_info = {
    "Arranjo Simples": "Esta função calcula o Arranjo Simples de dois números inteiros 'n' e 'k'.",
    "Arranjo com Repetição": "Esta função calcula o Arranjo com Repetição de dois números inteiros 'n' e 'k'.",
    "Combinação Simples": "A fórmula da Combinação Simples é usada para calcular o número de maneiras diferentes de escolher k elementos distintos de um conjunto de n elementos, onde a ordem em que os elementos são escolhidos não é importante, e a repetição de elementos não é permitida. A fórmula é a seguinte: C(n, k) = n! / [k! * (n - k)!]",
    "Produto Escalar": "Teorema. Fórmula geométrica do produto escalar. Sejam A e B dois vetores se ambos forem não-nulos, então: A⋅B=∣A∣⋅∣B∣⋅cos(θ). Em que θ é o ângulo formado por eles. Se um deles for nulo, então: A⋅B = 0",
    "Produto Vetorial": "O produto vetorial entre dois vetores U = (u1,u2,u3) e V = (v1,v2,v3) é dado por: U x V = (u2*v3 - u3*v2, u3*v1 - u1*v3, u1*v2 - u2*v1).",
    "Produto Misto": "O produto misto é uma operação que envolve o cálculo do produto vetorial de três vetores no espaço tridimensional e, em seguida, o cálculo do produto escalar desse resultado com um terceiro vetor. Matematicamente, dado três vetores a,b,c, o produto misto é calculado da seguinte forma: a⋅(b×c) onde × denota o produto vetorial entre dois vetores e ⋅ denota o produto escalar entre dois vetores."
}

def show_help(topic):
    help_text = help_info.get(topic, "Informações de ajuda não disponíveis para este tópico.")
    messagebox.showinfo("Ajuda", help_text)

def show_subtopic(subtopic):
    subtopic_frame = tk.Frame(root)
    subtopic_label = tk.Label(subtopic_frame, text=f"Subtópicos de {subtopic}")
    subtopic_label.pack()

    if subtopic.lower() == "geometria analítica":
        product_scalar_button = tk.Button(subtopic_frame, text="Produto Escalar", command=show_product_scalar)
        product_scalar_button.pack()

        product_vector_button = tk.Button(subtopic_frame, text="Produto Vetorial", command=show_product_vector)
        product_vector_button.pack()

    produto_misto_button = tk.Button(subtopic_frame, text="Produto Misto", command=show_produto_misto)
    produto_misto_button.pack()

    if subtopic.lower() == "matemática discreta":
        arranjo_button = tk.Button(subtopic_frame, text="Arranjo Simples", command=show_arranjo)
        arranjo_button.pack()

        combinacao_button = tk.Button(subtopic_frame, text="Combinação Simples", command=show_combinacao_simples)
        combinacao_button.pack()

        arranjo_repeticao_button = tk.Button(subtopic_frame, text="Arranjo com Repetição", command=show_arranjo_com_repeticao)
        arranjo_repeticao_button.pack()

    back_button = tk.Button(subtopic_frame, text="Voltar", command=subtopic_frame.destroy)
    back_button.pack()

    subtopic_frame.pack()

def show_help_menu():
    help_window = tk.Toplevel(root)
    help_window.title("Ajuda")
    help_text = "Clique na matéria que você quer saber como faz:"
    help_label = tk.Label(help_window, text=help_text)
    help_label.pack()

    for topic in help_info:
        help_button = tk.Button(help_window, text=topic, command=lambda t=topic: show_help(t))
        help_button.pack()

def show_product_scalar():

  def calculate_product_scalar():
    vector_a_str = vector_a_entry.get()
    vector_b_str = vector_b_entry.get()
    angle_str = angle_entry.get()

    try:
      vector_a = [float(x.strip()) for x in vector_a_str.split(',')]
      vector_b = [float(x.strip()) for x in vector_b_str.split(',')]

      scalar_product = sum(a * b for a, b in zip(vector_a, vector_b))

      angle_degrees = float(angle_str)
      angle_radians = math.radians(angle_degrees)
      cos_angle = math.cos(angle_radians)

      result_frame = tk.Frame(root)
      result_scalar_label = tk.Label(
          result_frame,
          text=f"Resultado do Produto Escalar: {scalar_product * cos_angle:.2f}"
      )
      result_scalar_label.pack()

      result_angle_label = tk.Label(
          result_frame,
          text=f"Ângulo entre os vetores (em graus): {angle_degrees:.2f}")
      result_angle_label.pack()

      result_cos_label = tk.Label(result_frame,
                                  text=f"Cosseno do ângulo: {cos_angle:.2f}")
      result_cos_label.pack()

      back_button = tk.Button(result_frame,
                              text="Voltar",
                              command=result_frame.destroy)
      back_button.pack()

      result_frame.pack()

    except ValueError:
      error_frame = tk.Frame(root)
      error_label = tk.Label(error_frame,
                             text="Erro: Insira valores numéricos válidos.")
      error_label.pack()

      back_button = tk.Button(error_frame,
                              text="Voltar",
                              command=error_frame.destroy)
      back_button.pack()

      error_frame.pack()

  product_scalar_frame = tk.Frame(root)
  product_scalar_label = tk.Label(product_scalar_frame,
                                  text="Cálculo do Produto Escalar")
  product_scalar_label.pack()

  vector_a_label = tk.Label(product_scalar_frame,
                            text="Digite o vetor A (no formato x, y, z):")
  vector_a_label.pack()
  vector_a_entry = Entry(product_scalar_frame)
  vector_a_entry.pack()

  vector_b_label = tk.Label(product_scalar_frame,
                            text="Digite o vetor B (no formato x, y, z):")
  vector_b_label.pack()
  vector_b_entry = Entry(product_scalar_frame)
  vector_b_entry.pack()

  angle_label = tk.Label(product_scalar_frame,
                         text="Digite o ângulo θ (em graus):")
  angle_label.pack()
  angle_entry = Entry(product_scalar_frame)
  angle_entry.pack()

  calculate_button = tk.Button(product_scalar_frame,
                               text="Calcular Produto Escalar e Ângulo",
                               command=calculate_product_scalar)
  calculate_button.pack()

  back_button = tk.Button(product_scalar_frame,
                          text="Voltar",
                          command=product_scalar_frame.destroy)
  back_button.pack()

  product_scalar_frame.pack()


def show_product_vector():

  def calculate_product_vector():
    vector_a_str = vector_a_entry.get()
    vector_b_str = vector_b_entry.get()

    try:
      vector_a = [float(x.strip()) for x in vector_a_str.split(',')]
      vector_b = [float(x.strip()) for x in vector_b_str.split(',')]

      if len(vector_a) != 3 or len(vector_b) != 3:
        raise ValueError

      result = [
          vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1],
          vector_a[2] * vector_b[0] - vector_a[0] * vector_b[2],
          vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]
      ]

      result_frame = tk.Frame(root)
      result_label = tk.Label(result_frame,
                              text=f"Resultado do Produto Vetorial: {result}")
      result_label.pack()

      back_button = tk.Button(result_frame,
                              text="Voltar",
                              command=result_frame.destroy)
      back_button.pack()

      result_frame.pack()

    except ValueError:
      error_frame = tk.Frame(root)
      error_label = tk.Label(
          error_frame,
          text=
          "Erro: Insira três valores numéricos para cada componente do vetor.")
      error_label.pack()

      back_button = tk.Button(error_frame,
                              text="Voltar",
                              command=error_frame.destroy)
      back_button.pack()

      error_frame.pack()

  product_vector_frame = tk.Frame(root)
  product_vector_label = tk.Label(product_vector_frame,
                                  text="Cálculo do Produto Vetorial")
  product_vector_label.pack()

  vector_a_label = tk.Label(product_vector_frame,
                            text="Digite o vetor A (no formato x, y, z):")
  vector_a_label.pack()
  vector_a_entry = Entry(product_vector_frame)
  vector_a_entry.pack()

  vector_b_label = tk.Label(product_vector_frame,
                            text="Digite o vetor B (no formato x, y, z):")
  vector_b_label.pack()
  vector_b_entry = Entry(product_vector_frame)
  vector_b_entry.pack()

  calculate_button = tk.Button(product_vector_frame,
                               text="Calcular Produto Vetorial",
                               command=calculate_product_vector)
  calculate_button.pack()

  back_button = tk.Button(product_vector_frame,
                          text="Voltar",
                          command=product_vector_frame.destroy)
  back_button.pack()

  product_vector_frame.pack()


def show_arranjo():

  def calculate_arranjo_simples():
    n_str = n_entry.get()
    k_str = k_entry.get()

    try:
      n = int(n_str)
      k = int(k_str)

      if n < 0 or k < 0:
        raise ValueError

      result = math.factorial(n) / (math.factorial(n - k))

      result_frame = tk.Frame(root)
      result_label = tk.Label(
          result_frame, text=f"Resultado do Arranjo Simples: {result:.2f}")
      result_label.pack()

      back_button = tk.Button(result_frame,
                              text="Voltar",
                              command=result_frame.destroy)
      back_button.pack()

      result_frame.pack()

    except ValueError:
      error_frame = tk.Frame(root)
      error_label = tk.Label(
          error_frame,
          text=
          "Erro: Insira valores inteiros não negativos válidos para 'n' e 'k'."
      )
      error_label.pack()

      back_button = tk.Button(error_frame,
                              text="Voltar",
                              command=error_frame.destroy)
      back_button.pack()

      error_frame.pack()

  arranjo_frame = tk.Frame(root)
  arranjo_label = tk.Label(arranjo_frame, text="Cálculo do Arranjo Simples")
  arranjo_label.pack()

  n_label = tk.Label(arranjo_frame, text="Digite o valor de 'n':")
  n_label.pack()
  n_entry = Entry(arranjo_frame)
  n_entry.pack()

  k_label = tk.Label(arranjo_frame, text="Digite o valor de 'k':")
  k_label.pack()
  k_entry = Entry(arranjo_frame)
  k_entry.pack()

  calculate_button = tk.Button(arranjo_frame,
                               text="Calcular Arranjo Simples",
                               command=calculate_arranjo_simples)
  calculate_button.pack()

  back_button = tk.Button(arranjo_frame,
                          text="Voltar",
                          command=arranjo_frame.destroy)
  back_button.pack()

  arranjo_frame.pack()


def show_combinacao_simples():

  def calculate_combinacao_simples():
    n_str = n_entry.get()
    k_str = k_entry.get()

    try:
      n = int(n_str)
      k = int(k_str)

      if n < 0 or k < 0:
        raise ValueError

      result = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

      result_frame = tk.Frame(root)
      result_label = tk.Label(
          result_frame, text=f"Resultado da Combinação Simples: {result:.2f}")
      result_label.pack()

      back_button = tk.Button(result_frame,
                              text="Voltar",
                              command=result_frame.destroy)
      back_button.pack()

      result_frame.pack()

    except ValueError:
      error_frame = tk.Frame(root)
      error_label = tk.Label(
          error_frame,
          text=
          "Erro: Insira valores inteiros não negativos válidos para 'n' e 'k'."
      )
      error_label.pack()

      back_button = tk.Button(error_frame,
                              text="Voltar",
                              command=error_frame.destroy)
      back_button.pack()

      error_frame.pack()

  combinacao_frame = tk.Frame(root)
  combinacao_label = tk.Label(combinacao_frame,
                              text="Cálculo da Combinação Simples")
  combinacao_label.pack()

  n_label = tk.Label(combinacao_frame, text="Digite o valor de 'n':")
  n_label.pack()
  n_entry = Entry(combinacao_frame)
  n_entry.pack()

  k_label = tk.Label(combinacao_frame, text="Digite o valor de 'k':")
  k_label.pack()
  k_entry = Entry(combinacao_frame)
  k_entry.pack()

  calculate_button = tk.Button(combinacao_frame,
                               text="Calcular Combinação Simples",
                               command=calculate_combinacao_simples)
  calculate_button.pack()

  back_button = tk.Button(combinacao_frame,
                          text="Voltar",
                          command=combinacao_frame.destroy)
  back_button.pack()

  combinacao_frame.pack()


def show_arranjo_com_repeticao():

  def calculate_arranjo_com_repeticao():
    n_str = n_entry.get()
    k_str = k_entry.get()

    try:
      n = int(n_str)
      k = int(k_str)

      if n < 0 or k < 0:
        raise ValueError

      result = math.pow(n, k)

      result_frame = tk.Frame(root)
      result_label = tk.Label(
          result_frame,
          text=f"Resultado do Arranjo com Repetição: {result:.2f}")
      result_label.pack()

      back_button = tk.Button(result_frame,
                              text="Voltar",
                              command=result_frame.destroy)
      back_button.pack()

      result_frame.pack()

    except ValueError:
      error_frame = tk.Frame(root)
      error_label = tk.Label(
          error_frame,
          text=
          "Erro: Insira valores inteiros não negativos válidos para 'n' e 'k'."
      )
      error_label.pack()

      back_button = tk.Button(error_frame,
                              text="Voltar",
                              command=error_frame.destroy)
      back_button.pack()

      error_frame.pack()

  arranjo_frame = tk.Frame(root)
  arranjo_label = tk.Label(arranjo_frame,
                           text="Cálculo do Arranjo com Repetição")
  arranjo_label.pack()

  n_label = tk.Label(arranjo_frame, text="Digite o valor de 'n':")
  n_label.pack()
  n_entry = Entry(arranjo_frame)
  n_entry.pack()

  k_label = tk.Label(arranjo_frame, text="Digite o valor de 'k':")
  k_label.pack()
  k_entry = Entry(arranjo_frame)
  k_entry.pack()

  calculate_button = tk.Button(arranjo_frame,
                               text="Calcular Arranjo com Repetição",
                               command=calculate_arranjo_com_repeticao)
  calculate_button.pack()

  back_button = tk.Button(arranjo_frame,
                          text="Voltar",
                          command=arranjo_frame.destroy)
  back_button.pack()

  arranjo_frame.pack()
def show_produto_misto():
  def calcular_produto_misto():
      vetor_a_str = vetor_a_entry.get()
      vetor_b_str = vetor_b_entry.get()
      vetor_c_str = vetor_c_entry.get()

      try:
          vetor_a = [float(x.strip()) for x in vetor_a_str.split(',')]
          vetor_b = [float(x.strip()) for x in vetor_b_str.split(',')]
          vetor_c = [float(x.strip()) for x in vetor_c_str.split(',')]

          if len(vetor_a) != 3 or len(vetor_b) != 3 or len(vetor_c) != 3:
              raise ValueError

          produto_vetorial = [
              vetor_a[1] * vetor_b[2] - vetor_a[2] * vetor_b[1],
              vetor_a[2] * vetor_b[0] - vetor_a[0] * vetor_b[2],
              vetor_a[0] * vetor_b[1] - vetor_a[1] * vetor_b[0]
          ]

          produto_misto = sum(a * b for a, b in zip(produto_vetorial, vetor_c))

          resultado_frame = tk.Frame(root)
          resultado_label = tk.Label(
              resultado_frame,
              text=f"Resultado do Produto Misto: {produto_misto:.2f}"
          )
          resultado_label.pack()

          botao_voltar = tk.Button(resultado_frame,
                                   text="Voltar",
                                   command=resultado_frame.destroy)
          botao_voltar.pack()

          resultado_frame.pack()

      except ValueError:
          erro_frame = tk.Frame(root)
          erro_label = tk.Label(
              erro_frame,
              text="Erro: Insira três valores numéricos para cada componente dos vetores."
          )
          erro_label.pack()

          botao_voltar = tk.Button(erro_frame,
                                   text="Voltar",
                                   command=erro_frame.destroy)
          botao_voltar.pack()

          erro_frame.pack()

  produto_misto_frame = tk.Frame(root)
  produto_misto_label = tk.Label(produto_misto_frame,
                                 text="Cálculo do Produto Misto")
  produto_misto_label.pack()

  vetor_a_label = tk.Label(produto_misto_frame,
                           text="Digite o vetor A (no formato x, y, z):")
  vetor_a_label.pack()
  vetor_a_entry = Entry(produto_misto_frame)
  vetor_a_entry.pack()

  vetor_b_label = tk.Label(produto_misto_frame,
                           text="Digite o vetor B (no formato x, y, z):")
  vetor_b_label.pack()
  vetor_b_entry = Entry(produto_misto_frame)
  vetor_b_entry.pack()

  vetor_c_label = tk.Label(produto_misto_frame,
                           text="Digite o vetor C (no formato x, y, z):")
  vetor_c_label.pack()
  vetor_c_entry = Entry(produto_misto_frame)
  vetor_c_entry.pack()

  calcular_botao = tk.Button(produto_misto_frame,
                             text="Calcular Produto Misto",
                             command=calcular_produto_misto)
  calcular_botao.pack()

  botao_voltar = tk.Button(produto_misto_frame,
                           text="Voltar",
                           command=produto_misto_frame.destroy)
  botao_voltar.pack()

  produto_misto_frame.pack()

# Restante do código permanece igual...

root = tk.Tk()
root.title("MathSolver")

buttons_frame = tk.Frame(root)

discreta_button = tk.Button(buttons_frame, text="Matemática Discreta", command=lambda: show_subtopic("Matemática Discreta"))
discreta_button.pack(side=tk.LEFT)

geometria_button = tk.Button(buttons_frame, text="Geometria Analítica", command=lambda: show_subtopic("Geometria Analítica"))
geometria_button.pack(side=tk.LEFT)

help_button = tk.Button(buttons_frame, text="Ajuda", command=show_help_menu)
help_button.pack(side=tk.LEFT)

buttons_frame.pack(pady=10)

root.mainloop()
