from collections import deque


class GestureStabilizer:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.history = deque(maxlen=window_size)

    def update(self, gesture):
        self.history.append(gesture)

        if len(self.history) < self.window_size:
            return None

        # verifica se todos os gestos na janela são iguais
        first = self.history[0]
        if all(g == first for g in self.history):
            return first

        return None
