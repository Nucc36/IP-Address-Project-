
Tim, Ibrahim, Dat and Nick's IP Address Project

A CLI that prints your public IP information using `ipapi.co`.

To run locally:

```bash
python ip_address_code_final.py
```

To conduct tests:

```bash
pip install -r requirements.txt
pip install pytest
pytest -q
```

CI/CD

A GitHub Actions workflow runs flake8 and pytest on every push and pull request
for **any** branch, which supports feature-branch workflows and branch protection.

Feature-branch flow

```bash
git checkout -b feature/ci-tests
# make changes
git add -A
git commit -m "feat: improve tests and CI for Activity 3"
git push -u origin feature/ci-tests
# then open a Pull Request
```
