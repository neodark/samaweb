cat ../neomatrix_samaweb.sql | perl mysql2sqlite.pl | sqlite3 db.sqlite3

ALTER table samacore_course ADD column course_price INT NOT NULL DEFAULT 70;
