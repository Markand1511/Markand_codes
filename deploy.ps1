# MovieVerse — one-click setup + GitHub push
# Run: powershell -ExecutionPolicy Bypass -File deploy.ps1

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "=== MovieVerse Deploy Script ===" -ForegroundColor Cyan

# Git setup
if (-not (Test-Path .git)) {
    git init
    Write-Host "Git initialized." -ForegroundColor Green
}

# Ensure .env not tracked
git rm --cached .env 2>$null

git add .
git status

$commitMsg = "Add MovieVerse Django app with PostgreSQL and Render deploy setup"
$status = git status --porcelain
if ($status) {
    git commit -m $commitMsg
    Write-Host "Committed." -ForegroundColor Green
} else {
    Write-Host "Nothing new to commit." -ForegroundColor Yellow
}

git branch -M main

git remote remove origin 2>$null
git remote add origin https://github.com/markandthewebhub-spec/markand_codes.git

Write-Host "Pushing to GitHub..." -ForegroundColor Cyan
git push -u origin main

Write-Host "Done! Ab Render.com pe Blueprint se deploy karo." -ForegroundColor Green
