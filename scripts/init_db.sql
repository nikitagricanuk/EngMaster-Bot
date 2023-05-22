/*
 * A1
 */

CREATE TABLE IF NOT EXISTS words_A1_nouns (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_A1_verbs (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_A1_phrasal_verbs (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_A1_adjectives (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

/*
 * A2
 */

CREATE TABLE IF NOT EXISTS words_A2_nouns (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_A2_verbs (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_A2_phrasal_verbs (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_A2_adjectives (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

/*
 * B1
 */

 CREATE TABLE IF NOT EXISTS words_B1_nouns (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_B1_verbs (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                   definition TEXT);

CREATE TABLE IF NOT EXISTS words_B1_phrasal_verbs (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_B1_adjectives (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

/*
 * B2
 */

  CREATE TABLE IF NOT EXISTS words_B2_nouns (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_B2_verbs (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_B2_phrasal_verbs (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_B2_adjectives (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

/*
 * C1
 */

 CREATE TABLE IF NOT EXISTS words_C1_nouns (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_C1_verbs (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_C1_phrasal_verbs (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_C1_adjectives (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

/*
 * C2
 */

 CREATE TABLE IF NOT EXISTS words_C2_nouns (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_C2_verbs (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_C2_phrasal_verbs (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);

CREATE TABLE IF NOT EXISTS words_C2_adjectives (
                    id serial PRIMARY KEY,
                    word VARCHAR(64) UNIQUE NOT NULL,
                    transcription VARCHAR(64),
                    translation VARCHAR(64) NOT NULL,
                    definition TEXT);
                    