import requests
import os

import os
import requests
from typing import Dict, Any, Optional

TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_API_KEY = os.getenv("TMDB_API_KEY")


class TMDbClient:
    """
    Client wrapper for The Movie Database (TMDb) API.

    Supports:
    - Search (text-based queries)
    - Discover (filtered queries)
    - Find (external ID lookup)
    """

    def __init__(self) -> None:
        if not TMDB_API_KEY:
            raise RuntimeError("TMDB_API_KEY is not set")

        self.session = requests.Session()
        self.session.params = {
            "api_key": TMDB_API_KEY,
        }

    # -------------------------
    # /search
    # -------------------------
    def search_movies(self, query: str, page: int = 1) -> Dict[str, Any]:
        """
        Search movies by text query.
        """
        return self._get(
            "/search/movie",
            params={
                "query": query,
                "page": page,
                "include_adult": False,
            },
        )

    # -------------------------
    # /discover
    # -------------------------
    def discover_movies(
        self,
        *,
        sort_by: str = "popularity.desc",
        min_vote_average: Optional[float] = None,
        primary_release_year: Optional[int] = None,
        page: int = 1,
    ) -> Dict[str, Any]:
        """
        Discover movies using filters.
        """
        params = {
            "sort_by": sort_by,
            "page": page,
        }

        if min_vote_average is not None:
            params["vote_average.gte"] = min_vote_average

        if primary_release_year is not None:
            params["primary_release_year"] = primary_release_year

        return self._get("/discover/movie", params=params)

    # -------------------------
    # /find
    # -------------------------
    def find_by_external_id(
        self,
        external_id: str,
        external_source: str = "imdb_id",
    ) -> Dict[str, Any]:
        """
        Find a movie, TV show, or person by an external ID.
        """
        return self._get(
            f"/find/{external_id}",
            params={"external_source": external_source},
        )

    # -------------------------
    # Internal helper
    # -------------------------
    def _get(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Internal GET request helper with error handling.
        """
        url = f"{TMDB_BASE_URL}{path}"
        response = self.session.get(url, params=params, timeout=10)

        if response.status_code != 200:
            raise RuntimeError(
                f"TMDb API error {response.status_code}: {response.text}"
            )

        return response.json()
