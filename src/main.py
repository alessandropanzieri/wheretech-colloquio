from ingestion import get_ingestion
from database import create_database
from connection import get_connection

url = "https://portalgis.wheretech.it/server/rest/services/VERTIGIS_TRAINING/Direttiva_alluvioni_v2/MapServer/8/query"
params = {
    "where": "1=1",
    "outFields": "*",
    "f": "pjson"
}

if __name__ == "__main__":

    print("ingestion data are being get...")
    ingestion_data = get_ingestion(url, params)
    print("ingestion data were get successfully")

    connection = get_connection()
    print("connection was established successfully")
    cursor = connection.cursor()

    create_database("test", ingestion_data, connection, cursor)