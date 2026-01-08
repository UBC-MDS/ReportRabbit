# Contributing to ReportRabbit 🐇📊

Thank you for your interest in contributing to **ReportRabbit**!  
We welcome contributions of all kinds—bug reports, feature ideas, code, and documentation.  
Every contribution helps make ReportRabbit more reliable, expressive, and useful for the data science community.

This document outlines how to contribute effectively and respectfully.

## Collaboration Workflow

ReportRabbit follows a GitHub Flow–based collaboration model:

- All work is done on feature or fix branches created from `main`
- Each issue corresponds to a single task or function
- Issues are assigned to exactly one team member
- Pull requests must be reviewed by at least one other team member before merging
- No direct commits are made to `main`
- GitHub issues and project boards are used for all project-related communication

### Branch naming

Create a new branch from `main` for each piece of work. Use consistent prefixes:

- `feature/<short-description>` for new features
- `fix/<short-description>` for bug fixes
- `docs/<short-description>` for documentation-only changes
- `test/<short-description>` for tests
- `chore/<short-description>` for maintenance tasks

Examples:
- `feature/metrics-report`
- `fix/mape-zero-division`
- `docs/readme-usage`
- `test/plot-report-tests`
- `chore/ci-update`

## Ways to Contribute

### 🐞 Report Bugs
If you encounter a bug, please open an issue and include:

- Your operating system and version
- Python version
- ReportRabbit version
- A minimal, reproducible example
- Expected behavior vs. actual behavior
- Any relevant error messages or stack traces

Clear bug reports help us resolve issues faster.

### 🔧 Fix Bugs
Browse open GitHub issues labeled **`bug`** or **`help wanted`**.  
If you plan to work on an issue, please comment on it first to avoid duplication.

### ✨ Implement Features
We welcome feature contributions that align with ReportRabbit’s scope:
**post-model reporting, evaluation, and interpretability**.

When proposing a feature:
- Clearly describe the problem it solves
- Keep the scope focused and incremental
- Explain how it integrates with the existing API
- Consider backward compatibility

### 📝 Improve Documentation
Good documentation is as important as good code. Contributions may include:
- Docstring improvements
- README updates
- Usage examples
- Tutorials or explanatory guides
- Diagrams or visuals that clarify workflows

### 💬 Submit Feedback or Ideas
Feature ideas and design feedback are welcome.  
When submitting feedback:
- Be specific and constructive
- Provide context or examples where possible
- Keep proposals concise and actionable

## Development Setup

To set up **ReportRabbit** for local development:

1. **Clone the repository**
   ```console
   git clone git@github.com:UBC-MDS/ReportRabbit.git
   cd reportrabbit
   ```

3. Install `reportrabbit` using `poetry`:

    ```console
    $ poetry install
    ```

4. Use `git` (or similar) to create a branch for local development and make your changes:

    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

5. When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests.

6. Commit your changes and open a pull request.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python.

## Code of Conduct

Please note that the `reportrabbit` project is released with a
[Code of Conduct](https://github.com/UBC-MDS/reportrabbit/blob/main/CONDUCT.md). By contributing to this project you agree to abide by its terms.
