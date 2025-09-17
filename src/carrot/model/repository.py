from abc import ABC, ABCMeta, abstractmethod
from typing import TypeVar, Generic, Iterable #, List, Optional

T = TypeVar('T')
ID = TypeVar('ID')

class CrudRepository(Generic[T, ID], metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'save') and 
            callable(subclass.save) and 
            hasattr(subclass, 'save_all') and 
            callable(subclass.save_all) and 
            hasattr(subclass, 'find_all') and 
            callable(subclass.find_all) and
            hasattr(subclass, 'find_all_by_id') and 
            callable(subclass.find_all_by_id) and
            hasattr(subclass, 'find_by_id') and 
            callable(subclass.find_by_id) and
            hasattr(subclass, 'find_one') and 
            callable(subclass.find_one) and
            hasattr(subclass, 'count') and 
            callable(subclass.count) and
            hasattr(subclass, 'delete') and 
            callable(subclass.delete) and
            hasattr(subclass, 'delete_all') and 
            callable(subclass.delete_all) and
            hasattr(subclass, 'delete_by_id') and 
            callable(subclass.delete_by_id) and
            hasattr(subclass, 'exists_by_id') and 
            callable(subclass.exists_by_id)
        )

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def save(self, entity: T) -> T:
        pass

    @abstractmethod
    def save_all(self, entities: Iterable[T]) -> Iterable[T]:
        pass

    @abstractmethod
    def find_all(self) -> Iterable[T]:
        pass

    @abstractmethod
    def find_all_by_id(self, id: ID) -> Iterable[T]:
        pass

    @abstractmethod
    def find_by_id(self, id: ID) -> None:
        pass

    @abstractmethod
    def find_one(self, id: ID) -> T:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def delete(self, entity: T):
        pass

    @abstractmethod
    def delete_all(self):
        pass

    @abstractmethod
    def delete_by_id(self, id: ID):
        pass

    @abstractmethod
    def exists_by_id(self, id: ID) -> bool:
        pass
