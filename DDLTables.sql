-- Usuário
CREATE TABLE Usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_nascimento DATE
);

-- Artista
CREATE TABLE Artista (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    pais VARCHAR(50),
    genero_musical_principal VARCHAR(50)
);

-- Gênero
CREATE TABLE Genero (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

-- Álbum
CREATE TABLE Album (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    data_lancamento DATE,
    artista_id INTEGER REFERENCES Artista(id) NOT NULL
);

-- Música com artista_id
CREATE TABLE Musica (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    duracao VARCHAR(20), -- duração em segundos
    album_id INTEGER REFERENCES Album(id),
    artista_id INTEGER REFERENCES Artista(id) NOT NULL
);

-- Música_Gênero
CREATE TABLE Musica_Genero (
    musica_id INTEGER REFERENCES Musica(id) ON DELETE CASCADE,
    genero_id INTEGER REFERENCES Genero(id) ON DELETE CASCADE,
    PRIMARY KEY (musica_id, genero_id)
);

-- Playlist
CREATE TABLE Playlist (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_criacao TIMESTAMP DEFAULT now()
);
