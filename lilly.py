from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()

mc.postToChat("Hello Lilly's world")
x, y, z = mc.player.getPos()


x, y, z = mc.player.getPos()
for loopa in range(0,3):
    mc.setBlock(x+1, y+1, z, block.DIAMOND_BLOCK.id)
    mc.setBlock(x+2, y+2, z, block.GOLD_BLOCK.id)
    mc.setBlock(x+3, y+3, z, block.STONE.id)
    mc.setBlock(x+4, y+4, z, block.NETHER_REACTOR_CORE.id)
    z = z+1

mc.player.setPos(x-5, y+2, z-10)
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, block.STONE.id)

x, y, z = mc.player.getPos()  # player position (x, y, z)
block_beneath = mc.getBlock(x, y-1, z)  # block ID
print(block_beneath)

