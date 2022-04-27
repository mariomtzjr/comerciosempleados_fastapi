import os


def get_database_path(db_file):
    """Get the path of the database file"""

    db_file_path = os.path.join(os.path.dirname(__file__), f'{db_file}')
    normalized_db_file_path = os.path.normpath(db_file_path)

    return normalized_db_file_path