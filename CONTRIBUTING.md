# Contributing

Thanks for contributing to UFC Vibes Lab.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Good contributions

Useful changes include:

- new interpretable fighter metrics
- better UFCStats parsing resilience
- improved visualizations
- stronger tests
- weight-class or era normalization
- documentation and reproducibility improvements

## Before opening a PR

- [ ] Run the full test suite
- [ ] Keep funny metrics interpretable
- [ ] Avoid hard-coded fighter rankings
- [ ] Do not add betting claims
- [ ] Document new assumptions
- [ ] Keep scraped data out of git unless intentionally sampled for tests

## Style

The project should stay technically serious and slightly ridiculous.
