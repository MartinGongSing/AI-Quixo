import cherrypy
import sys
import random

def listinlist (lineX):
  for elem in threesome:
     if elem not in lineX:
         return False
     return True 

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

        rdmcube = [0,1,2,3,4,5,9,10,14,15,19,20,21,22,23,24]
        rdmmessage = ['Hello There', "To infinity and beyond","Why so serious",'How you doing ?', 'Execute order 66', 'Winter is coming', 'Avengers Assemble','Alohomora', 'Hakuna Matata','Follow the yellow brick road', 'For the horde', 'My Precious', 'May the force be with you',"Frankly, my dear, I don't give a damn", "Go ahead, make my day", "Fasten your seatbelts. It's going to be a bumpy night","You talking to me?","E.T. phone home","Bond. James Bond","There's no place like home","Mama always said life was like a box of chocolates. You never know what you're gonna get","I see dead people","Hasta la vista, baby","Carpe diem","I'm king of the world!", "I know Kung-Fu","中国制造","I'll be back", "Houston we have a problem"]

        ### Stocke dans 'you' la valeur de nous 
        you = 0        
        if body['players'][1] == body['you']:
            you = 1
            him = (you + 1) %2
# 
#####################################################################################
        # def basic(self) :
        #     neutral = []
        #     i=0
        #     for i in rdmcube :
        #         if body['game'][i] == None :
        #             elem = i
        #             neutral.append(elem) 
            # 
# 
        #     if len(neutral) == 0: # si pas de nt joue 'you'
        #         cube = random.choice(rdmcube)
        #         while body['game'][cube] != None and body['game'][cube] != you:
        #             cube = random.choice(rdmcube)
        #     else:
        #         cube = random.choice(neutral) 
# 
        #     return cube
##########################################################################################
        # 
        ################################
        ################################
        ################################
# 
        col1 = [ 0,  5, 10, 15, 20]
        col2 = [ 1,  6, 11, 16, 21]
        col3 = [ 2,  7, 12, 17, 22]
        col4 = [ 3,  8, 13, 18, 23]
        col5 = [ 4,  9, 14, 19, 24]
        line1 = [ 0,  1,  2,  3,  4]
        line2 = [ 5,  6,  7,  8,  9]
        line3 = [10, 11, 12, 13, 14]
        line4 = [15, 16, 17, 18, 19]
        line5 = [20, 21, 22, 23, 24]
        dia1 = [ 0,  6, 12, 18, 24]
        dia2 = [ 4,  8, 12, 16, 20]        
        # 
        ################################
        ################################
        ################################
        # 
            #  
        winlist = [
                [ 0,  1,  2,  3,  4],
                [ 5,  6,  7,  8,  9],
                [10, 11, 12, 13, 14],
                [15, 16, 17, 18, 19],
                [20, 21, 22, 23, 24],
                [ 0,  5, 10, 15, 20],
                [ 1,  6, 11, 16, 21],
                [ 2,  7, 12, 17, 22],
                [ 3,  8, 13, 18, 23],
                [ 4,  9, 14, 19, 24],
                [ 0,  6, 12, 18, 24],
                [ 4,  8, 12, 16, 20] ]
        
# 
    ####################################################
    #############           SMART           ############
    ####################################################

         
            
############# NEUTRAL ################
#Commence par jouer aléatoire neutre
        neutral = []
        for i in rdmcube :
            if body['game'][i] == None :
                neutral.append(i) 
             
        if len(neutral) == 0: # si pas de nt joue 'you'
           cube = random.choice(rdmcube)
           while body['game'][cube] != None and body['game'][cube] != you:
                     cube = random.choice(rdmcube)
                     message = random.choice(rdmmessage)
        else:
                 cube = random.choice(neutral)
                 message = random.choice(rdmmessage)    
############## SMART #################     
#regarde si nous en avons 4 en suivant                
        for y in winlist:
            threesome = []
            other = []  
            for x in y:
                if body['game'][x]== you :
                    threesome.append(x)
                    threesome = list(dict.fromkeys(threesome))
                    # print (threesome)

                elif body['game'][x]== None :
                    other.append(x)
                    other = list(dict.fromkeys(other))
                    # while len(other)>1:
                    #     del other[:] 
                    print(other)               
                # print (threesome)
                # print (other)
                elif len(threesome) == 4 and len(other)== 1: # you en a 4 qui se suivent 
                    cube = other[0]
                    if cube in rdmcube and cube == None:
                ###0-24####################################################
                        if cube == 0 :
                            if listinlist(line1) == True :
                                direction = 'E'
                            elif listinlist(dia1) == True:
                                direction = random.choice(['E','S'])
                            else : 
                                direction = 'S'
                        if cube == 1 :
                            if listinlist(line1) == True :
                                direction = 'E'
                            else : 
                                direction = 'S' 
                        if cube == 2 :
                            if listinlist(line1) == True :
                                direction = 'E'
                            else : 
                                direction = 'S'
                        if cube == 3 :
                            if listinlist(line1) == True :
                                direction = 'E'
                            else : 
                                direction = 'S'
                        if cube == 4 :
                            if listinlist(line1) == True :
                                direction = 'W'
                            elif listinlist(dia2) == True:
                                direction = random.choice(['W','S'])
                            else : 
                                direction = 'S'
                        if cube == 5 :
                            if listinlist(line2) == True :
                                direction = 'E'
                            else : 
                                direction = 'S'
                        if cube == 9 :                  
                            if listinlist(line2) == True :
                                direction = 'W'
                            else : 
                                direction = 'S'
                        if cube == 10 :               
                            if listinlist(line3) == True :
                                direction = 'E'
                            else : 
                                direction = 'S'
                        if cube == 14 :                    
                            if listinlist(line3) == True :
                                direction = 'W'
                            else : 
                                direction = 'S'
                        if cube == 15 :                    
                            if listinlist(line4) == True :
                                direction = 'E'
                            else : 
                                direction = 'S'
                        if cube == 19 :
                            if listinlist(line4) == True :
                                direction = 'W'
                            else : 
                                direction = 'S'
                        if cube == 20 :
                            if listinlist(line5) == True :
                                direction = 'E'
                            elif listinlist(dia2) == True:
                                direction = random.choice(['E','N'])
                            else : 
                                direction = 'N'
                        if cube == 21 :
                            if listinlist(line5) == True :
                                direction = 'E'
                            else : 
                                direction = 'N'
                        if cube == 22 :
                            if listinlist(line5) == True :
                                direction = 'E'
                            else : 
                                direction = 'N'
                        if cube == 23 :
                            if listinlist(line5) == True :
                                direction = 'E'
                            else : 
                                direction = 'N'
                        if cube == 24 :
                            if listinlist(line5) == True :
                                direction = 'W'
                            elif listinlist(dia1) == True:
                                direction = random.choice(['W','N'])
                            else : 
                                direction = 'N'
                ###end of it#######################################################

                    message = 'OKAYYYYYYYY'
                
                

            
                    # Joue neutre
                    #  Faire une liste ave c NT si liste == 0 alors on prend les X 
                        
                ############
                ############
                            
                
                dirE =[9, 14, 19]
                dirW =[5, 10, 15]
                dirN =[1, 2, 3]
                dirS =[21, 22, 23]

                if cube == 0 :
                    direction = random.choice(['E','S'])
                    message = random.choice(rdmmessage)
                elif cube == 4 :
                    direction = random.choice(['W','S'])
                    message = random.choice(rdmmessage)
                elif cube == 20 :
                    direction = random.choice(['E','N'])
                    message = random.choice(rdmmessage)
                elif cube == 24 :
                    direction = random.choice(['N','W'])
                    message = random.choice(rdmmessage)
                elif cube in dirE:
                    direction = random.choice(['N','S','W'])
                    message = random.choice(rdmmessage)
                elif cube in dirW:
                    direction = random.choice(['N','S','E'])
                    message = random.choice(rdmmessage)
                elif cube in dirN:
                    direction =random.choice(['S','W','E'])
                    message = random.choice(rdmmessage)
                elif cube in dirS:
                    direction =random.choice(['N','W','E'])
                    message = random.choice(rdmmessage)        
                
                #############
                #############
            

    


        return {"move": {'cube' : int(cube), 'direction' : str(direction)}, "message" : str(message)}



if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8083

    cherrypy.config.update({'server.socket_host' : '0.0.0.0','server.socket_port': port})
    cherrypy.quickstart(Server())
    
    