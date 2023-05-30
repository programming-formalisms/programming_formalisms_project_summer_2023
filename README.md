# python_pfproject_2023

The Python Programming Formalisms project of 2023.

See also [the R Programming Formalisms project of 2023](https://github.com/richelbilderbeek/r_pfproject_2023).

## Workflow

 * Always work in a project, create a Project if needed.
   The first Issue for a Project is to document what it needs to do.
 * Within a project, always work on one Issue: 
   assign yourself and move to 'In Progress' on the kanban board
 * Each problem start with a design that is reviewed:
   when an Issue is posted for review, move the Issue to 'Under review'
 * Each reviewed design is implemented using TDD, after which the code is reviewed:
   when an Issue is posted for review, move the Issue to 'Under review'

 * Branching model from [Vincent Driessen's post](https://nvie.com/posts/a-successful-git-branching-model/)
   * `master` always works
   * `develop` is where merging takes place. 
     Merging to `develop` is done by a Pull Request with a code review,
     that follows a Code of Conduct
   * Feature branches are where Issues are fixed

 * Use of TDD
 * Use of CI: tests, codecov, ruff
 * 100% code coverage
 * `ruff` style guide


## Guidelines

 * [Agile software development](https://en.wikipedia.org/wiki/Agile_software_development)
 * [Design by Contract](https://en.wikipedia.org/wiki/Design_by_contract)
 * [The C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-philosophy) (i.e. those that apply to code in general)
 * Classes follow [Design Patterns](https://en.wikipedia.org/wiki/Software_design_pattern)
 * [Don't Repeat Yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
 * [Rules of Thumb, Laws, Guidelines and Principles](https://en.wikipedia.org/wiki/List_of_software_development_philosophies#Rules_of_thumb,_laws,_guidelines_and_principles)
 * [SOLID principles](https://en.wikipedia.org/wiki/SOLID) (for OOP)
 * [Principle of Least Astonishment: POLA](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)
 * [You aren't gonna need it: YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)
 * [Fail Fast](https://en.wikipedia.org/wiki/Fail-fast)

## `assert` in Python

```
(base) richel@richel-N141CU:~$ python assert.py 
Traceback (most recent call last):
  File "/home/richel/assert.py", line 1, in <module>
    assert 1 == 2
AssertionError
(base) richel@richel-N141CU:~$ python -O assert.py 
(base) richel@richel-N141CU:~$ 
```
