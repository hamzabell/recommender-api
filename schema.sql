DROP TABLE IF EXISTS articles;


CREATE TABLE articles (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                              created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                                                                 Title TEXT NOT NULL,
                                                                                            Description TEXT NOT NULL,
                                                                                                             link Text NOT NULL);


CREATE TABLE updates ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                                              created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                                                                 update_id INTEGER NOT NULL);