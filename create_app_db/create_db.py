import aiopg.sa


def create_db(config):
    return aiopg.sa.create_engine(user=config['user'],
                                  database=config['database'],
                                  host=config['host'],
                                  password=config['password'])
