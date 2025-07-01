from abc import ABC, abstractmethod

class BasePageClass(ABC):
    @abstractmethod
    def set_url(url: str):
        pass