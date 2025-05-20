# ProjetoBancoDados2

## Integrantes

Nome: Gabriel Lovato Camilo de Campos - 22.123.004-8

Nome: Theo Zago Zimmermann - 22.123.035-2

## Descrição do Projeto

Este projeto tem como objetivo criar um sistema de música simples estilo spotify para gerenciar essas informações, como Artista, Usuário, Gênero, Álbum, Música, Playlist e Avaliação. O sistema permite o cadastro de dados em um banco de dados PostgreSQL, utilizando a linguagem Python com a biblioteca psycopg2. O projeto também inclui um menu interativo para facilitar a inserção de dados no banco de forma prática.

## Como Executar o Projeto

1.Criar o Banco de Dados

  Como Por Exemplo:
  
    CREATE DATABASE BancoSpotify;

  
2.Criar as tabelas relacionadas a uma universidade

  Depois de criar o banco de dados e conectar-se, deve se inserir as tabelas necessárias e executar o arquivo DDLTables.sql (conforme o GitHub)

3.Configurar o Ambiente que irá executar o código

  Após ter criado as tabelas necessárias, deve-se instalar a biblioteca: pip install psycopg2.

  Deve fazer a conexão com o Banco de Dados, conforme exemplo:

    host = "localhost"
    database = "BancoSpotify"
    user = "postgres"
    password = "sua_senha"
    port = 5432


# Diagrama Modelo Entidade Relacionamento(MER)

```mermaid
erDiagram

    Usuario ||--o{ Usuario_Playlist : possui
    Playlist ||--o{ Usuario_Playlist : é_compartilhada_com
    Playlist ||--o{ Playlist_Musica : contém
    Musica ||--o{ Playlist_Musica : está_em
    Musica ||--o{ Musica_Genero : possui
    Genero ||--o{ Musica_Genero : classifica
    Usuario ||--o{ Avaliacao : faz
    Musica ||--o{ Avaliacao : recebe
    Artista ||--o{ Album : cria
    Album ||--o{ Musica : inclui
    Artista ||--o{ Musica : interpreta

    Usuario {
        int id PK
        varchar nome
        varchar email
        date data_nascimento
    }

    Artista {
        int id PK
        varchar nome
        varchar pais
        varchar genero_musical_principal
    }

    Genero {
        int id PK
        varchar nome
    }

    Album {
        int id PK
        varchar titulo
        date data_lancamento
        int artista_id FK
    }

    Musica {
        int id PK
        varchar titulo
        varchar duracao
        int album_id FK
        int artista_id FK
    }

    Musica_Genero {
        int musica_id PK, FK
        int genero_id PK, FK
    }

    Playlist {
        int id PK
        varchar nome
        timestamp data_criacao
    }

    Usuario_Playlist {
        int usuario_id PK, FK
        int playlist_id PK, FK
    }

    Playlist_Musica {
        int playlist_id PK, FK
        int musica_id PK, FK
    }

    Avaliacao {
        int id PK
        int usuario_id FK
        int musica_id FK
        int nota
        text comentario
        timestamp data_avaliacao
    }

```

## Diagrama Modelo Relacional(MR)
![image](https://github.com/user-attachments/assets/94cf888e-8674-43df-a88e-85fec9bbe7bd)

