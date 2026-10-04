"""电影/剧集的本地 NFO-only 能力档案。"""

from movieclaw_api.services.library.profile import profile_for
from movieclaw_media.models import MediaKind


def test_movie_and_tv_local_profiles_keep_structure_without_scraping() -> None:
    movie = profile_for(MediaKind.MOVIE, "local")
    tv = profile_for(MediaKind.TV, "local")

    for profile, collection, jellyfin_type in (
        (movie, "movies", "Movie"),
        (tv, "tvshows", "Series"),
    ):
        assert profile.scraped is False
        assert profile.naming is True
        assert profile.write_nfo is False
        assert profile.subscribable is False
        assert profile.jellyfin_collection == collection
        assert profile.jellyfin_type == jellyfin_type
