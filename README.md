## Intro
- git clone from https://github.com/xtekky/gpt4free
- Add a simple gui for conversation!
![img.png](result_readme%2Fimg.png)

## Setup
#### 1st method : Run in local
```commandline
sh entrypoint.sh
```

#### 2nd method : Docker
```commandline
1. docker build -t gpt4free_simple_gui .
2. docker run -p 1336:1336 -p 1337:1337 --name gpt4free_simple_gui gpt4free_simple_gui
```