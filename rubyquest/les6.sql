PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE sporten(id integer primary key,name);
CREATE TABLE personen(id integer primary key autoincrement,name);
CREATE TABLE personen_sporten(persoon_id integer,sport_id integer,primary key(persoon_id,sport_id));
COMMIT;
