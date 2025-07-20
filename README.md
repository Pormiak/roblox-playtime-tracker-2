# Roblox Playtime Tracker

A simple FastAPI server to track and store total playtime across multiple Roblox games.

## Usage

- Deploy this server (e.g., on Render.com).
- Use Roblox HttpService to POST playtime data to `/update`.
- Query total playtime from `/get/{user_id}` endpoint.
