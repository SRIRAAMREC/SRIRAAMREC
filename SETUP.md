# SRIRAAMREC GitHub profile

## Local build

In PowerShell, from this folder:

```powershell
Set-ExecutionPolicy -Scope Process Bypass; .\run.ps1
```

The build downloads the current GitHub avatar for `SRIRAAMREC`, generates the ASCII portrait and wordmark, fetches the public contribution calendar, renders the self-hosted heatmap, and opens the local preview.

## Publish

Create a **public** repository named exactly `SRIRAAMREC` under the `SRIRAAMREC` account. GitHub displays its `README.md` as the profile README when the repository name matches the username and the repository is public.

Copy the generated `README.md`, `assets/`, `scripts/`, `data/`, and `.github/` into that repository and push them to `main`.

The workflow in `.github/workflows/update-profile-art.yml` refreshes the contribution SVG daily.
