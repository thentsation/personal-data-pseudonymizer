# CHANGELOG

<!-- version list -->

## v1.0.4 (2026-09-28)

### Bug Fixes

- **ci**: Open lockfile PRs with RELEASE_PAT so CI runs on them
  ([`3e3a8cd`](https://github.com/thentsation/personal-data-pseudonymizer/commit/3e3a8cd6f7b6b29ff00de46ad4c13eb51e045698))


## v1.0.3 (2026-09-28)

### Bug Fixes

- Use RELEASE_PAT so dependabot auto-merge can write to PRs
  ([`885b23c`](https://github.com/thentsation/personal-data-pseudonymizer/commit/885b23c349ff06f168fb8a508eb6b9b3c4870311))

### Chores

- **deps**: Bump ruff from 0.16.8 to 0.16.9 in /config
  ([#4](https://github.com/thentsation/personal-data-pseudonymizer/pull/4),
  [`a6abedf`](https://github.com/thentsation/personal-data-pseudonymizer/commit/a6abedf7b91d019b1ce7e2ddb71998e8f1781f96))


## v1.0.2 (2026-09-26)

### Bug Fixes

- Broaden Trivy's pip/_vendor skip-dirs to a recursive glob
  ([`f5b96a2`](https://github.com/thentsation/personal-data-pseudonymizer/commit/f5b96a2f4bb06780231ce6245a2109a56d97fbe4))


## v1.0.1 (2026-09-25)

### Bug Fixes

- Skip pip's vendored msgpack copy in the Trivy scan
  ([`62432bb`](https://github.com/thentsation/personal-data-pseudonymizer/commit/62432bb485f1db4772bbf1e7e003ee38a60c2b9d))

### Chores

- **deps**: Bump python from 3.12-slim to 3.14-slim in /docker
  ([#1](https://github.com/thentsation/personal-data-pseudonymizer/pull/1),
  [`09200a0`](https://github.com/thentsation/personal-data-pseudonymizer/commit/09200a0aa458ede5ec410f13ca8ca4d66dc5a8a6))

- **deps**: Bump ruff from 0.16.3 to 0.16.8 in /config
  ([#3](https://github.com/thentsation/personal-data-pseudonymizer/pull/3),
  [`0584fbf`](https://github.com/thentsation/personal-data-pseudonymizer/commit/0584fbf3c28ec137c15c2bbc035c904c9874de71))

- **deps**: Update spacy requirement in /config
  ([#2](https://github.com/thentsation/personal-data-pseudonymizer/pull/2),
  [`0772874`](https://github.com/thentsation/personal-data-pseudonymizer/commit/077287477644318659c639a9b93fb45fbd745570))
