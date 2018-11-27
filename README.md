# GoBack
Go back to the old times (of your project)

It can navigate you to the first page of commits of a project on GitHub.

---

## Installation
Install `goback`:

```bash
pip install goback
```

---

## Usage
```bash
goback LINK_OF_A_GITHUB_PROJECT

# you can specify the branch you want to check using -b argument
goback LINK_OF_A_GITHUB_PROJECT -b NAME_OF_THE_BRANCH
```
e.g.
```bash
goback https://github.com/vuejs/vue
```
It returns a **url** which navigates to the first page of commits of Vue.js.
> Note: by default, the url navigates to the first page of commits of the `master` branch.

We can "**goback**" to the first page of commits of `dev` branch:
```bash
goback https://github.com/vuejs/vue -b dev
```
