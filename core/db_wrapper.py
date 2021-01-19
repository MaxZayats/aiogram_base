from databases import Database
import asyncpg

from settings.config import database_url


database = Database(database_url)

# do something with database