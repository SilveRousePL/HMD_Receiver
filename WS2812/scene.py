from abc import ABC, abstractmethod
import threading

class Scene(ABC):
    @abstractmethod
    def do(self, step, led_count):
        Tuple
        return List((0, 0, 0), led_count)
