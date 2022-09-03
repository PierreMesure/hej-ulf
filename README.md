# Hej Ulf

For the 2022 campaign, Moderaterna is sending personalised videos. These videos usually contain a few references to the person's name as well as their city or country of residence (for Swedes living abroad). These videos are produced by the company [Seen.io](https://seen.io).

Most of these references are quite lame but the introduction is striking as the receiver is welcomed by Ulf Kristersson personally saluting. "Hej Pierre".

According to Martin Borgs, chief of communication at Moderaterna, Kristersson [personally recorded](https://www.expressen.se/tv/nyheter/ms-reklamdrag-raggar-roster-med-personliga-videohalsningar-/) "a couple of thousands" ("ett par tusen namn") of these 1-second long introduction.

All of these clips are publicly available on the Internet and can be fetched by their unique URL.

## What does this script do?

- It downloads the most common Swedish names from [SCB](https://www.scb.se/hitta-statistik/sverige-i-siffror/namnsok/), sorted by popularity.
- It iterates through these names to download the videos of the ones that were actually recorded.
- It creates an .m3u8 file gathering the links to these videos from their original server.

This .m3u8 can be read by a web browser. It will then play all the videos one by one.
