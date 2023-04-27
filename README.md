# python aiohttp server w/ jquery single page web app

### to deploy on ubuntu vm

setting up postgresql database

```
sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common
sudo -i -u postgres
createuser yourlinuxusername -P --interactive
```
- this will prompt you for a password, use "yourlinuxpassword" without the quotes of coarse

- answer yes to all questions

```
createdb pyaiodatabase
git clone https://github.com/noitpecedfles/pyaioserver.git
psql pyaiodatabase
\i 'pyaioserver/source/resources/schema.sql'
\q
cd pyaioserver
python3 -m venv env
. env/bin/activate
pip install -r python_requirements.txt
cd source
nano resources/db_connection.py
```
paste the following text into the file, obviously you must replace with your information:

- secret = {'database': 'pyaiodatabase', 'user': 'yourlinuxusername', 'password':'yourlinuxpassword'}

ctrl+o to save & ctrl+x to exit the nano program

you should have retured to the comandline, now just run the app with the following command

``` python app.py ```

### note

if you see frequent commits it's because I am testing on a remote server, using git to ferry code back and forth

### current bug

Exception in callback Connection._ready(<weakref at 0...x7f595390c940>) at /home/webapp/pyaioserver/env/lib/python3.10/site-packages/aiopg/connection.py:779
handle: <Handle Connection._ready(<weakref at 0...x7f595390c940>) at /home/webapp/pyaioserver/env/lib/python3.10/site-packages/aiopg/connection.py:779>
Traceback (most recent call last):
  File "/usr/lib/python3.10/asyncio/events.py", line 80, in _run
    self._context.run(self._callback, *self._args)
  File "/home/webapp/pyaioserver/env/lib/python3.10/site-packages/aiopg/connection.py", line 837, in _ready
    self._loop.add_writer(
  File "/usr/lib/python3.10/asyncio/selector_events.py", line 341, in add_writer
    self._add_writer(fd, callback, *args)
  File "/usr/lib/python3.10/asyncio/selector_events.py", line 299, in _add_writer
    self._selector.modify(fd, mask | selectors.EVENT_WRITE,
  File "/usr/lib/python3.10/selectors.py", line 390, in modify
    self._selector.modify(key.fd, selector_events)
FileNotFoundError: [Errno 2] No such file or directory
Error handling request
