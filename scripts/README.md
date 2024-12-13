## Purpose

The scripts folder contains modular code for running the primary analysis, preprocessing data, and evaluating results.

## Key Script(s)

1. **run_analysis.py**: The main script to execute the end-to-end analysis.
2. **analysis.py**: Contains functions for EDA, sentiment analysis, and correlation computation.

## CI/CD Integration

The project includes a CI/CD pipeline to ensure code reliability and maintainability:

- **GitHub Actions Workflow**:
  - Located in `.github/workflows/unittests.yml`.
  - Automatically runs unit tests on each push or pull request.
  - Ensures continuous integration by verifying that new code doesn’t break existing functionality.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/username/financial-news-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd financial-news-analysis
   ```
3. Run the main analysis script:
   ```bash
   python scripts/run_analysis.py
   ```

## Testing

Unit tests for key functions are located in the `tests` directory. To run tests, use:

```bash
pytest tests/
```
