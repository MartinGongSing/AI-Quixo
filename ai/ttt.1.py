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
        #wins if 012-345-678-036-147-258-048-246
        
        for i in range(8):
            if body['game'][i] == None :
                
                move = i
                break
            

        
        return {"move": move}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8082

    cherrypy.config.update({'server.socket_host' : '0.0.0.0','server.socket_port': port})
    cherrypy.quickstart(Server())