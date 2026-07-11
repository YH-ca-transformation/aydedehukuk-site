# Standalone GitHub Pages deployment plan

## 1. Repository scope
- This website will be maintained as its own GitHub repository.
- It will stay separate from Market Intelligence and PRI Check.
- The repository root is the current project folder.

## 2. Files already prepared
- index.html
- hakkimizda.html
- hizmetler.html
- iletisim.html
- styles.css
- script.js
- CNAME
- .github/workflows/deploy.yml
- assets/brand/*

## 3. GitHub repository setup
1. Create a new GitHub repository, for example:
   - aydedehukuk-site
2. Add the remote:
   - git remote add origin https://github.com/<username>/aydedehukuk-site.git
3. Push the branch:
   - git push -u origin main

## 4. GitHub Pages configuration
1. Open the repository on GitHub.
2. Go to Settings > Pages.
3. Choose Source: GitHub Actions.
4. Enter the custom domain: aydedehukuk.com

## 5. GoDaddy DNS requirements
Add these records in GoDaddy:
- A records:
  - 185.199.108.153
  - 185.199.109.153
  - 185.199.110.153
  - 185.199.111.153
- CNAME:
  - www -> <github-username>.github.io

## 6. Domain handling
- The site will use the custom domain aydedehukuk.com.
- The repository already contains the CNAME file for the apex domain.
- Once GoDaddy DNS is configured, GitHub Pages will verify and serve the site.
