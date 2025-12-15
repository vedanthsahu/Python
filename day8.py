import os
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError, NotFoundError, RequestError

ES_HOST = os.getenv("ES_HOST", "http://172.19.179.185:9200")

# Initialize Elasticsearch client
es = Elasticsearch(ES_HOST, verify_certs=False)


def check_connection():
    """Verify that Elasticsearch is reachable."""
    try:
        info = es.info()
        print("===== Elasticsearch Connection Successful =====")
        print(f"Cluster Name: {info['cluster_name']}")
        print(f"Node Name: {info['name']}")
        print(f"Version: {info['version']['number']}")
        print("===============================================\n")
        return True
    except Exception as e:
        print("Connection to Elasticsearch FAILED")
        print(str(e))
        return False


def list_indexes():
    """List all indexes in Elasticsearch."""
    try:
        indexes = es.indices.get_alias("*")
        print("===== Available Indexes =====")
        for idx in indexes.keys():
            print(f"- {idx}")
        print("=============================\n")
    except Exception as e:
        print("Error listing indexes:", e)


def show_mappings(index):
    """Show mappings (schema) of a given index."""
    try:
        if not es.indices.exists(index=index):
            print(f"Index '{index}' does NOT exist.\n")
            return

        mappings = es.indices.get_mapping(index=index)
        print(f"===== Mappings for Index: {index} =====")
        print(mappings[index]["mappings"])
        print("=========================================\n")

    except Exception as e:
        print("Error fetching mappings:", e)


def show_sample_documents(index, size=5):
    """Fetch sample documents from the index."""
    try:
        if not es.indices.exists(index=index):
            print(f"Index '{index}' does NOT exist.\n")
            return

        result = es.search(index=index, query={"match_all": {}}, size=size)
        hits = result["hits"]["hits"]

        print(f"===== Sample Documents from '{index}' (limit {size}) =====")
        if not hits:
            print("No documents found.\n")
            return

        for i, hit in enumerate(hits, 1):
            print(f"--- Document {i} ---")
            print(hit["_source"])
        print("=========================================================\n")

    except Exception as e:
        print("Error fetching documents:", e)


def show_index_stats(index):
    """Display stats such as document count and storage size."""
    try:
        if not es.indices.exists(index=index):
            print(f"Index '{index}' does NOT exist.\n")
            return

        stats = es.indices.stats(index=index)
        total = stats["indices"][index]["total"]

        print(f"===== Stats for Index: {index} =====")
        print(f"Document Count: {total['docs']['count']}")
        print(f"Storage Size (bytes): {total['store']['size_in_bytes']}")
        print("=====================================\n")

    except Exception as e:
        print("Error fetching stats:", e)


def main():
    if not check_connection():
        return

    list_indexes()

    index = input("Enter index name to explore: ").strip()

    show_mappings(index)
    show_index_stats(index)
    show_sample_documents(index, size=10)


if __name__ == "__main__":
    main()



from langchain_core.prompts import ChatMessagePromptTemplate






















