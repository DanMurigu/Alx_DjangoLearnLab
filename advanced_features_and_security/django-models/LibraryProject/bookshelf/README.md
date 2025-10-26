# HTTPS Deployment Notes
- SSL/TLS configured via Nginx
- Certificates from Let's Encrypt stored at /etc/letsencrypt/live/
- Django SECURE_SSL_REDIRECT enabled
- HSTS headers enabled for all subdomains
