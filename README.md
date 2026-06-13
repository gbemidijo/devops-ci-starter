# DevOps CI Starter

A tiny, ready-to-run project for learning Continuous Integration with GitHub Actions.
It is deliberately small: five calculator functions and their tests. The point is the
pipeline, not the code.

This starter has the code and the tests, but **no pipeline yet**. Adding the pipeline is
the whole exercise. Follow the companion article and you will build it yourself in a few
minutes.

> Want to see the finished version? It lives on the [`solution`](../../tree/solution)
> branch, complete with a working `.github/workflows/ci.yml`.

## Follow along with the article

This repo is the companion to **"CI/CD Explained: Build Your First Automated Pipeline."**

### 1. Get your own copy
Click the green **Use this template** button at the top of this repo (or **Fork** it).
That gives you a copy under your own GitHub account that you can push to.

Then clone it to your machine (swap in your own username):

```bash
git clone https://github.com/YOUR-USERNAME/devops-ci-starter.git
cd devops-ci-starter
```

### 2. Run the tests locally first
```bash
pip install -r requirements.txt
pytest
```

You should see `6 passed`. That confirms the project works before you automate anything.

### 3. Add the pipeline
Following the article, create the file `.github/workflows/ci.yml`, commit it, and push.
The moment it lands, GitHub runs it. Open the **Actions** tab on your repo to watch the
green check appear.

### 4. Break a test on purpose
Open `test_calculator.py`, change `assert add(2, 2) == 4` to `== 5`, then:

```bash
git add test_calculator.py
git commit -m "Break a test on purpose"
git push
```

Watch the Actions tab turn red, read the error, then change it back to `4` and push
again to watch it go green. That loop is the whole point of CI.

## Files
- `calculator.py` - the code under test
- `test_calculator.py` - the tests
- `requirements.txt` - dependencies (just pytest)
- `.github/workflows/ci.yml` - the pipeline you will add (see the `solution` branch for a reference)
