from abc import ABC, abstractmethod
from typing import List
from schemas import RetrievedDocumentSchema

class VectorDBInterface(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def is_collection_exist(self, collection_name : str) -> bool:
        pass

    @abstractmethod
    def list_all_collections(self) -> List:
        pass

    def get_collection_info(self, collection_name : str) -> dict:
        pass

    @abstractmethod
    def delete_collection(self, collection_name : str):
        pass

    @abstractmethod
    def create_collection(self, collection_name : str,
                          embedding_size : int,do_reset : bool = False):
        pass


    def insert_one(self, collection_name : str, text : str, vector : list,
                   metadata : dict = None,
                   record_id : int = None):
        pass


    def insert_many(self, collection_name : str, texts : list, vectors : list,
                   metadatas :  list = None,
                   record_ids : list = None, batch_size : int = 50):
        
        pass

    
    def search_by_vector(self, collection_name : str, vector : list, limit : int) -> List[RetrievedDocumentSchema]:
        pass
