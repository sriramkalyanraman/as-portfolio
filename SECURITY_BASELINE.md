# Website Security Baseline

## Implemented

- HTTPS/custom-domain deployment through GitHub Pages
- No server-side application, database, authentication, or file-upload surface
- External links opened in new tabs use `rel="noopener"`
- Contact form uses client-side required fields and opens WhatsApp rather than posting to a site-owned backend
- Sensitive clinical information warning on the contact page
- Security contact and disclosure policy
- Dependabot monitoring for GitHub Actions dependencies
- Security-policy meta directives are intended for the static pages where supported by the browser

## Platform controls

GitHub Pages controls the TLS certificate and hosting response headers. Header-level controls should be verified against the live domain after deployment.

## Recommended account/DNS controls

- Verify the custom domain in the GitHub account settings using the GitHub-provided TXT record.
- Keep HTTPS enforcement enabled in GitHub Pages.
- Keep DNS limited to the required GitHub Pages records; remove unused redirects/parking records.
- Enable GitHub account two-factor authentication.
- Review repository Actions permissions periodically.
