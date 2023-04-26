# python aiohttp server

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