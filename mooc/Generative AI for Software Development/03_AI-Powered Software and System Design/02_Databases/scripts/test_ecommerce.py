from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///ecommerce.db", echo=True)

# Test the connection
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print(f"Connection successful: {result.scalar()}")

        # Print all tables
        tables_result = connection.execute(
            text("SELECT name FROM sqlite_master WHERE type='table';")
        )
        tables = tables_result.fetchall()
        print("Tables in the database:", [table[0] for table in tables])
except Exception as e:
    print(f"Connection failed: {e}")
