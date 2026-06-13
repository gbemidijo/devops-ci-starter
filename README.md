# DevOps CI Starter

A tiny, ready-to-run project for learning Continuous Integration with GitHub Actions.
It is deliberately small: four calculator functions and their tests. The point is the
pipeline, not the code.

## Follow along with the article

This repo is the companion to **"CI/CD Explained: Build Your First Automated Pipeline."**

### 1. Get your own copy
Click the green **Use this template** button at the top of this repo (or **Fork** it).
That gives you a copy under your own GitHub account that you can push to.

Then clone it to your machine:

```bash
git clone https://github.com/YOUR-USERNAME/devops-ci-starter.git
cd devops-ci-starter
```

### 2. Run the tests locally first
```bash
pip install -r requirements.txt
pytest
```

You should see `5 passed`. That confirms the project works before any automation.

### 3. The pipeline is already here
Look in `.github/workflows/ci.yml`. The moment you pushed to your own copy, GitHub
already ran it. Open the **Actions** tab on your repo to see the green check.

### 4. Break a test on purpose
Open `test_calculator.py`, change `assert add(2, 2) == 4` to `== 5`, then:

```bash
git add .
git commit -m "Break a test on purpose"
git push
```

Watch the Actions tab turn red, read the error, then change it back to `4` and push
again to watch it go green. That loop is the whole point of CI.

## Files
- `calculator.py` - the code under test
- `test_calculator.py` - the tests
- `requirements.txt` - dependencies (just pytest)
- `.github/workflows/ci.yml` - the CI pipeline
