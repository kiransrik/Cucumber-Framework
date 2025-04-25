# Cucumber-Framework
# My-Framework
### 🧪 Test Automation Framework using **Cucumber** ,**Playwright** && **Python**
## 📦 1. Setup Instructions

### ✅ Prerequisites:
- Node.js (v16+ recommended)
- playwright install
- Git

## 2. Running Tests Locally

behave

### View Test Results:
- Screenshots are saved in the `screenshots/` folder.

## 3. CI/CD Integration (GitHub Actions)

A GitHub Actions pipeline (`playwright-ci.yml`) is included. It runs tests on every push and PR to `main`.

### CI/CD Workflow Steps:
1. Clone repository/Checkout code
2. Run tests
3. Upload test results as artifacts

To trigger the pipeline, push changes to the `main` branch or create a pull request.
