import os
import requests
from typing import Dict, Any, Optional

TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_ACCESS_TOKEN = os.getenv("TMDB_API_KEY")  # Bearer token


class TMDbClient:
    """
    TMDb API client using Bearer token authentication.

    Supported operations:
    - search (text-based)
    - discover (filter-based)
    - movie details
    - movie videos
    """

    def __init__(self) -> None:
        if not TMDB_ACCESS_TOKEN:
            raise RuntimeError("TMDB_API_KEY (Bearer token) is not set")

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}",
                "Accept": "application/json",
            }
        )

    # -------------------------
    # /search/movie
    # -------------------------
    def search_movies(self, query: str, page: int = 1) -> Dict[str, Any]:
        return self._get(
            "/search/movie",
            params={
                "query": query,
                "page": page,
                "include_adult": False,
            },
        )

    # -------------------------
    # /discover/movie
    # -------------------------
    def discover_movies(
        self,
        *,
        sort_by: str = "popularity.desc",
        min_vote_average: Optional[float] = None,
        page: int = 1,
    ) -> Dict[str, Any]:
        params = {
            "sort_by": sort_by,
            "page": page,
        }

        if min_vote_average is not None:
            params["vote_average.gte"] = min_vote_average

        return self._get("/discover/movie", params=params)

    # -------------------------
    # /movie/{id}
    # -------------------------
    def get_movie_details(
        self,
        movie_id: int,
        append_videos: bool = False,
    ) -> Dict[str, Any]:
        params = {}
        if append_videos:
            params["append_to_response"] = "videos"

        return self._get(f"/movie/{movie_id}", params=params)

    # -------------------------
    # /movie/{id}/videos
    # -------------------------
    def get_movie_videos(self, movie_id: int) -> Dict[str, Any]:
        return self._get(f"/movie/{movie_id}/videos")

    # -------------------------
    # internal helper
    # -------------------------
    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{TMDB_BASE_URL}{path}"
        response = self.session.get(url, params=params, timeout=10)

        if response.status_code != 200:
            raise RuntimeError(
                f"TMDb API error {response.status_code}: {response.text}"
            )

        return response.json()
