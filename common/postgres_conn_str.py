def get_pg_conn_str(dbname: str, host: str = '127.0.0.1', port: int = 5432, user: str = 'postgres',
                    password: int = 123):
    return f"host={host} port={port} user={user} password={password} dbname={dbname}"
