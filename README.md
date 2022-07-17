<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/rom1trt/crypto-news-bot">
    <img align=top src="twitterbot.png" alt="Logo" width="270" height="270">
    <img align=top src="decryptofr.png" alt="Logo" width="400" height="400">
  </a>

  <h3 align="center">Twitter Crypto News Bot</h3>

  <p align="center">
    An awesome bot that enables you to post and translate crypto-related news on your Twitter account.
    <br />
    <a href="https://github.com/rom1trt/crypto-news-bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/rom1trt/crypto-news-bot">View Demo</a>
    ·
    <a href="https://github.com/rom1trt/crypto-news-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/rom1trt/crypto-news-bot/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Being French, I was looking for crypto daily news and analytics on French Twitter accounts in my feed. 
However, except one or two news' sources, few accounts commented events on a daily basis as well as analyzed technical indicators.
This is why I had an idea about a bot that scrapes and retrieves diverse data not only from several twitter accounts, but also from [CryptoPanic](https://cryptopanic.com).
Aditionnally, the bot automatically translates the info in foreign languages using Deepl API.

Here's why:
* Your time should be focused on the most reliable and important news. A project that helps others being kept updated of this fast-paced crypto-world.
* You shouldn't be doing the same tasks over and over like (re)tweeting and translating news and analytics.

The bot is specifically tailored for my case (being French and chose my news' sources). I'll be adding more in the near future. 
You may also suggest changes by forking this repo and creating a pull request or opening an issue.

A list of commonly used resources that I found helpful.

### Built With

* [![Python](https://img.shields.io/badge/python-c2a90f?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![Twitter](https://img.shields.io/badge/twitter-blue?style=for-the-badge&logo=twitter&logoColor=white)](https://developer.twitter.com/en/docs)
* [![Deepl](https://img.shields.io/badge/deepl-darkblue?style=for-the-badge&logo=deepl&logoColor=white)](https://www.deepl.com/docs-api/)
* [![Youtube](https://img.shields.io/badge/youtube-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com)
* [![Docker](https://img.shields.io/badge/docker-00bfff?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com)


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation

1. Get a free API Key at [Deepl](https://www.deepl.com/)
2. Get a free API Key at [CryptoPanic](https://cryptopanic.com/)
3. Get a free API Key at [Twitter](https://developer.twitter.com/en/docs)
4. Clone the repository
   ```sh
   git clone https://github.com/rom1trt/crypto-news-bot.git
   ```
4. Install python packages (using pip)
   ```sh
   pip install tweepy
   pip install pandas
   ```
5. Enter the corresponding API in `config_example.py`
   ```sh
   CRYPTOPANIC_API_KEY = '...................................' 
   DEEPL_AUTH_KEY = '........................................' 
   TWITTER_API_KEY = '...................................' 
   TWITTER_API_PRIVATE_KEY = '.........................................' 
   TWITTER_ACCESS_TOKEN = '...................................................' 
   TWITTER_ACCESS_TOKEN_SECRET = '.............................................' 
   ```
 6. Rename the `config_example.py` to `config.py`
 7. Run/modify the `main.py` file or create a new script

### Docker

You can also build thee dockerfile and make the program run in the background or on a virtual machine.

```shell
docker build . (name_of_file)
```
```shell
docker run (name_of_image or image_id)
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
