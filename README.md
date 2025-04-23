# KeywordReplaceMiddleware: A middleware for EFB

## Notice

**Middleware ID**: `jiz4oh.keyword_replace`

**KeywordReplaceMiddleware** is a middleware of EFB replace text by keywords.

## How it works

replace text by keywords both sent by master and slaves

## Dependense
* Python >= 3.6
* EFB >= 2.0.0

## Install and configuration

### Install

```
pip install git+https://github.com/jiz4oh/efb-keyword-replace.git
```

### Enable

Register to EFB
Following [this document](https://ehforwarderbot.readthedocs.io/en/latest/getting-started.html) to edit the config file. The config file by default is `$HOME/.ehforwarderbot/profiles/default`. It should look like:

```yaml
master_channel: foo.demo_master
slave_channels:
- foo.demo_slave
- bar.dummy
middlewares:
- foo.other_middlewares
- jiz4oh.keyword_replace
```

You only need to add the last line to your config file.

### Configure the middleware

The config file by default is `$HOME/.ehforwarderbot/profiles/default/jiz4oh.keyword_replace/config.yaml`.

```yaml
keywords:
  关键字1: 回复词1
  关键字2: 回复词2
  # below is how I use it
  https://x.com: https://fxtwitter.com
  https://twitter.com: https://fxtwitter.com
```

### Restart EFB.

