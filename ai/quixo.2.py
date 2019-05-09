import cherrypy
import sys
import random

class Server:
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        if cherrypy.request.method == "OPTIONS":
            return ''
        
        body = cherrypy.request.json
        
        
        ################ RANDOM ##################
                
        rdmcube = [0,1,2,3,4,5,9,10,14,15,19,20,21,22,23,24]
                
        ### stocke dans 'you' la valeur de nous
        you = 0
        if body['players'][1] == body['you']:
            you = 1         
        ###choisi un cube au hasard qui est neutre ou a nous
        cube = random.choice(rdmcube)
        while body['game'][cube] != None and body['game'][cube] != you:
            cube = random.choice(rdmcube)

        ###listes pour lesquels X cube ne suis pas 'Y' direction
        dirE =[9, 14, 19]
        dirW =[5, 10, 15]
        dirN =[1, 2, 3]
        dirS =[21, 22, 23]

        ### vérifie si cube est dans liste interdite
        if cube == 0 :
            direction = random.choice(['E','S'])
        elif cube == 4 :
            direction = random.choice(['W','S'])
        elif cube == 20 :
            direction = random.choice(['E','N'])
        elif cube == 24 :
            direction = random.choice(['N','W'])
        elif cube in dirE:
            direction = random.choice(['N','S','W'])
        elif cube in dirW:
            direction = random.choice(['N','S','E'])
        elif cube in dirN:
            direction =random.choice(['S','W','E'])
        elif cube in dirS:
            direction =random.choice(['N','W','E'])

        ################# FIN RANDOM #######################

        return {"move": {'cube' : int(cube), 'direction' : str(direction)}, "message" : "Gotcha"}



if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8083

    cherrypy.config.update({'server.socket_host' : '0.0.0.0','server.socket_port': port})
    cherrypy.quickstart(Server())
    
    