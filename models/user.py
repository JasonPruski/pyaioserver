from pprint import pprint
from models.db_connection import secret
import asyncio
import aiopg

async def get_users():
    print("user model called")
    conn = await aiopg.connect(database=secret['database'],
                               user=secret['user'],
                               password=secret['password'],
                               host='127.0.0.1')
    cur = await conn.cursor()
    await cur.execute("SELECT * FROM auth")
    return await cur.fetchall()
