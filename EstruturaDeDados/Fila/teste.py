class FilaRecursiva:
    def __init__(self):
        self.fila = []

    def enfileirar(self, elemento):
        self.fila.append(elemento)

    def desenfileirar(self):
        if len(self.fila) == 0:
            raise IndexError("Fila vazia!")
        return self._desenfileirar_recursivo()

    def _desenfileirar_recursivo(self):
        if len(self.fila) == 1:
            return self.fila.pop(0)
        else:
            primeiro = self.fila.pop(0)
            valor = self._desenfileirar_recursivo()
            self.enfileirar(primeiro)  # Coloca o primeiro de volta
            return valor

    def esta_vazia(self):
        return len(self.fila) == 0

# Exemplo de uso
fila = FilaRecursiva()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)

print(fila.desenfileirar())  # Saída: 1
print(fila.desenfileirar())  # Saída: 2
print(fila.desenfileirar())  # Saída: 3
print(fila.desenfileirar())