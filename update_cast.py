import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie.settings")
django.setup()

from movieapp.models import Movie, Cast
from movieapp.services.tmdb import search_movie, get_movie_details


movies = Movie.objects.all()

print(f"Total movies: {movies.count()}")

for movie in movies:

    # Skip if this movie already has proper cast members saved
    if movie.cast_members.exists():
        print(f"\n{movie.title} — already has cast members, skipping.")
        continue

    print(f"\nSearching: {movie.title}")

    results = search_movie(movie.title)

    if not results:
        print(f"  ❌ No TMDB match found")
        continue

    tmdb_id = results[0]["id"]
    data = get_movie_details(tmdb_id)

    if not data:
        print(f"  ⚠️ Could not fetch details")
        continue

    cast_data = data.get("credits", {}).get("cast", [])[:10]

    if not cast_data:
        print(f"  ⚠️ No cast data found on TMDB")
        continue

    for index, actor in enumerate(cast_data):
        Cast.objects.create(
            movie=movie,
            tmdb_person_id=actor.get("id"),
            name=actor.get("name", "Unknown"),
            character=actor.get("character", ""),
            photo_url=f"https://image.tmdb.org/t/p/w300{actor.get('profile_path')}" if actor.get("profile_path") else "",
            order=index,
        )

    print(f"  ✅ Cast saved ({len(cast_data)} members)")

print("\nDone!")