DROP TABLE IF EXISTS auth;
CREATE TABLE auth ( ID BIGSERIAL PRIMARY KEY, username VARCHAR(255) UNIQUE NOT NULL, password VARCHAR(255 ) NOT NULL);
