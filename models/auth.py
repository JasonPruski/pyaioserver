from resources.db_connection import secret
import asyncio
import aiopg

async def _register(username,password):
    print("user model called")
    conn = await aiopg.connect(database=secret['database'],
                               user=secret['user'],
                               password=secret['password'],
                               host='127.0.0.1')
    cur = await conn.cursor()
    await cur.execute("INSERT INTO auth (username, password) VALUES (%s,%s) RETURNING id;", (username,password))
    return await cur.fetchall()

async def _login(username,password):
    print("user model called")
    conn = await aiopg.connect(database=secret['database'],
                               user=secret['user'],
                               password=secret['password'],
                               host='127.0.0.1')
    cur = await conn.cursor()
    await cur.execute("SELECT * FROM auth WHERE username = %s AND password = %s;", (username,password))
    return await cur.fetchall()