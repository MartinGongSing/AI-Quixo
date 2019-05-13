# AI Quixo

Quixo is a boardgame created by Gigamic
* [Quixo](https://www.gigamic.com/game/quixo) - the website of the creators of the game

We have created an AI capable of playing without making any bad moves, in python

## Our strategy

We noticed that the more cubes bearing our symbol we have, the higher the chances of winning are. So our first strategy is to take all the neutral cubes and turn them (litteraly) on our side. Once all the border cubes are taken, we only play with ours, untill a new neutral block appears. 
\\ (For now the 'intelligence' is the [Smart_Random.py](https://github.com/MartinGongSing/AI-Quixo/blob/master/ai/Smart_Random.py) file, but will soon be [Super_Smart.py](https://github.com/MartinGongSing/AI-Quixo/blob/master/ai/Super_smart.py)) \\

## Libraries

We have used the followings libraries : 

* cherrypy              
* sys
* random 

```
example for random : 
cube = random.choice(rdmcube)
```


## Authors

* **Yannick Elens** - 16046 - [AleckSinenny](https://github.com/AleckSinenny)
* **Martin Sing** - 16116 - [MartinGongSing](https://github.com/MartinGongSing)



## License

![My idea](https://images.says.com/uploads/story_source/source_image/475645/ea89.jpg)



##### Image source
[1](https://www.google.com/search?q=copyright&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjfl6C5kZjiAhVM_qQKHURCBiYQ_AUIDigB&biw=1536&bih=722#imgrc=FxpAoPlQk148tM:)
