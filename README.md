# Project Nexus – Movie Recommendation Backend (ProDev BE)

This project is a production-ready backend system for a movie recommendation application.  
It follows twelve-factor app principles, uses Docker for deployment, and integrates external
services for scalability and performance.

---

## Overview

The Movie Recommendation Backend provides RESTful APIs for retrieving trending movies,
managing user authentication, and allowing users to save their favorite movies.
The system emphasizes clean architecture, performance optimization, and clear API documentation.

---

## Features

- Fetch trending movies using the TMDb API
- JWT-based user authentication
- Save and retrieve user favorite movies
- Redis caching for high-performance API responses
- Swagger (OpenAPI) documentation for all endpoints

---

## Technologies Used

- Django & Django REST Framework
- PostgreSQL
- Redis
- TMDb API
- JWT Authentication
- Swagger (drf-yasg)
- Docker & Docker Compose
- Nginx (reverse proxy)

---

## System Architecture

- Django REST API handles business logic
- PostgreSQL stores persistent application data
- Redis caches frequently accessed movie data
- TMDb provides external movie information
- Nginx proxies requests to Gunicorn

---

## Running the Application (Docker – Recommended)

The application is fully containerized and can be run using Docker Compose.

### Prerequisites

- Docker
- Docker Compose
- TMDb API Key

### Start the Application

```bash
docker compose -f docker-compose-nexus.yaml up --build
```

### Querying using postman

```
http://localhost/api/movies/search/?q=Rambo
```

### Output below in JSON format:

```
{
    "page": 1,
    "results": [
        {
            "adult": false,
            "backdrop_path": "/wzfTG1obTazlGXiIcfRIviBZ1QU.jpg",
            "genre_ids": [
                28,
                53,
                10752
            ],
            "id": 7555,
            "original_language": "en",
            "original_title": "Rambo",
            "overview": "In Thailand, ex-Green Beret John James Rambo joins a group of mercenaries to venture into war-torn neighboring Myanmar to rescue a group of Christian aid workers who have been kidnapped by a ruthless local infantry unit.",
            "popularity": 7.455,
            "poster_path": "/3mInub5c8o00H7EJ1TrjAqOzIuc.jpg",
            "release_date": "2008-01-24",
            "title": "Rambo",
            "video": false,
            "vote_average": 6.69,
            "vote_count": 4166
        },
        {
            "adult": false,
            "backdrop_path": null,
            "genre_ids": [
                28
            ],
            "id": 1205021,
            "original_language": "hi",
            "original_title": "Rambo",
            "overview": "Upcoming Rambo remake starring Tiger Shroff",
            "popularity": 5.0054,
            "poster_path": "/9YtiecEbDSx4MEt2HUS2fKcJ9Dq.jpg",
            "release_date": "2025-01-01",
            "title": "Rambo",
            "video": false,
            "vote_average": 0.0,
            "vote_count": 0
        },
        {
            "adult": false,
            "backdrop_path": "/ilfH6RHpzfq8rMedMjr0BPoNDdw.jpg",
            "genre_ids": [
                35,
                53
            ],
            "id": 849210,
            "original_language": "kn",
            "original_title": "Rambo",
            "overview": "Car brokers Kitty and Premkumar come across a vehicle that contains a corpse. Soon, they learn that the body has a pen drive that holds information about a terrorist plot.",
            "popularity": 2.2974,
            "poster_path": "/gwP7l73XxxXffdFhrcFaiN38qmm.jpg",
            "release_date": "2012-09-07",
            "title": "Rambo",
            "video": false,
            "vote_average": 3.5,
            "vote_count": 2
        },
        {
            "adult": false,
            "backdrop_path": null,
            "genre_ids": [
                28
            ],
            "id": 1612499,
            "original_language": "ta",
            "original_title": "Rambo",
            "overview": "A ruthless education empire heir and a compassionate orphanage worker clash when a woman reveals the heir's hidden past, leading to a violent confrontation.",
            "popularity": 0.3198,
            "poster_path": "/j2N2B4Y4wDo1d9hh2uxAGV9S01v.jpg",
            "release_date": "2025-10-10",
            "title": "Rambo",
            "video": false,
            "vote_average": 0.0,
            "vote_count": 0
        },
        {
            "adult": false,
            "backdrop_path": "/zMIAkebGFDHvGep2vYvDM27qhxj.jpg",
            "genre_ids": [
                53,
                18,
                35
            ],
            "id": 1170841,
            "original_language": "ar",
            "original_title": "البحث عن منفذ لخروج السيد رامبو",
            "overview": "The story follows Hassan and his dog, Rambo, as they embark on a quest to save Rambo from Hassan's vengeful landlord, whom the dog attacked. Through his challenging journey across Cairo to find a safe haven for Rambo, Hassan confronts his deepest fears and rediscovers himself.",
            "popularity": 1.241,
            "poster_path": "/7XPZOfZcuaBawXON9kHDwrrCeJR.jpg",
            "release_date": "2025-01-01",
            "title": "Seeking Haven for Mr. Rambo",
            "video": false,
            "vote_average": 6.75,
            "vote_count": 10
        },
        {
            "adult": false,
            "backdrop_path": "/p2QCyCJEEmstjK1VGs9wF6T7W3L.jpg",
            "genre_ids": [
                99
            ],
            "id": 612866,
            "original_language": "ca",
            "original_title": "Darrere l'ombra de Natacha Rambova",
            "overview": "The adventurous life of Natacha Rambova (1897-1966), an American artist, born Winifred Kimball Shaughnessy, who reincarnated herself countless times: false Russian dancer, silent film actress, scenographer and costume designer, writer, spiritist, Egyptologist, indefatigable traveler, mysterious and curious; an amazing 20th century woman who created the myth of Rudolph Valentino.",
            "popularity": 0.3499,
            "poster_path": "/45AETc2BItaDLb1YCh0oQ8BsfKS.jpg",
            "release_date": "2019-07-06",
            "title": "Behind Natacha Rambova's Shadow",
            "video": false,
            "vote_average": 5.0,
            "vote_count": 1
        },
        {
            "adult": false,
            "backdrop_path": null,
            "genre_ids": [
                35,
                28
            ],
            "id": 699406,
            "original_language": "el",
            "original_title": "Ο Ράμπο ο κοντός και η τάπα!",
            "overview": "Rambo, on orders from Stathis the Short, a wealthy but illegal guy, undertakes to blow up a tourist hotel. He immediately begins training with the help of Sakis Tsanas or Tapa...",
            "popularity": 0.0546,
            "poster_path": "/zEyJZORGjPMx1yYO1p98BiHdGSR.jpg",
            "release_date": "1986-01-01",
            "title": "O Rambo, o Kontos kai i Tapa!",
            "video": false,
            "vote_average": 0.0,
            "vote_count": 0
        },
        {
            "adult": false,
            "backdrop_path": "/vDAjjvOOxOo6ESegvuIsOtTerph.jpg",
            "genre_ids": [
                28,
                18
            ],
            "id": 1433133,
            "original_language": "ta",
            "original_title": "ராம்போ",
            "overview": "Gowtham a ruthless heir to an education empire and Ram, a kind hearted orphanage caretaker, are raised with opposing beliefs. When Malar exposes Gowtham's dark secret, the two men face off in a brutal test of power and fists.",
            "popularity": 2.5794,
            "poster_path": "/qqlcaDSFv9bPJFLH4TV5iPpXiJ.jpg",
            "release_date": "2025-10-10",
            "title": "Rambo",
            "video": false,
            "vote_average": 0.0,
            "vote_count": 0
        },
        {
            "adult": false,
            "backdrop_path": null,
            "genre_ids": [
                18
            ],
            "id": 587120,
            "original_language": "fr",
            "original_title": "Arthur Rambo",
            "overview": "Alain is a little boy from the Reunion Island born on the wrong side of the tracks. To earn a few pennies, he recites Arthur Rimbaud’s poems to drivers stuck at the red light. One day, Alain is invited to Guillaume's birthday who lives uptown.",
            "popularity": 0.053,
            "poster_path": "/rIcGPxtDYspA8vMl5TzgNtj5jje.jpg",
            "release_date": "2018-01-01",
            "title": "Arthur Rambo",
            "video": false,
            "vote_average": 0.0,
            "vote_count": 0
        },
        {
            "adult": false,
            "backdrop_path": "/spYx9XQFODuqEVoPpvaJI1ksAVt.jpg",
            "genre_ids": [
                28,
                53,
                18
            ],
            "id": 522938,
            "original_language": "en",
            "original_title": "Rambo: Last Blood",
            "overview": "After fighting his demons for decades, John Rambo now lives in peace on his family ranch in Arizona, but his rest is interrupted when Gabriela, the granddaughter of his housekeeper María, disappears after crossing the border into Mexico to meet her biological father. Rambo, who has become a true father figure for Gabriela over the years, undertakes a desperate and dangerous journey to find her.",
            "popularity": 7.1125,
            "poster_path": "/kTQ3J8oTTKofAVLYnds2cHUz9KO.jpg",
            "release_date": "2019-09-18",
            "title": "Rambo: Last Blood",
            "video": false,
            "vote_average": 6.531,
            "vote_count": 4123
        },
        {
            "adult": false,
            "backdrop_path": "/Afkcvov0y7osi6NwubwpPL6pfrA.jpg",
            "genre_ids": [
                28,
                12,
                53,
                10752
            ],
            "id": 1370,
            "original_language": "en",
            "original_title": "Rambo III",
            "overview": "Combat has taken its toll on Rambo, but he's finally begun to find inner peace in a monastery. When Rambo's friend and mentor Col. Trautman asks for his help on a top secret mission to Afghanistan, Rambo declines but must reconsider when Trautman is captured.",
            "popularity": 5.1397,
            "poster_path": "/uycbt9iVlAnKkQIisqUWuO8hVcm.jpg",
            "release_date": "1988-05-24",
            "title": "Rambo III",
            "video": false,
            "vote_average": 6.199,
            "vote_count": 3394
        },
        {
            "adult": false,
            "backdrop_path": "/tYwkQigtc8afw0XeEogSSG0YcYQ.jpg",
            "genre_ids": [
                28,
                12,
                53,
                10752
            ],
            "id": 1369,
            "original_language": "en",
            "original_title": "Rambo: First Blood Part II",
            "overview": "John Rambo is released from prison by the government for a top-secret covert mission to the last place on Earth he'd want to return - the jungles of Vietnam.",
            "popularity": 8.4617,
            "poster_path": "/lIyUiHted0eWUceCx2ZHLnQGmgy.jpg",
            "release_date": "1985-05-21",
            "title": "Rambo: First Blood Part II",
            "video": false,
            "vote_average": 6.657,
            "vote_count": 4210
        },
        {
            "adult": false,
            "backdrop_path": null,
            "genre_ids": [
                28,
                10752,
                35
            ],
            "id": 349964,
            "original_language": "ko",
            "original_title": "영구와 땡칠이 3: 영구람보",
            "overview": "Bumbling simpleton Yeong-koo is back, this time he enlists in the military and joins the special forces to take on an enemy robot.",
            "popularity": 0.1025,
            "poster_path": "/mpjoqXS4AvXkHqxFpqpHIkIYLSR.jpg",
            "release_date": "1990-07-28",
            "title": "Yeong-Gu And Daeng-Chil 3 - Yeong-Gu Rambo",
            "video": false,
            "vote_average": 2.0,
            "vote_count": 1
        },
        {
            "adult": false,
            "backdrop_path": "/lCLajFMuNd8eQ6SoLFVpgY3mykU.jpg",
            "genre_ids": [
                28
            ],
            "id": 187110,
            "original_language": "ja",
            "original_title": "女ランボー",
            "overview": "Lady Ramboh finds her sister and her best friend on vacation, and the three of them spend the days having lots of fun. But the fun trip is ruined, when the girls are kidnapped and raped by the remaining traffickers. Lady Ramboh seeks revenge. She has a room full of grenade launchers to prove it.",
            "popularity": 1.5977,
            "poster_path": "/a2wxySOKgX5ZLUr4ZPFqLAfvhwh.jpg",
            "release_date": "1991-01-01",
            "title": "Lady Ramboh",
            "video": false,
            "vote_average": 4.0,
            "vote_count": 1
        },
        {
            "adult": false,
            "backdrop_path": "/3N2BU1hmILP3aye0U0pMahohIWv.jpg",
            "genre_ids": [
                35
            ],
            "id": 547428,
            "original_language": "ar",
            "original_title": "عبده يتحدى رامبو",
            "overview": "The play revolves around Abdo (Mohammad Najm), who works at Amani (Vivian) in a strange job, to prevent her from interviewing Shaukat (Mahmoud al-Qal'awi) her ex-husband who tries to exploit her and grab her money but does not know how to get away from him even though she knows well his bad intentions . (Abdu) agrees to a physical reward of half a million pounds to prevent her from making mistakes. Abdu tries to prevent her husband from stealing her money because of his strange job.",
            "popularity": 0.0688,
            "poster_path": "/mZ2xfZzbwA304WyT7dd9P6AuywD.jpg",
            "release_date": "1990-06-13",
            "title": "Abdo Challenges Rambo",
            "video": false,
            "vote_average": 7.0,
            "vote_count": 1
        },
        {
            "adult": false,
            "backdrop_path": null,
            "genre_ids": [],
            "id": 470204,
            "original_language": "en",
            "original_title": "Remo, Rambo, Reagan and Reds: The Eighties Action Movie Explosion",
            "overview": "This feature-length documentary from High Rise Productions takes a close look at some of the most popular action movies from the '80s and the different political overtones in them, as well as the very specific characterizations they promoted, their general attitude towards violence, the political climate in Hollywood, etc. - www.blu-ray.com",
            "popularity": 0.0723,
            "poster_path": "/lzwnK8LRDjx9NCsD2e7RkgDG2Zr.jpg",
            "release_date": "2014-07-07",
            "title": "Remo, Rambo, Reagan and Reds: The Eighties Action Movie Explosion",
            "video": false,
            "vote_average": 8.0,
            "vote_count": 1
        },
        {
            "adult": false,
            "backdrop_path": null,
            "genre_ids": [
                16
            ],
            "id": 758526,
            "original_language": "sh",
            "original_title": "Kako smo isekli Ramba—i okrenuli ga naopako",
            "overview": "A three-projector Super 8 film.",
            "popularity": 0.0261,
            "poster_path": "/gM1NQfuFj3SsIlxpDOF9ixFOkOZ.jpg",
            "release_date": "1988-01-01",
            "title": "How We Cut Up and Flipped Rambo",
            "video": false,
            "vote_average": 0.0,
            "vote_count": 0
        },
        {
            "adult": false,
            "backdrop_path": null,
            "genre_ids": [
                35
            ],
            "id": 1101663,
            "original_language": "my",
            "original_title": "ရမ်ဘိုလာပြီ",
            "overview": "",
            "popularity": 0.0143,
            "poster_path": "/sbdo2nKwAN3pvDZQpJN8RHccPdC.jpg",
            "release_date": "2022-12-30",
            "title": "Rambo",
            "video": false,
            "vote_average": 0.0,
            "vote_count": 0
        },
        {
            "adult": false,
            "backdrop_path": null,
            "genre_ids": [
                35,
                28
            ],
            "id": 278249,
            "original_language": "de",
            "original_title": "Pudelmützen Rambos",
            "overview": "Charly is a complete loser who forms a gang to rescue his sister from a vampire.",
            "popularity": 3.049,
            "poster_path": "/jZQCqnfeDv1pS6CLCf0KiqFOWaN.jpg",
            "release_date": "2004-01-02",
            "title": "Pudelmützen Rambos",
            "video": true,
            "vote_average": 2.0,
            "vote_count": 2
        },
        {
            "adult": false,
            "backdrop_path": null,
            "genre_ids": [
                28
            ],
            "id": 1267233,
            "original_language": "en",
            "original_title": "Rambo Raja Revolver Rani",
            "overview": "Raja and Rani realize that they have a mutual enemy who is responsible for hurting many people with his illegal activities. So they both get together and make a plan to get him out of the way.",
            "popularity": 0.4683,
            "poster_path": "/fY62NhkaH0DwPTeKjuXEngAEe7V.jpg",
            "release_date": "1996-03-01",
            "title": "Rambo Raja Revolver Rani",
            "video": false,
            "vote_average": 0.0,
            "vote_count": 0
        }
    ],
    "total_pages": 4,
    "total_results": 63
}
```
