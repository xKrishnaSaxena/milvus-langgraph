from milvus_agent import MilvusAgent
import random

def main():
    agent = MilvusAgent()

 
    print(agent.create_db("my_new_collection"))

 
    data = [
        [i for i in range(10)],  
        [[random.random() for _ in range(128)] for _ in range(10)]
    ]
    print(agent.insert_data("my_new_collection", data))


    print(agent.create_index("my_new_collection"))

   
    random_vector = [random.random() for _ in range(128)]
    results = agent.search_data("my_new_collection", random_vector)
    print("Search Results:", results)


    # print(agent.delete_data("my_new_collection", [1, 2, 3]))

    
    collections = agent.list_collections()
    print("Collections in Milvus:", collections)

    print(agent.retrieve_data("my_new_collection", [1, 2, 3]))


if __name__ == "__main__":
    main()
