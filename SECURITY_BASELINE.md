# Website Security Baseline

## Repository and supply-chain controls implemented

- GitHub Actions use least-privilege workflow permissions.
- The Pages workflow uses the dedicated `github-pages` environment.
- Pages deployments use a single concurrency group and do not overlap.
- Third-party Pages Actions are pinned to full immutable commit SHAs.
- `actions/checkout` does not persist the repository token into the checked-out Git configuration during deployment.
- Dependabot checks GitHub Actions dependencies weekly.
- CODEOWNERS marks workflow and security configuration for owner review.
- `.gitignore` excludes common environment files, logs, temporary files, editor files, and build output.
- The website does not require application secrets.

## Website controls

- HTTPS/custom-domain deployment is provided by GitHub Pages.
- The site has no server-side application, database, authentication, session, or file-upload surface.
- External links opened in new tabs use opener isolation.
- Contact data is URL-encoded before the WhatsApp hand-off and is not posted to a site-owned backend.
- Users are warned not to submit sensitive clinical information through the contact flow.
- Security reporting is documented in `SECURITY.md` and `.well-known/security.txt`.

## Platform/account controls

The following controls are GitHub or DNS settings rather than repository files and should be enabled where supported:

- Branch protection/rulesets for `main`, including pull-request review and required status checks.
- Secret scanning and push protection.
- GitHub account two-factor authentication.
- Verified custom domain using GitHub's TXT-record verification.
- GitHub Pages HTTPS enforcement.
- Protected `github-pages` environment/deployment approval rules where appropriate.

## Verification

After deployment, HTTP response headers and TLS configuration should be checked against the live custom domain. GitHub Pages controls those response headers; repository files cannot reliably set `X-Content-Type-Options`, `Permissions-Policy`, `Cross-Origin-*`, or other response-header-only controls.
