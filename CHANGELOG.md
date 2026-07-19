# CHANGELOG

<!-- version list -->

## v0.4.1 (2026-07-19)

### Bug Fixes

- Forward message kwarg in send_robust
  ([#27](https://github.com/ivellios/django-unified-signals/pull/27),
  [`c6c0f08`](https://github.com/ivellios/django-unified-signals/commit/c6c0f0874426f2f1c5d6a9be397d6ca471bc8b34))

### Chores

- Sync uv.lock version
  ([`5d2f80d`](https://github.com/ivellios/django-unified-signals/commit/5d2f80d91e853a59efc24f21ba96bc272495c858))


## v0.4.0 (2026-07-19)

### Bug Fixes

- Move uv.lock sync out of psr build_command
  ([#26](https://github.com/ivellios/django-unified-signals/pull/26),
  [`3d9c6b9`](https://github.com/ivellios/django-unified-signals/commit/3d9c6b9594a1c08c2454f955f131cdab4cb7de1a))

- Skip CKV_GHA_7 for validated tag input
  ([#24](https://github.com/ivellios/django-unified-signals/pull/24),
  [`3793e06`](https://github.com/ivellios/django-unified-signals/commit/3793e06cc04f172eada663bd6f762995168a65d7))

- Sync uv.lock version on release
  ([#25](https://github.com/ivellios/django-unified-signals/pull/25),
  [`4498b2d`](https://github.com/ivellios/django-unified-signals/commit/4498b2d80df93f2a76d8116a1c3f1fd471735815))

### Continuous Integration

- Add PyPI publish workflow ([#25](https://github.com/ivellios/django-unified-signals/pull/25),
  [`4498b2d`](https://github.com/ivellios/django-unified-signals/commit/4498b2d80df93f2a76d8116a1c3f1fd471735815))

### Features

- Add TestPyPI publish workflow via OIDC trusted publishing
  ([#24](https://github.com/ivellios/django-unified-signals/pull/24),
  [`3793e06`](https://github.com/ivellios/django-unified-signals/commit/3793e06cc04f172eada663bd6f762995168a65d7))

- Allow selecting which release tag to publish to TestPyPI
  ([#24](https://github.com/ivellios/django-unified-signals/pull/24),
  [`3793e06`](https://github.com/ivellios/django-unified-signals/commit/3793e06cc04f172eada663bd6f762995168a65d7))


## v0.3.0 (2026-07-19)

### Bug Fixes

- **ci**: Use admin PAT for release push to bypass branch protection
  ([#21](https://github.com/ivellios/django-unified-signals/pull/21),
  [`3ba2b33`](https://github.com/ivellios/django-unified-signals/commit/3ba2b3390f869cac5fe053426be9ce4d41228d54))

- **release**: Allow staying on 0.x versions
  ([`15b8add`](https://github.com/ivellios/django-unified-signals/commit/15b8addff72448d1d55f670b946079d636c955e8))

- **release**: Keep breaking changes on minor bumps while pre-1.0
  ([`23f623c`](https://github.com/ivellios/django-unified-signals/commit/23f623c2224f0d85239f36e0e4ab8868df7f6e51))

- **security**: Bumps the uv group with 6 updates in the / directory:
  ([#20](https://github.com/ivellios/django-unified-signals/pull/20),
  [`a9b2860`](https://github.com/ivellios/django-unified-signals/commit/a9b286047719e3bd3d1de3f316a958f08190cbf8))

### Build System

- Migrate to uv/hatchling, ruff, and add automated release workflow
  ([#18](https://github.com/ivellios/django-unified-signals/pull/18),
  [`153cd60`](https://github.com/ivellios/django-unified-signals/commit/153cd60f01c9ae1290c2170f922a249dfa819d45))

### Breaking Changes

- Drop support for Python 3.9-3.10 and Django 4.0-5.1; minimum versions are now Python 3.11 and
  Django 5.2.


## v0.2.1 (2024-10-10)


## v0.2.0 (2024-10-07)

### Features

- **package**: Add support for using with Django@5
  ([`8e81a4e`](https://github.com/ivellios/django-unified-signals/commit/8e81a4eec03b4689bc65ad61a6b06a3beb7eae02))


## v0.1.1 (2023-09-20)


## v0.1.0 (2023-09-20)

- Initial Release
