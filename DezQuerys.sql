--1. Top 5 músicas com maior média de avaliação
SELECT m.titulo, a.nome AS artista, ROUND(AVG(av.nota), 2) AS media_avaliacao
FROM Musica m
JOIN Artista a ON m.artista_id = a.id
JOIN Avaliacao av ON m.id = av.musica_id
GROUP BY m.id, m.titulo, a.nome
ORDER BY media_avaliacao DESC
LIMIT 5


--2. Usuários que mais avaliaram músicas
SELECT u.nome, COUNT(*) AS total_avaliacoes
FROM Usuario u
JOIN Avaliacao av ON u.id = av.usuario_id
GROUP BY u.id, u.nome
ORDER BY total_avaliacoes DESC


--3. Artistas com mais músicas cadastradas
SELECT a.nome AS artista, COUNT(m.id) AS total_musicas
FROM Artista a
LEFT JOIN Musica m ON a.id = m.artista_id
GROUP BY a.id, a.nome
ORDER BY total_musicas DESC

--4. Playlists com mais músicas
SELECT p.nome AS playlist, COUNT(pm.musica_id) AS total_musicas
FROM Playlist p
JOIN Playlist_Musica pm ON p.id = pm.playlist_id
GROUP BY p.id, p.nome
ORDER BY total_musicas DESC


--5. Álbuns mais antigos (top 5)
SELECT titulo, data_lancamento
FROM Album
ORDER BY data_lancamento
LIMIT 5;


--6. Quantidade de artistas por país
SELECT pais, COUNT(*) AS total_artistas
FROM Artista
GROUP BY pais
ORDER BY total_artistas DESC;

--7. Gênero musical mais avaliado (por número de avaliações)
SELECT 
  g.nome AS genero,
  COUNT(av.id) AS total_avaliacoes
FROM Genero g
JOIN Musica_Genero mg ON g.id = mg.genero_id
JOIN Musica m ON mg.musica_id = m.id
JOIN Avaliacao av ON m.id = av.musica_id
GROUP BY g.id, g.nome
ORDER BY total_avaliacoes DESC;

--8. Gêneros mais utilizados em músicas
SELECT g.nome AS genero, COUNT(*) AS total_musicas
FROM Genero g
JOIN Musica_Genero mg ON g.id = mg.genero_id
GROUP BY g.id, g.nome
ORDER BY total_musicas DESC;


--9. Músicas que aparecem em mais playlists
SELECT m.titulo, COUNT(pm.playlist_id) AS total_playlists
FROM Musica m
JOIN Playlist_Musica pm ON m.id = pm.musica_id
GROUP BY m.id, m.titulo
ORDER BY total_playlists DESC;

--10.  Música com mais avaliações 5 estrelas
SELECT m.titulo, COUNT(*) AS avaliacoes_5_estrelas
FROM Musica m
JOIN Avaliacao av ON m.id = av.musica_id
WHERE av.nota = 5
GROUP BY m.id, m.titulo
ORDER BY avaliacoes_5_estrelas DESC
