CREATE database test;

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

-- Path: test/sqlite3/data.sql

INSERT INTO user (username, password) VALUES ('alice', 'alice');
INSERT INTO user (username, password) VALUES ('bob', 'bob');
INSERT into post (author_id, title, body) VALUES (1, 'Hello', 'Hello world!');
INSERT into post (author_id, title, body) VALUES (1, 'Goodbye', 'Goodbye world!');
