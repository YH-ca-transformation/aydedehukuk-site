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

## 7. Ongoing change management workflow
Use the repository as the single source of truth for all future updates.

### 7.1 Recommended working method
1. Create a branch for each change set, for example:
   - feature/design-tweak
   - feature/maps-integration
   - content/hero-copy-update
2. Make edits locally in the relevant files.
3. Preview the changes locally before publishing.
4. Commit with a clear message.
5. Push the branch to GitHub.
6. Open a pull request and merge to main when ready.
7. GitHub Pages will deploy automatically after merge.

### 7.2 Where each type of change goes
- Small visual or cosmetic updates:
  - edit [styles.css](styles.css)
  - add or replace images under [assets/brand](assets/brand) or a future assets/images folder
- Text and content updates:
  - edit [index.html](index.html), [hakkimizda.html](hakkimizda.html), [hizmetler.html](hizmetler.html), or [iletisim.html](iletisim.html)
- Small interactivity or page behavior:
  - edit [script.js](script.js)
- Google Maps integration:
  - add the embed or map code in [iletisim.html](iletisim.html)

### 7.3 Safe deployment rule
- Do not make direct production updates on main unless the change is trivial and already tested locally.
- Keep main always deployable.
- Use pull requests for review even for small changes.

## 8. Google Maps integration plan
For this site, the healthiest approach is a lightweight embedded map.

### 8.1 Recommended option
- Use a simple Google Maps embed iframe in [iletisim.html](iletisim.html).
- This requires no API key, works well on GitHub Pages, and is easy to maintain.

### 8.2 When to use a more advanced map
If you later want features such as custom markers, interactive zoom, or directions, we can add a JavaScript-based Google Maps implementation.
- Keep the API key out of the public repository if possible.
- For a static site on GitHub Pages, a serverless proxy or backend would be the safer long-term approach.

## 9. Maintenance checklist for each update
Before publishing, verify:
- local preview looks correct
- links still work
- the page is responsive on mobile
- the deployment workflow finishes successfully on GitHub
- the custom domain still serves the latest version
