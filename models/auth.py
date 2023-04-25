import asyncio
import aiopg
import bcrypt
from resources.db_connection import secret

salt = bcrypt.gensalt()

async def _register(username,password):
    conn = await aiopg.connect(database=secret['database'],
                               user=secret['user'],
                               password=secret['password'],
                               host='127.0.0.1')
    cur = await conn.cursor()
    await cur.execute(
        "SELECT id FROM auth WHERE username = %s;",
        (username,))
    problem = await cur.fetchone()
    if problem:
        conn.close()
        return None
    else:
        await cur.execute(
            "INSERT INTO auth (username, password) VALUES (%s,%s) RETURNING id;",
            (username, bcrypt.hashpw(password.encode('utf-8'), salt).decode("utf-8")))
        ret = await cur.fetchone()
        conn.close()
        return ret

async def _login(username,password):
    conn = await aiopg.connect(database=secret['database'],
                               user=secret['user'],
                               password=secret['password'],
                               host='127.0.0.1')
    cur = await conn.cursor()
    await cur.execute(
        "SELECT id FROM auth WHERE username = %s AND password = %s;",
        (username, bcrypt.hashpw(password.encode('utf-8'), salt).decode("utf-8")))
    ret= await cur.fetchone()
    conn.close()
    return ret