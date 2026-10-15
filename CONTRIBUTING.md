# Contributing

Short version: if you know a resource that's better than something listed, or
you spot a dead link, open a pull request. I'll actually read it.

## Suggesting a link

One link per PR keeps review fast. In the PR body, write one or two lines on:

1. What it is and who it's for.
2. Why it's better than what's already listed in that section (or why the
   section has a gap).

The README entry format is:

```markdown
- [Name](https://example.com) — One honest line on what it does.
```

"Honest" means: say what it's bad at too, if that matters. "Great docs, JS
only" beats "amazing revolutionary framework".

## What gets merged

- It's alive: the link works and the project is maintained, or stable enough
  that maintenance doesn't matter (a finished spec, for example).
- It solves a real problem bot developers have.
- No referral or affiliate links. No paywalled-only tools. No listicles that
  are just SEO.

## What gets rejected

- Your own project with no explanation of why it belongs. (Your project is
  welcome — just make the case like anyone else would.)
- "Ultimate" repos that are 500 copy-pasted commands with no structure.
- Anything I can't verify without signing up for something.

## Reporting a dead link

Open an issue with the link and what it returns now. If you know the new URL,
even better — put it in a PR instead.

## Running the link checker

```bash
python3 scripts/check_links.py
```

It walks README.md and CONTRIBUTING.md, hits every URL, and reports anything
that doesn't come back alive. Run it before submitting if you've touched links.
Takes a minute or so — be patient, it's polite to other people's servers.
