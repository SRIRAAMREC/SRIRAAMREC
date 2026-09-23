import os
import json
import requests

user = os.environ.get("GH_PROFILE_USER", "SRIRAAMREC")
token = os.environ.get("GITHUB_TOKEN")

if not token:
    raise RuntimeError("GITHUB_TOKEN is not available.")

query = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        weeks {
          contributionDays {
            date
            contributionLevel
          }
        }
      }
    }
  }
}
"""

response = requests.post(
    "https://api.github.com/graphql",
    json={
        "query": query,
        "variables": {"login": user}
    },
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "SRIRAAMREC-profile-art"
    },
    timeout=30
)

response.raise_for_status()

result = response.json()

if "errors" in result:
    raise RuntimeError(f"GitHub GraphQL error: {result['errors']}")

calendar = (
    result.get("data", {})
    .get("user", {})
    .get("contributionsCollection", {})
    .get("contributionCalendar", {})
)

weeks = calendar.get("weeks", [])

if not weeks:
    raise RuntimeError(f"No contribution calendar returned for {user}.")

level_map = {
    "NONE": 0,
    "FIRST_QUARTILE": 1,
    "SECOND_QUARTILE": 2,
    "THIRD_QUARTILE": 3,
    "FOURTH_QUARTILE": 4,
}

rows = []

for week in weeks:
    for day in week.get("contributionDays", []):
        rows.append({
            "date": day["date"],
            "level": level_map.get(day["contributionLevel"], 0)
        })

if not rows:
    raise RuntimeError(f"No contribution days returned for {user}.")

os.makedirs("data", exist_ok=True)

with open("data/contributions.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=2)

print(f"Saved {len(rows)} contribution cells for {user}.")
