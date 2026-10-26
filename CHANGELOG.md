# CHANGELOG

<!-- version list -->

## v1.0.5 (2026-10-26)

### Bug Fixes

- **deps**: Upgrade lockfile and use --upgrade in lockfile workflow
  ([#18](https://github.com/thentsation/personal-data-pseudonymizer/pull/18),
  [`5dc3b3b`](https://github.com/thentsation/personal-data-pseudonymizer/commit/5dc3b3bcd1dea4dbbb667db290dde78882987f52))

- **deps**: Use --upgrade when regenerating the lockfile
  ([#18](https://github.com/thentsation/personal-data-pseudonymizer/pull/18),
  [`5dc3b3b`](https://github.com/thentsation/personal-data-pseudonymizer/commit/5dc3b3bcd1dea4dbbb667db290dde78882987f52))

### Chores

- **ci**: Bump astral-sh/setup-uv from 10.2.0 to 10.3.2
  ([#17](https://github.com/thentsation/personal-data-pseudonymizer/pull/17),
  [`d0cda18`](https://github.com/thentsation/personal-data-pseudonymizer/commit/d0cda18b583b98f0ed8e949930d2f445dbd09dd8))

- **deps**: Bump ruff from 0.16.10 to 0.17.0 in /config
  ([#13](https://github.com/thentsation/personal-data-pseudonymizer/pull/13),
  [`f42284f`](https://github.com/thentsation/personal-data-pseudonymizer/commit/f42284ffa2967e2ac28b45da52f17c51e85638ae))

- **deps**: Bump ruff from 0.17.0 to 0.17.1 in /config
  ([#15](https://github.com/thentsation/personal-data-pseudonymizer/pull/15),
  [`49251a6`](https://github.com/thentsation/personal-data-pseudonymizer/commit/49251a67ddac1228dc37a7754b41a96b1031c337))

- **deps**: Bump ruff from 0.17.1 to 0.17.2 in /config
  ([#16](https://github.com/thentsation/personal-data-pseudonymizer/pull/16),
  [`1f450a2`](https://github.com/thentsation/personal-data-pseudonymizer/commit/1f450a2ba066881482ec67fce69a8b4499fa02bc))

- **deps**: Refresh pip-compile outputs
  ([#10](https://github.com/thentsation/personal-data-pseudonymizer/pull/10),
  [`bdc34cc`](https://github.com/thentsation/personal-data-pseudonymizer/commit/bdc34cc66c00aaa4c511466e47029c096ba18225))

- **deps**: Update dependency mypy to v2.4.0
  ([#8](https://github.com/thentsation/personal-data-pseudonymizer/pull/8),
  [`565fa7d`](https://github.com/thentsation/personal-data-pseudonymizer/commit/565fa7d2e83abd78145ad13e21378503b6a80d4f))

- **deps**: Update dependency ruff to v0.16.10
  ([#7](https://github.com/thentsation/personal-data-pseudonymizer/pull/7),
  [`70030a1`](https://github.com/thentsation/personal-data-pseudonymizer/commit/70030a1bf1b458a08bc1cdf17fd8e36e69d5085c))

- **deps**: Update lockfile
  ([#18](https://github.com/thentsation/personal-data-pseudonymizer/pull/18),
  [`5dc3b3b`](https://github.com/thentsation/personal-data-pseudonymizer/commit/5dc3b3bcd1dea4dbbb667db290dde78882987f52))

### Continuous Integration

- Pipeline da Shared Library da plataforma e Renovate
  ([#6](https://github.com/thentsation/personal-data-pseudonymizer/pull/6),
  [`7117f34`](https://github.com/thentsation/personal-data-pseudonymizer/commit/7117f348db5070bf7a52b9f989fa722836db707d))

- Remove workflow notify-portfolio (token sem acesso; o portfolio atualiza pelo cron diário)
  ([#12](https://github.com/thentsation/personal-data-pseudonymizer/pull/12),
  [`4517b82`](https://github.com/thentsation/personal-data-pseudonymizer/commit/4517b82ee6e003ec840665ef95aec21d83d41192))


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
