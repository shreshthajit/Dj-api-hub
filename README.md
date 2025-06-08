# Dj-api-hub

## Where the CSRF Token Comes From:
```
Django’s Middleware:

1. CSRF protection is handled by Django’s built-in middleware: django.middleware.csrf.CsrfViewMiddleware

2. This middleware ensures that every POST request contains a valid CSRF token.
```

## How It's Created:
```
1. When a user visits a page with a form (using a GET request), Django automatically generates a CSRF token.

2. It stores the token in the user’s session (or as a cookie, depending on configuration).

3. The token is made available in the template context.
```
