# Awkward Polaroids

Copyright (c) 2017 [Finn Ellis](relsqui@chiliahedron.com).

This is a bot that generates polaroid photos of people and tweets them. Some examples (there are a bunch more in [polaroids/](polaroids)):

<img src="https://pbs.twimg.com/media/C_Wlzh-UMAEk4Ue.jpg" width=250 height=250> <img src="https://pbs.twimg.com/media/C_Vho9yU0AIXoLN.jpg" width=250 height=250> <img src="https://pbs.twimg.com/media/C_UhjtDUIAAx19D.jpg" height=250 width=250>

The grammar and photos are licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/), which means you can modify them and use them for whatever you want as long as you include attribution (linking to this repository is fine). The code is licensed under [MIT](LICENSE), which means you can modify it and use it for whatever you want, with or without attribution.

If you have ideas for additions, feel free to create an issue, send a pull request, or [email me](mailto:relsqui@chiliahedron.com).

## Setup and Usage

To generate the images, you'll need [Context Free](https://www.contextfreeart.org/downloads.html). If that's all you want to do, you can just install it and drop [polaroids.cfdg](polaroids.cfdg) into the editor (or follow the instructions to use it on the command line).

To run the bot, you'll need Tweepy, which you can get with `pip install tweepy`. Then clone this repository, and clone the Linux version of Context Free into the new directory:

```
git clone https://github.com/relsqui/awkward_polaroid.git
cd awkward_polaroid
git clone https://github.com/MtnViewJohn/context-free.git CF3
```

Once that's there, you can use `./makephotos.sh` to fill the polaroids/ directory with pictures. (It defaults to 999 at a time, which might take a minute; you can edit that file and make the maximum number smaller, or the starting number higher.)

Create a Twitter account for the bot, add a phone number to it, and [create an app](https://apps.twitter.com/) from that account. This will get you a consumer key and secret for OAUTH. Authenticate with the app to get your personal access token and secret. Add all those values to `example-secrets.py` and rename it to `secrets.py`.

After populating the polaroids directory and setting up your authentication secrets, tweeting a photo is as simple as running `./bot.py`.
