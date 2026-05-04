import os
import psycopg2
from dotenv import load_dotenv

# Load variables from .env file if it exists (for local development)
load_dotenv("local.env")

def get_db_connection():
    """
    Connects to PostgreSQL. 
    On Vercel, it uses the 'DATABASE_URL' environment variable.
    Locally, it uses your Postgres credentials.
    """
    # Try to get the Neon URL first; fallback to local Postgres settings
    db_url = os.environ.get('DATABASE_URL')
    
    if db_url:
        # For Neon/Vercel
        return psycopg2.connect(db_url)
    else:
        # For Local Setup (Update these with your pgAdmin credentials)
        return psycopg2.connect(
            host="localhost",
            database="resumeproject",
            user="postgres",
            password="Admin@123", # Replace with your real password
            port="5432"
        )

def increment_and_get_visitor_count():
    """
    Updates the visitor table and returns the current count.
    """
    conn = None
    new_count = 0
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # 1. Increment the count for the 'home' page
        # 2. Return the updated value immediately using RETURNING
        query = "UPDATE visitor_counts SET count = count + 1 WHERE page_name = 'home' RETURNING count;"
        cur.execute(query)
        
        result = cur.fetchone()
        if result:
            new_count = result[0]
            conn.commit()
        
        cur.close()
    except Exception as e:
        print(f"Database Error: {e}")
    finally:
        if conn:
            conn.close()
            
    return new_count