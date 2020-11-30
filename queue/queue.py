# Creating an abstract class for any queue

from abc import ABC, abstractmethod


class Queue(ABC):

    @abstractmethod
    def offer(self, elem):
        pass

    @abstractmethod
    def poll(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

