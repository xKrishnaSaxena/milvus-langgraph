from pymilvus import FieldSchema, CollectionSchema, DataType

def get_milvus_schema():
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=128)
    ]
    return CollectionSchema(fields)
