import logging
import os

from peewee import OperationalError, IntegrityError

from monkeys.models import database, DATABASE_PATH, Monkey, UserRequest, Task

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DATABASE_MODELS = [
    Monkey,
    UserRequest,
    Task
]

def setup():
    logger.info("Starting database setup...")

    try:
        logger.info(f"Connecting to database: {DATABASE_PATH}")

        database.connect()

        logger.info("Database connection established")

        logger.info("Creating tables if they don't exist...")

        database.create_tables(
            DATABASE_MODELS,
            safe=True
        )
        logger.info("Tables created successfully")

        logger.info("Verifying table creation...")

        tables_created = database.get_tables()

        logger.info(f"Tables in database: {tables_created}")

        try:
            logger.info("Testing database connectivity...")

            tables = database.get_tables()

            logger.info(f"Database contains {len(tables)} tables: {tables}")

            for model in DATABASE_MODELS:
                if model.table_exists():
                    logger.info(f"{model.__name__.lower()} table is accessible")

            logger.info("Database connection test passed")

        except Exception as e:
            logger.error(f"Database connection test failed: {e}")

    except OperationalError as e:
        logger.error(f"Database connection error: {e}")

    except IntegrityError as e:
        logger.error(f"Data integrity error: {e}")

    except Exception as e:
        logger.error(f"Unexpected error during setup: {e}")

    finally:
        if not database.is_closed():
            database.close()
            logger.info("Database connection closed")
