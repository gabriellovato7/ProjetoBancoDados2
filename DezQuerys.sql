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