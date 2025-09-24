from model.selection import Selection
from model.selection_repository import SelectionRepository

if __name__ == '__main__':
    # print(issubclass(SelectionRepository, CrudRepository))
    
    r = SelectionRepository()
    with r as sr:
        print('doing something with sr')
    
    # r = SelectionRepository[str,int]()
    # print(r.count())
    
    # ns1 = "f"
    # s = r.save(ns1)
    # print(s)
    
    # ns2 = ["g", "h"]
    # r.save_all(ns2)
    # print(r.find_all())
    
    # print(r.exists_by_id("g"))

    # print(r.exists_by_id("e"))

    # r.delete("h")
    # print(r.find_all())

    # r.delete_by_id(0)
    # print(r.find_all())

    # r.delete_all()
    # print(r.find_all())
    
    # print(r.count())
    
    s = Selection(crc32 = 0xdead0001, file_size = 0x1000beef)
    print(s.id)