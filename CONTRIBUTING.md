# Contributing

Awesome that you are reading this.

This GitHub follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

 * For questions, you can create an Issue
 * Code changes go via Pull Requests

## Submitting code

Submitted code should follow these quality guidelines:

 * All tests pass cleanly/silently
 * Code coverage at 100%
 * Coding style should follow the default style by `ruff`

These are all checked by GitHub Actions when submitting
a Pull Request. 

Emails with code will not be accepted.

## Submitting bugs

Awesome. These are your options:

 * Add an Issue, with the test that fails
 * Submit a Pull Request, where the test is added to the `tests` folder
 * Send @richelbilderbeek an email (@richelbilderbeek will make an Issue of it)

Pull Requests should follow the same guidelines as 'Submitting code'.

## Branching policy

 * The `master` branch should always build successfully
 * The `development` branch is where our developers merge their code
 * The feature branches (e.g. `richel`) are for features

## git usage

To get started working on `programming_formalisms_project_2023` do:

```
git clone https://github.com/programming-formalisms/programming_formalisms_project_2023
```

Development is done on a feature branch. 
To download and checkout the (for example) `richel` branch, 
first go into the `programming_formalisms_project_2023` folder (`cd programming_formalisms_project_2023`), then do:

```
git checkout richel
```

Then the workflow is the common `git` workflow:

```
git pull
git add .
git commit -m "Did something awesome"
git push
```
