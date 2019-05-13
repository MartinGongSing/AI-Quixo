# AI Quixo

## Introduction 

Quixo is a boardgame created by Gigamic
* [Quixo](https://www.gigamic.com/game/quixo) - the website of the creators of the game

We have created an AI capable of playing without making any bad moves, in python (UTF-8 encoding)

## How to launch the game

* First thing you must do is clone or download the entire repositiry [AI-Quixo](https://github.com/MartinGongSing/AI-Quixo)
* Then launch the server : [server.py](https://github.com/MartinGongSing/AI-Quixo/blob/master/server.py). Be sure the game you want to play is named 'current.py' [In this repository](https://github.com/MartinGongSing/AI-Quixo/tree/master/public/games) (in this case, it is Quixo)
* Now you can launch your AI, based on the [matches.py](https://github.com/MartinGongSing/AI-Quixo/blob/master/ai/matches.py) file. (You need to launch 2 entities to play)
* If you want to play yourself, launch the [Quixo.1.py](https://github.com/MartinGongSing/AI-Quixo/blob/master/input_game/Quixo.1.py) in the [input_game](https://github.com/MartinGongSing/AI-Quixo/tree/master/input_game) repository (special thanks to [Thibaut Maringer ©titimar16](https://github.com/titimar16)) 
* None of the above would be possible without the original files : [ECAM Brussels - AIGameRunner](https://github.com/ECAM-Brussels/AIGameRunner)

## Our strategy

We noticed that the more cubes bearing our symbol we have, the higher the chances of winning are. So our first strategy is to take all the neutral cubes and turn them (litteraly) on our side. Once all the neutral border cubes are taken, we only play with ours, untill a new neutral block appears. 

(For now the 'intelligence' is the [Smart_Random.py](https://github.com/MartinGongSing/AI-Quixo/blob/master/ai/Smart_Random.py) file, but will soon be [Super_Smart.py](https://github.com/MartinGongSing/AI-Quixo/blob/master/ai/Super_smart.py), which strategy should be : "When four of our cubes are next to each other, we will play the fifth if possible")

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

![CopyRights](https://thumbs.dreamstime.com/t/campos-comunes-creativos-por-el-nd-del-nc-13329631.jpg)
Ce(tte) oeuvre est mise à disposition selon les termes de la Licence Creative Commons Attribution – Pas d’Utilisation Commerciale – Pas de Modification 4.0 International.



##### Image source
[1](https://www.google.com/search?q=copyright&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjfl6C5kZjiAhVM_qQKHURCBiYQ_AUIDigB&biw=1536&bih=722#imgrc=FxpAoPlQk148tM:)
[2](https://www.google.com/search?q=(cc)&tbm=isch&tbs=rimg:CeVgBf1AC6JCIji6N647rv--1G9SgXdVE3e_1DrXERXBlSIH5C9ZBHmZY7rYOGSdgmLPAtXiEVjPT96wxO3EMYsrYeSoSCbo3rjuu_177UEUws8Zt8rN2kKhIJb1KBd1UTd78RAKZvuiqM07kqEgkOtcRFcGVIgRFccxMpNjd8_1CoSCfkL1kEeZljuEaSJKz9v_1UTBKhIJtg4ZJ2CYs8ARkOLPliYxmZUqEgm1eIRWM9P3rBFaFBqwkZ5d2CoSCTE7cQxiyth5EVxXr6R2YVBv&tbo=u&sa=X&ved=2ahUKEwjYwrPa2ZjiAhVOaVAKHf5nCQoQ9C96BAgBEBs&biw=1536&bih=722&dpr=1.25#imgrc=b1KBd1UTd7_NiM:)