from collections import deque
from collections import Counter


class GestureBuffer:
    def __init__(self, size=10):
        self.buffer = deque(maxlen=size)

    def update(self, gesture):

        self.buffer.append(tuple(gesture))

        if len(self.buffer) < self.buffer.maxlen:  # type: ignore
            return None

        most_common = Counter(self.buffer).most_common(1)[0][0]

        return list(most_common)
