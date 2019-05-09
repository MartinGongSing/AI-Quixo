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
        name = str(body['you'])
        if name == str(body['players'][0]):
            case = input("quelle case 0 ? : ")
            direc = input("direction 0 ? : ")
            return {"move": {'cube':int(case), 'direction':str(direc)}}
        else:
            case = input("quelle case 1 ? : ")
            direc = input("direction 1 ? : ")
            return {"move": {'cube':int(case), 'direction':str(direc)}}

        
        

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8083

    cherrypy.config.update({'server.socket_port': port})
    cherrypy.quickstart(Server())