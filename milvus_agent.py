from pymilvus import Collection, FieldSchema, CollectionSchema, DataType, connections,utility

class MilvusAgent:
    def __init__(self):

        connections.connect("default", host="127.0.0.1", port="19530")

    def create_db(self, collection_name):
  
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
            FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=128)
        ]
        schema = CollectionSchema(fields)
   
        collection = Collection(name=collection_name, schema=schema)
        return f"Collection {collection_name} created."

    def insert_data(self, collection_name, data):

        collection = Collection(name=collection_name)
      
        collection.insert(data)
        return f"Inserted data into {collection_name}."

    def create_index(self, collection_name):
    
        collection = Collection(name=collection_name)
        index_params = {
            "index_type": "IVF_FLAT",
            "metric_type": "L2",
            "params": {"nlist": 128}
        }
        collection.create_index(field_name="vector", index_params=index_params)
        return f"Index created for collection {collection_name}."

    def search_data(self, collection_name, vector):
      
        collection = Collection(name=collection_name)
        collection.load()  

        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}

        results = collection.search([vector], "vector", search_params, limit=5)
        return results

    def delete_data(self, collection_name, ids):
     
        collection = Collection(name=collection_name)
        collection.delete(f"id in {ids}")
        return f"Deleted data from {collection_name} where id in {ids}."
    def list_collections(self):
     
        collections = utility.list_collections()
        return collections
    
    def retrieve_data(self, collection_name, ids):
        collection = Collection(name=collection_name)
        collection.load()
        results = collection.query(expr=f"id in {ids}")
        return results
