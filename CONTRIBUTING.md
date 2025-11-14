## Branch Naming
```
feature/<feature-name>
bugfix/<description>
docs/<update>
```

## Commit Messages
Follow conventional commits:
```
feat: added new output formatting
fix: resolved API handling bug
docs: updated README
test: added unit test
ci: updated workflow
```

## Running Tests
Before pushing:
```bash
pytest -q
flake8 .
```

## Pull Request Process
1. Ensure tests pass  
2. Ensure linting passes  
3. Add a clear description  
4. Request review  
5. CI must pass before merge  
