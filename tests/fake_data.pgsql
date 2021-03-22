--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: clothes; Type: TABLE; Schema: public; Owner: leyi_psql
--

CREATE TABLE public.clothes (
    id integer NOT NULL,
    location integer,
    category character varying,
    description character varying
);


ALTER TABLE public.clothes OWNER TO leyi_psql;

--
-- Name: clothes_id_seq; Type: SEQUENCE; Schema: public; Owner: leyi_psql
--

CREATE SEQUENCE public.clothes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.clothes_id_seq OWNER TO leyi_psql;

--
-- Name: clothes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: leyi_psql
--

ALTER SEQUENCE public.clothes_id_seq OWNED BY public.clothes.id;


--
-- Name: location; Type: TABLE; Schema: public; Owner: leyi_psql
--

CREATE TABLE public.location (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.location OWNER TO leyi_psql;

--
-- Name: location_id_seq; Type: SEQUENCE; Schema: public; Owner: leyi_psql
--

CREATE SEQUENCE public.location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.location_id_seq OWNER TO leyi_psql;

--
-- Name: location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: leyi_psql
--

ALTER SEQUENCE public.location_id_seq OWNED BY public.location.id;


--
-- Name: clothes id; Type: DEFAULT; Schema: public; Owner: leyi_psql
--

ALTER TABLE ONLY public.clothes ALTER COLUMN id SET DEFAULT nextval('public.clothes_id_seq'::regclass);


--
-- Name: location id; Type: DEFAULT; Schema: public; Owner: leyi_psql
--

ALTER TABLE ONLY public.location ALTER COLUMN id SET DEFAULT nextval('public.location_id_seq'::regclass);


--
-- Data for Name: clothes; Type: TABLE DATA; Schema: public; Owner: leyi_psql
--

COPY public.clothes (id, location, category, description) FROM stdin;
1	1	dress	maxi red
2	1	shirt	blue
3	1	shirt	green
4	2	shirt	yellow
5	1	pants	short blue
6	2	pants	long khaki
7	3	dress	mini black
8	3	shirt	purple
\.


--
-- Data for Name: location; Type: TABLE DATA; Schema: public; Owner: leyi_psql
--

COPY public.location (id, name) FROM stdin;
1	closet
2	cabinet
3	attic
\.


--
-- Name: clothes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: leyi_psql
--

SELECT pg_catalog.setval('public.clothes_id_seq', 8, true);


--
-- Name: location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: leyi_psql
--

SELECT pg_catalog.setval('public.location_id_seq', 3, true);


--
-- Name: clothes clothes_pkey; Type: CONSTRAINT; Schema: public; Owner: leyi_psql
--

ALTER TABLE ONLY public.clothes
    ADD CONSTRAINT clothes_pkey PRIMARY KEY (id);


--
-- Name: location location_name_key; Type: CONSTRAINT; Schema: public; Owner: leyi_psql
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT location_name_key UNIQUE (name);


--
-- Name: location location_pkey; Type: CONSTRAINT; Schema: public; Owner: leyi_psql
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT location_pkey PRIMARY KEY (id);


--
-- Name: clothes clothes_location_fkey; Type: FK CONSTRAINT; Schema: public; Owner: leyi_psql
--

ALTER TABLE ONLY public.clothes
    ADD CONSTRAINT clothes_location_fkey FOREIGN KEY (location) REFERENCES public.location(id);


--
-- PostgreSQL database dump complete
--

