from typing import TypeVar, Generic, Iterable

from repository import CrudRepository

T = TypeVar('T')
ID = TypeVar('ID')

class SelectionRepository(CrudRepository, Generic[T, ID]):

    def __init__(self):
        self._a = ["a", "b", "c", "d"]

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

    def find_all_by_id(self, id: ID) -> Iterable[T]:
        r = []
        for e in self._a:
            if e == id:
                r.append(e)
        return r

    def find_by_id(self, id: ID) -> None:
        found = self.find_all_by_id(id)

        if len(found) == 0:
            return None
        else:
            return found[0]

    def find_one(self, id: ID) -> T:
        found = self.find_all_by_id(id)

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

    def delete_by_id(self, id: ID):
        self._a.pop(id)

    def exists_by_id(self, id: ID) -> bool:
        return id in self._a

if __name__ == '__main__':
    print(issubclass(SelectionRepository, CrudRepository))
    
    r = SelectionRepository[str,int]()
    print(r.count())
    
    ns1 = "f"
    s = r.save(ns1)
    print(s)
    
    ns2 = ["g", "h"]
    r.save_all(ns2)
    print(r.find_all())
    
    print(r.exists_by_id("g"))

    print(r.exists_by_id("e"))

    r.delete("h")
    print(r.find_all())

    r.delete_by_id(0)
    print(r.find_all())

    r.delete_all()
    print(r.find_all())
    
    print(r.count())
    
