# Awesome Bot Building

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Everything I'd hand to someone who asks "how do I build a Discord bot?"

I run a Discord bot called SYNCORE — all-in-one, 130+ commands, web dashboard,
the works. Every time I mention it somewhere, someone asks how they can build
one too. I got tired of typing the same links into DMs, so I wrote them all
down here.

This is the list I wish existed when I started: libraries, docs, hosting,
dashboards, testing, design, getting users, getting paid. Everything on it is
something I've used, read properly, or dug into before recommending. Links get
checked before every update (there's a script for that in `scripts/`).

One honest bias: this leans JavaScript and Python, because that's what I build
in. If your favourite Rust or Go library is missing, it's probably because I
haven't used it — suggest it and I'll take a look.

## Contents

- [Libraries & frameworks](#libraries--frameworks)
- [Docs & guides](#docs--guides)
- [Hosting & deployment](#hosting--deployment)
- [Dashboards](#dashboards)
- [Dev workflow & testing](#dev-workflow--testing)
- [Design & UX](#design--ux)
- [Getting users](#getting-users)
- [Monetisation](#monetisation)
- [Communities](#communities)
- [Didn't make the cut](#didnt-make-the-cut)
- [Contributing](#contributing)
- [License](#license)

## Libraries & frameworks

Pick by language, not by hype. Every one of these is maintained and documented.

- [discord.js](https://discord.js.org) — The big one for JavaScript/TypeScript.
  Most tutorials, most Stack Overflow answers, most problems already solved by
  someone else. Default choice if you're unsure.
- [discord.py](https://github.com/Rapptz/discord.py) — The Python equivalent.
  Went through a rough patch a few years back, came back strong with v2. Solid.
- [nextcord](https://github.com/nextcord/nextcord) — discord.py fork from when
  discord.py went quiet. Kept innovating on its own since.
- [disnake](https://github.com/DisnakeDev/disnake) — Another discord.py fork,
  also still going. Between this and nextcord, read both docs and pick the one
  you enjoy reading.
- [Hikari](https://github.com/hikari-py/hikari) — Newer Python library, built
  around type hints and slash commands from day one. Cleaner if you like modern
  Python.
- [discordgo](https://github.com/bwmarrin/discordgo) — Go. No magic, just the
  API. Good if you already write Go.
- [JDA](https://github.com/discord-jda/JDA) — Java. The old reliable of the
  Java world.
- [Javacord](https://github.com/Javacord/Javacord) — Java alternative with a
  friendlier API than JDA, in my opinion.
- [serenity](https://github.com/serenity-rs/serenity) — Rust. Fast and safe,
  and the docs assume you know Rust.
- [Eris](https://github.com/abalabahaha/eris) — JavaScript, lighter than
  discord.js. Fine for small bots; you'll outgrow it if the bot gets big.

## Docs & guides

- [Discord Developer Docs](https://discord.com/developers/docs) — The actual
  API reference. Bookmark it, you'll live here.
- [Developer Portal](https://discord.com/developers/applications) — Where your
  bot is born: create the application, grab the token, enable intents.
- [discord.js Guide](https://discordjs.guide) — The best-written bot tutorial
  on the internet, in my opinion. The general concepts transfer to other
  languages too.
- [discord.py docs](https://discordpy.readthedocs.io) — Thorough reference,
  and the examples are actually runnable, which is rarer than it should be.

## Hosting & deployment

Your bot needs to be online when you're not.

- [Railway](https://railway.app) — Easiest deploy I've tried: connect GitHub,
  done. Free tier is limited but fine for a small bot.
- [Render](https://render.com) — Similar idea. Note the free tier sleeps when
  idle — bad for bots unless you pay or accept the naps.
- [Fly.io](https://fly.io) — Generous free tier, slightly more setup. Good
  middle ground.
- [Hetzner](https://www.hetzner.com) — Cheap VPS for when you outgrow free
  tiers. A few euros a month gets you a lot of bot.
- [FreezeHost](https://panel.freezehost.pro) — Free Pterodactyl-based hosting.
  I run my own bot on their free tier. It works for small bots — just don't
  expect miracles.
- Your own hardware — An old laptop or Raspberry Pi on your home network.
  Free, and you learn Linux properly along the way.
- [PM2](https://pm2.keymetrics.io) — Keeps a Node bot alive and restarts it
  when it crashes. Two commands to learn.
- [Docker](https://www.docker.com) — For when "works on my machine" stops
  being funny.

## Dashboards

- Build it yourself with [Next.js](https://nextjs.org) + Discord OAuth2. Every
  serious bot ends up here eventually, so you might as well plan for it.
- [Discord OAuth2 docs](https://discord.com/developers/docs/topics/oauth2) —
  The flow is: login with Discord, list their guilds, manage settings. The docs
  explain it well.
- Honest gap: I looked for a dashboard starter template I'd actually recommend
  and didn't find one I'd put my name on. If you know a good one, send a PR.

## Dev workflow & testing

- [ngrok](https://ngrok.com) — Exposes localhost so you can test webhooks and
  OAuth callbacks without deploying anything.
- [GitHub Actions](https://github.com/features/actions) — Free CI. Run tests
  and lint on every push; future you says thanks.
- [pytest](https://pytest.org) — If your bot is Python, test the logic, not
  Discord. (The link-checker script in this repo does exactly that.)
- Slash command deploy scripts — Every major library ships one. Run it in CI
  so your registered commands never drift from your code.

## Design & UX

Bots are UI too. The pretty ones all do this stuff.

- [Message components](https://discord.com/developers/docs/interactions/message-components) —
  Buttons, selects, modals. This is where bots stop feeling like 2015 IRC scripts.
- [node-canvas](https://github.com/Automattic/node-canvas) — Draw rank cards,
  welcome banners and memes in Node. Powers half the good-looking bots you've seen.
- [skia-canvas](https://github.com/samizdatco/skia-canvas) — Newer, faster
  alternative to node-canvas. Worth a look for new projects.
- [Pillow](https://pillow.readthedocs.io) — The Python equivalent for image
  generation.
- Pick a colour palette and stick to it — Not a link, just the cheapest way to
  look professional. Mine's red on near-black.

## Getting users

- [top.gg](https://top.gg) — The biggest bot list. Voting rewards give people
  a reason to come back daily.
- [discord.bots.gg](https://discord.bots.gg) — Smaller alternative, less noise.

## Monetisation

- [Patreon](https://www.patreon.com) — The classic: supporters pay monthly, you
  give them premium features.
- [Ko-fi](https://ko-fi.com) — One-off tips without the platform-cut drama.
- Discord's own monetisation — Premium app subscriptions are built into Discord
  now. Read the current terms before you build a business on it.

## Communities

Ask questions here, not in my DMs.

- [Discord Developers](https://discord.gg/discord-developers) — The official
  server.
- [discord.js](https://discord.gg/djs) — Fastest help for JavaScript bots.
- [Python Discord](https://pythondiscord.com) ([server](https://discord.gg/python)) —
  Genuinely welcoming, great for Python questions of any kind.
- [r/Discord_Bots](https://www.reddit.com/r/Discord_Bots/) — Good for "is this
  allowed?" and show-and-tell.
- [Stack Overflow](https://stackoverflow.com/questions/tagged/discord.js) —
  The `discord.js` and `discord.py` tags are active. Search before asking.

## Didn't make the cut

Things I looked at and left out, and why.

- Old discord.py v1 tutorials — Slash commands changed everything; v1 guides
  teach you the past.
- "Ultimate 500-command bot" GitHub repos — Copy-paste codebases with no
  structure. You'll learn nothing and inherit someone else's bugs.
- Replit — Used to be the default free answer, but the free tier kept shifting
  under people's feet. Check current pricing before building on it.

## Contributing

Found a dead link or something better than what's here? PRs welcome. Read
[CONTRIBUTING.md](CONTRIBUTING.md) first — it's short.

Last link check: 2026-10-15. Every link above returned HTTP 200 that day.

## License

MIT — see [LICENSE](LICENSE). Do whatever you want with the list, just keep
the copyright line.

---

Built and maintained by [Krrish](https://github.com/codewithkrrish). I make
Discord bots and the tools around them.
