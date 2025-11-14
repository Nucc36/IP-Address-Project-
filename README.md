# IP Address Project

Quadfecta's IP Address Project (Ibrahim, Nick, Tim and Dat) for showing basic public IP information.

This is a small Python CLI that calls [`ipapi.co`](https://ipapi.co/) and prints details about
your current public IP address (city, country, ISP, ASN, etc.).

## Requirements

- Python 3.8 or later
- `requests` (installed via `requirements.txt`)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the app

From the project root:

```bash
python ip_address_code_final.py
```

If the request succeeds you will see output similar to:

```text
=== IP Address Information ===
IP Address : 1.2.3.4
City      : Sydney
Region    : New South Wales
Country   : AU
ISP       : Example ISP
ASN       : AS12345
===========================
```

If the API rate limit is reached or there is a network problem, the script will print an
error message instead.

## Running the tests

We use `pytest` plus the built-in `unittest` framework.

First install dev dependencies (if needed):

```bash
pip install -r requirements.txt
pip install pytest
```

Then run:

```bash
pytest
```

All tests should pass before pushing changes.

## CI/CD

A GitHub Actions workflow in `.github/workflows/python-app.yml` runs `flake8` and `pytest`
on every push and pull request to the `main` branch. This helps keep the code clean and
ensures the tests pass before changes are merged.

## Typical feature-branch flow

```bash
# create your own branch (example: ibby)
git checkout -b ibby

# make changes
git add -A
git commit -m "feat: improve CLI output formatting"

# push your branch
git push -u origin ibby

# then open a Pull Request from ibby -> main on GitHub
```

### Connection issues
- Check your internet connection
- Verify ipapi.co API is accessible
- Check firewall settings

## Rate Limiting
The ipapi.co API has rate limits for free usage. If you hit the rate limit, you'll receive an error message. Wait a few minutes before trying again.

## Data Source
This application uses **ipapi.co** for IP geolocation data. For more information, visit:
https://ipapi.co/

## Privacy
This application:
- Does not store any search history
- Does not collect personal information
- Only queries public IP geolocation data
- Does not track users

## Support
For issues or questions:
1. Check the troubleshooting section above
2. Verify your internet connection
3. Check ipapi.co status page.
