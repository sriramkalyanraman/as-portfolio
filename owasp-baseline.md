# OWASP baseline for this static site

This site is intentionally a static brochure/contact site. The relevant OWASP baseline is therefore focused on browser-side and deployment risks rather than server-side application risks.

## Applicable controls

- Security headers / browser security policy
- Input validation and length limits on contact fields
- Output encoding via URL encoding before constructing the WhatsApp enquiry URL
- No authentication or session management
- No database or server-side request handling
- No file upload functionality
- No dynamic HTML injection from visitor input
- External-link isolation with `noopener`
- Dependency/update monitoring for GitHub Actions
- Secure HTTPS delivery through GitHub Pages
- Domain/DNS takeover protection through GitHub custom-domain verification
- Security disclosure contact

## Not applicable to the current architecture

- SQL injection controls: no database
- Server-side command injection: no server-side command execution
- SSRF: no server-side URL fetching
- Server-side request forgery: no backend
- Authentication/authorization testing: no accounts
- Session fixation/hijacking: no application sessions
- File-upload malware scanning: no uploads

## Important limitation

OWASP controls cannot make a static site immune to compromised third-party services or compromised hosting/DNS accounts. Protect the GitHub, Namecheap/DNS, and email accounts with strong unique credentials and MFA/2FA.
