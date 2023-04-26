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
    existing = await cur.fetchone()
    if existing:
        conn.close()
        return 0
    else:
        await cur.execute(
            "INSERT INTO auth (username, password) VALUES (%s,%s) RETURNING id;",
            (username, bcrypt.hashpw(password.encode('utf8'), salt)))
        ret = await cur.fetchone()
        conn.close()
        if ret:
            return ret[0]
        else:
            return 0

async def _login(username,password):
    conn = await aiopg.connect(database=secret['database'],
                               user=secret['user'],
                               password=secret['password'],
                               host='127.0.0.1')
    cur = await conn.cursor()
    await cur.execute(
        "SELECT id, password FROM auth WHERE username = %s;",
        (username,))
    ret = await cur.fetchone()
    conn.close()
    if ret and bcrypt.checkpw(password.encode('utf8'), bytes(ret[1])):
        return ret[0]
    else:
        return 0