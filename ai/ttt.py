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

        # if body['game'][0-8] == None :
        #     move = 0
        # elif body['game'][0] == 1  :
        #     move = 1
        # elif body['game'][1] == 1  :
        #     move = 2
        # elif body['game'][2] == 1  :
        #     move = 3
        # elif body['game'][3] == 1  :
        #     move = 4
        # elif body['game'][4] == 1  :
        #     move = 5
        # elif body['game'][5] == 1  :
        #     move = 6
        # elif body['game'][6] == 1  :
        #     move = 7
        # elif body['game'][7] == 1  :
        #     move = 8


        for i in range(8):
            if body['game'][i] == None :
                move = i
                break
                
        # if body['game'][0-8] == None :
        #     if body['game'][0] == 0 or 1:
        #         if body['game'][1] == 0 or 1  :
        #             if body['game'][2] == 0 or 1  :
        #                 if body['game'][3] == 0 or 1  :
        #                     if body['game'][4] == 0 or 1  :
        #                         if body['game'][5] == 0 or 1  :
        #                             if body['game'][6] == 0 or 1  :
        #                                 if body['game'][7] == 0 or 1  :
        #                                     move = 8                                    
        #                             else:
        #                                  move = 7
        #                         else:
        #                              move = 6
        #                     else:
        #                          move = 5
        #                 else:
        #                      move = 4
        #             else:
        #                  move = 3
        #         else:
        #              move = 2
        #     else:
        #          move = 1
        # else:
        #      move = 0

        return {"move": move}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8081

    cherrypy.config.update({'server.socket_host' : '0.0.0.0','server.socket_port': port})
    cherrypy.quickstart(Server())