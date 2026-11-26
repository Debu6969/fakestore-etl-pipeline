import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL

load_dotenv()

def load_to_postgres(df, table_name):
    connection_url = URL.create(
        drivername='postgresql+psycopg',
        username=user,
        password=password,
        host=host,
        port=port,
        database=db_name
    )

    engine = create_engine(connection_url)
    df.to_sql(table_name,
              engine,
              if_exists='replace',
              index = False)

    print('data loaded to postgres successfully')