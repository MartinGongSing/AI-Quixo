import cherrypy
import sys

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
        print(body)
        
        if body['game']%4 == 1 :
            move = 1
        elif body['game']%4 == 2 :
            move = 2
        elif body['game']%4 == 3 :
            move = 3
        elif body['game']%4 == 0:
            move = 1
            print('you lost')
        
      

        return {"move": move}



if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
         port=8081

    cherrypy.config.update({'server.socket_host' : '0.0.0.0','server.socket_port': port})
    cherrypy.quickstart(Server())