from typing import TypeVar, Generic, Iterable
import csv
from .repository import CrudRepository

T = TypeVar('T')
ID = TypeVar('ID')

class SelectionRepository(CrudRepository, Generic[T, ID]):

    def __init__(self):
        self._a = ["a", "b", "c", "d"]
        
    def __enter__(self):
        print('__enter__')
        return 'main body'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')

    def save(self, entity: T) -> T:
        self._a.append(entity)
        return entity

    def save_all(self, entities: Iterable[T]) -> Iterable[T]:
        saved = []
        for e in entities:
            s = self.save(e)
            saved.append(s)
        return saved

    def find_all(self) -> Iterable[T]:
        return self._a

    def find_all_by_id(self, oid: ID) -> Iterable[T]:
        r = []
        for e in self._a:
            if e == oid:
                r.append(e)
        return r

    def find_by_id(self, oid: ID) -> None:
        found = self.find_all_by_id(oid)

        if len(found) == 0:
            return None
        else:
            return found[0]

    def find_one(self, oid: ID) -> T:
        found = self.find_all_by_id(oid)

        if len(found) == 0:
            return None
        else:
            return found[0]

    def count(self) -> int:
        return len(self._a)

    def delete(self, entity: T):
        self._a.remove(entity)

    def delete_all(self):
        self._a.clear()

    def delete_by_id(self, oid: ID):
        self._a.pop(oid)

    def exists_by_id(self, oid: ID) -> bool:
        return oid in self._a

