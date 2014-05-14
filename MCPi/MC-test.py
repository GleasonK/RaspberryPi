import mcpi.minecraft as minecraft
import mcpi.block as block
# import mcpi.camera as camera

if __name__=="__main__":

    ## MC Object variable
    mc = minecraft.Minecraft.create();
    p1 = mc.player
    ## Post to chat
    # mc.postToChat('Hello World! This is a MC API Test!')
    playerPos = p1.getPos()
    playerPos = minecraft.Vec3(int(playerPos.x),
            int(playerPos.y),int(playerPos.z))

    playerTilePos = mc.player.getTilePos()

    ## Block Below player type
    def blockBelowType():
        return mc.getBlock(playerTilePos.x, playerTilePos.y - 1,
                playerTilePos.z)

    ## Player Freefall
    def freeFall(height=50):                                  
        p1.setPos(playerPos.x, playerPos.y+height,playerPos.z)
                                                              
    ## Gold Block beside                                      
    def goldSide():                                           
        mc.setBlock(playerPos.x+1,playerPos.y+1,playerPos.z,block.GOLD_BLOCK)
                                                              
    ## Array of blocks                                        
    def glassBlock():                                         
        mc.setBlocks(playerPos.x+1, playerPos.y, playerPos.z+1, playerPos.x+5,
            playerPos.y+5, playerPos.z+5, block.GLASS)        
                                                              
    ## Diamond Floor                                          
    def diamondFloor():                                       
        mc.setBlocks(playerTilePos.x-25, playerTilePos.y-1,playerTilePos.z-25,
            playerTilePos.x+25, playerTilePos.y-1, playerTilePos.z+25,      
            block.DIAMOND_BLOCK)                              
        mc.postToChat("Now thats a Diamond Floor")            
                                                              
    def hut():                                                
        # Behind                                              
        mc.setBlocks(playerTilePos.x-5, playerTilePos.y-1, playerTilePos.z-5,
            playerTilePos.x+5, playerTilePos.y+5, playerTilePos.z-5,        
            block.GOLD_BLOCK)                                 
                                                              
        # Front                                               
        mc.setBlocks(playerTilePos.x-5, playerTilePos.y-1, playerTilePos.z+5,
            playerTilePos.x+5, playerTilePos.y+5, playerTilePos.z+5,        
            block.GOLD_BLOCK)                                 
                                                              
        # Right                                               
        mc.setBlocks(playerTilePos.x-5, playerTilePos.y-1, playerTilePos.z-5,
            playerTilePos.x-5, playerTilePos.y+5, playerTilePos.z+5,        
            block.GOLD_BLOCK)                                 
                                                              
        # Left                                                
        mc.setBlocks(playerTilePos.x+5, playerTilePos.y-1, playerTilePos.z-5,
            playerTilePos.x+5, playerTilePos.y+5, playerTilePos.z+5,        
            block.GOLD_BLOCK)          


               def perch(blockType=block.GOLD_BLOCK):                    
        # Pillar Lookout                                      
        mc.setBlocks(playerTilePos.x, playerTilePos.y+2, playerTilePos.z,   
            playerTilePos.x, playerTilePos.y+15, playerTilePos.z,
            blockType)                                        
                                                              
        #Standing Space                                       
        mc.setBlocks(playerTilePos.x-1, playerTilePos.y+15, playerTilePos.z-1,
            playerTilePos.x+1, playerTilePos.y+15, playerTilePos.z-1,       
            blockType)                                        
        freeFall(16)                                          
                                                              
    hut()                                                     
    perch()                                                   