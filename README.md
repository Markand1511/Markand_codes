# MovieVerse

Django movie discovery app with TMDB integration, favorites, and PostgreSQL.

## Tech Stack

- Django 6
- PostgreSQL
- TMDB API
- WhiteNoise + Gunicorn (production)
- Render (deployment)

## Local Setup

```powershell
cd "C:\Users\khushi\OneDrive\Desktop\the mark\movie"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
# .env me TMDB_API_KEY aur PostgreSQL password set karo
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## SQLite se PostgreSQL migrate

```powershell
python scripts/migrate_sqlite_data.py
```

## GitHub Push

```powershell
git init
git add .
git commit -m "Add MovieVerse Django app with PostgreSQL and Render deploy setup"
git branch -M main
git remote add origin https://github.com/markandthewebhub-spec/markand_codes.git
git push -u origin main
```

## Render Deploy

1. https://render.com pe login karo
2. **New → Blueprint**
3. Repo connect karo: `markandthewebhub-spec/markand_codes`
4. Environment variables:
   - `TMDB_API_KEY` = 71602f6f505d810a85854664f976afbb
   - `DEBUG` = `False`
5. Deploy complete hone ke baad Render Shell me:
   ```bash
   python manage.py createsuperuser
   ```

Site live ho jayegi at `https://<your-app>.onrender.com`

## Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret (Render auto-generates) |
| `DEBUG` | `False` in production |
| `TMDB_API_KEY` | TMDB API key |
| `DATABASE_URL` | Auto-set by Render PostgreSQL |
| `DB_NAME` | Local PostgreSQL database name |
| `DB_USER` | Local PostgreSQL user |
| `DB_PASSWORD` | Local PostgreSQL password |
| `USE_SQLITE` | `True` only for SQLite data export |

Built by Markand
