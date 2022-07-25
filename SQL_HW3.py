CREATE TABLE IF NOT EXISTS Singer (
	id SERIAL PRIMARY KEY,
	singer name VARCHAR(40) NOT null
);


CREATE TABLE IF NOT EXISTS genres (
	id SERIAL PRIMARY KEY,
	genre name VARCHAR(40) NOT null
);

CREATE TABLE IF NOT EXISTS SingerGenre (
	singer_id integer references Singer(id),
	genre_id integer references genres(id),
	constraint pk primary key (singer_id, genre_id
);

CREATE TABLE IF NOT EXISTS Album (
	id SERIAL PRIMARY KEY,
	album name VARCHAR(60) NOT NULL,
	release year INTEGER CHECK (release > 0)
);


CREATE TABLE IF NOT EXISTS SingerAlbum (
	singer_id integer references Singer(id),
	album_id integer references Album(id),
	constraint pk primary key (singer_id, album_id)
);

CREATE TABLE IF NOT EXISTS Songs (
	id SERIAL PRIMARY KEY,
	song name VARCHAR(60) NOT NULL,
	duration INTEGER CHECK (duration > 0),
	album id INTEGER REFERENCES Album (id))
);


CREATE TABLE IF NOT EXISTS Compilation (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	release_year INTEGER CHECK (release > 0)
);

CREATE TABLE IF NOT EXISTS CompilationSongs (
	compilation_id integer references Compilation(id),
	songs_id integer references Songs(id),
	constraint pk primary key (compilation_id, songs_id)
);