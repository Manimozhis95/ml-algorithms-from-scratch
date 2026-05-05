import duckdb
from pathlib import Path


def load_data():
    #Get project root folder 
    root = Path(__file__).resolve().parents[1]

    #Path to CSV
    file_path=root/"data"/"raw"/"StudentsPerformance.csv"

    #Load using duckdb
    query = f"SELECT * FROM read_csv_auto('{file_path.as_posix()}')"
    return duckdb.query(query).to_df()

# def get_avg_score_by_gender():
#     root=Path(__file__).resolve().parents[1]
#     file_path=root/"data"/"raw"/"StudentsPerformance.csv"
#     query=f"""SELECT gender,
#                     AVG(math score) AS avg_math,
#                     AVG()

if __name__=="__main__":
    df = load_data()
    print(df.head())