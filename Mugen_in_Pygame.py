import pygame
import sys
import os
from random import randint
import time

RED4 = "\033[31m"
BLUE4 = "\033[34m"
RESET = "\033[0m"
WHITE4= "\033[37m"
BOLD4 = "\033[1m"
UNDERLINE4="\033[4m"
#pygame and pip install coloram
pygame.init()
pygame.mixer.init()
#info on what I did
print("\n")
print(BOLD4+ WHITE4 + "Figther facotry dio is scale  3 and rin is 2"+ RESET)
print("\n")
#demon lord dio
print(BOLD4+ WHITE4 +" Demon Lord Dio Spire:"+ RESET)
print(UNDERLINE4+ BLUE4 + " https://mugenarchive.com/forums/downloads.php?do=file&id=158222-demon-lord-dio-edit-sweet-adventurer"+ RESET)
print(BOLD4+ WHITE4 +" Demon Lord Controls:"+ RESET)
print(BOLD4+ WHITE4 +" E: Throw"+ RESET)
print(BOLD4+ WHITE4 +" F: Barrage Punch"+ RESET)
print(BOLD4+ WHITE4 +" R: Special"+ RESET)
print("\n")
print(BOLD4+ WHITE4 +" Rin Kagamine Spire:"+ RESET)
print(UNDERLINE4+ BLUE4 + " https://mugenarchive.com/forums/downloads.php?do=file&id=10686-rin-kagamine-nanda"+ RESET)
print(BOLD4+ WHITE4 +" Rin Kagamine Controls:"+ RESET)
print(BOLD4+ WHITE4 +" Z: Throw"+ RESET)
print(BOLD4+ WHITE4 +" Q: Punch"+ RESET)
print(BOLD4+ WHITE4 +" C: Special"+ RESET)
print("\n")


#tools
print(BOLD4+ WHITE4 +"Tools I Used:"+ RESET)
print(UNDERLINE4+ BLUE4 + " https://virtualltek.com/download/"+ RESET)
print(UNDERLINE4+ BLUE4 + " https://onlinegiftools.com/flip-gif"+ RESET)
print(UNDERLINE4+ BLUE4 + " https://scratch.mit.edu/"+ RESET)
print(UNDERLINE4+ BLUE4 + " https://mugenarchive.com/forums/downloads.php?do=cat&id=39-mugen-builds"+ RESET)
print("\n")






# display
width, height = 1900, 950
win = pygame.display.set_mode((width, height), pygame.SRCALPHA)
pygame.display.set_caption("Mugen in Pygmae")
clock = pygame.time.Clock()
clicked_to_fullscreen = False


# load sounds
mm = pygame.mixer.Sound("Main Menu.mp3")
mm.play(loops=-1)
hitsound = pygame.mixer.Sound("loud hit.wav")
hitsound.set_volume(0.5)
muda = pygame.mixer.Sound("very long muda.wav")
diothrow=pygame.mixer.Sound("wwrry.wav")
rinhitsound=pygame.mixer.Sound("rinhit2.wav")
rindancesong=pygame.mixer.Sound("rindancesong.wav")
rinthrowsound=pygame.mixer.Sound("rinthrowsound.wav")
spawn=pygame.mixer.Sound("stand spawn.wav")
muitairhit=pygame.mixer.Sound("muitairhit.wav")
muitairhit.set_volume(0.5)
muda.set_volume(0.5)
diothrow.set_volume(0.5)
superintro=pygame.mixer.Sound("I will not stay by this.wav")

stand= pygame.image.load("zaworldstand.png")
standleft= pygame.image.load("zaworldleft.png")
standgone =pygame.image.load("invs.png")
bg = pygame.image.load("jojoBsG.jpg")
char_left = pygame.image.load("diostandleft.png")
char_right = pygame.image.load("diostandright.png")
char = char_right

# movement
walkLeft = [
    pygame.image.load("diowalkleft.png"),
    pygame.image.load("diowalkleft2.png"),
    pygame.image.load("diowalkleft3.png"),
    pygame.image.load("diowalkleft4.png"),
    pygame.image.load("diowalkleft5.png"),
    pygame.image.load("diowalkleft6.png"),
]

walkRight = [
    pygame.image.load("diowalkright.png"),
    pygame.image.load("diowalkright2.png"),
    pygame.image.load("diowalkright3.png"),
    pygame.image.load("diowalkright4.png"),
    pygame.image.load("diowalkright5.png"),
    pygame.image.load("diowalkright6.png"),
]

standkick = [
    pygame.image.load("muda_kick.png"),
    pygame.image.load("muda_kick2.png"),
    pygame.image.load("muda_kick3.png"),
    pygame.image.load("muda_kick4.png"),
    pygame.image.load("muda_kick5.png"),
    pygame.image.load("muda_kick6.png"),
    pygame.image.load("muda_kick7.png"),
    pygame.image.load("muda_kick8.png"),
    pygame.image.load("muda_kick.png"),
    pygame.image.load("muda_kick2.png"),
    pygame.image.load("muda_kick3.png"),
    pygame.image.load("muda_kick4.png"),
    pygame.image.load("muda_kick5.png"),
    pygame.image.load("muda_kick6.png"),
    pygame.image.load("muda_kick7.png"),
    pygame.image.load("muda_kick8.png"),
    pygame.image.load("muda_kick.png"),
    pygame.image.load("muda_kick2.png"),
    pygame.image.load("muda_kick3.png"),
    pygame.image.load("muda_kick4.png"),
    pygame.image.load("muda_kick5.png"),
    pygame.image.load("muda_kick6.png"),
    pygame.image.load("muda_kick7.png"),
    pygame.image.load("muda_kick8.png"),
]

standkickleft = [
    pygame.image.load("muda_kickleft.png"),
    pygame.image.load("muda_kickleft2.png"),
    pygame.image.load("muda_kickleft3.png"),
    pygame.image.load("muda_kickleft4.png"),
    pygame.image.load("muda_kickleft5.png"),
    pygame.image.load("muda_kickleft6.png"),
    pygame.image.load("muda_kickleft7.png"),
    pygame.image.load("muda_kickleft8.png"),
    pygame.image.load("muda_kickleft.png"),
    pygame.image.load("muda_kickleft2.png"),
    pygame.image.load("muda_kickleft3.png"),
    pygame.image.load("muda_kickleft4.png"),
    pygame.image.load("muda_kickleft5.png"),
    pygame.image.load("muda_kickleft6.png"),
    pygame.image.load("muda_kickleft7.png"),
    pygame.image.load("muda_kickleft8.png"),
    pygame.image.load("muda_kickleft.png"),
    pygame.image.load("muda_kickleft2.png"),
    pygame.image.load("muda_kickleft3.png"),
    pygame.image.load("muda_kickleft4.png"),
    pygame.image.load("muda_kickleft5.png"),
    pygame.image.load("muda_kickleft6.png"),
    pygame.image.load("muda_kickleft7.png"),
    pygame.image.load("muda_kickleft8.png"),
]


jump = [
    pygame.image.load("diojump.png"),
    pygame.image.load("diojump2.png"),
    pygame.image.load("diojump.png"),
    pygame.image.load("diojump2.png"),
    pygame.image.load("diojump.png"),
    pygame.image.load("diojump2.png"),
    pygame.image.load("diojump.png"),
    pygame.image.load("diojump2.png"),
    pygame.image.load("diojump.png"),
    pygame.image.load("diojump2.png"),
    pygame.image.load("diojump.png"),
    pygame.image.load("diojump2.png"),
    pygame.image.load("diojump.png"),
    pygame.image.load("diojump2.png"),
    pygame.image.load("diojump.png"),
    pygame.image.load("diojump2.png"),
    pygame.image.load("diojump.png"),
    pygame.image.load("diojump2.png"),
    pygame.image.load("diojump.png"),
    pygame.image.load("diojump2.png"),
    pygame.image.load("diojump.png"),
    pygame.image.load("diojump2.png"),
    pygame.image.load("diojump.png"),
    pygame.image.load("diojump2.png"),
]

fall = [
    pygame.image.load("fall down.png"),
    pygame.image.load("fall down2.png"),
    pygame.image.load("fall down3.png"),
]

jumpleft = [
    pygame.image.load("diojumpleft.png"),
    pygame.image.load("diojumpleft2.png"),
    pygame.image.load("diojumpleft.png"),
    pygame.image.load("diojumpleft2.png"),
    pygame.image.load("diojumpleft.png"),
    pygame.image.load("diojumpleft2.png"),
    pygame.image.load("diojumpleft.png"),
    pygame.image.load("diojumpleft2.png"),
    pygame.image.load("diojumpleft.png"),
    pygame.image.load("diojumpleft2.png"),
    pygame.image.load("diojumpleft.png"),
    pygame.image.load("diojumpleft2.png"),
    pygame.image.load("diojumpleft.png"),
    pygame.image.load("diojumpleft2.png"),
    pygame.image.load("diojumpleft.png"),
    pygame.image.load("diojumpleft2.png"),
    pygame.image.load("diojumpleft.png"),
    pygame.image.load("diojumpleft2.png"),
]

fallleft = [
    pygame.image.load("fall downleft.png"),
    pygame.image.load("fall downleft2.png"),
    pygame.image.load("fall downleft3.png"),
]

dioanim = [
    pygame.image.load("diothrow.png"),
    pygame.image.load("diothrow2.png"),
    pygame.image.load("diothrow3.png"),
    pygame.image.load("diothrow4.png"),
    pygame.image.load("diothrow2.png"),
    pygame.image.load("diothrow3.png"),
    pygame.image.load("diothrow4.png"),
    pygame.image.load("diothrow2.png"),
    pygame.image.load("diothrow3.png"),
    pygame.image.load("diothrow4.png"),
]

dioanimleft = [
    pygame.image.load("diothrowleft.png"),
    pygame.image.load("diothrowleft2.png"),
    pygame.image.load("diothrowleft3.png"),
    pygame.image.load("diothrowleft4.png"),
    pygame.image.load("diothrowleft2.png"),
    pygame.image.load("diothrowleft3.png"),
    pygame.image.load("diothrowleft4.png"),
    pygame.image.load("diothrowleft2.png"),
    pygame.image.load("diothrowleft3.png"),
    pygame.image.load("diothrowleft4.png"),
]

mudapunching = [
    pygame.image.load("mudapunch.png"),
    pygame.image.load("mudapunch2.png"),
    pygame.image.load("mudapunch3.png"),
    pygame.image.load("mudapunch4.png"),
    pygame.image.load("mudapunch5.png"),
    pygame.image.load("mudapunch6.png"),
    pygame.image.load("mudapunch7.png"),
    pygame.image.load("mudapunch8.png"),
    pygame.image.load("mudapunch.png"),
    pygame.image.load("mudapunch2.png"),
    pygame.image.load("mudapunch3.png"),
    pygame.image.load("mudapunch4.png"),
    pygame.image.load("mudapunch5.png"),
    pygame.image.load("mudapunch6.png"),
    pygame.image.load("mudapunch7.png"),
    pygame.image.load("mudapunch8.png"),
    pygame.image.load("mudapunch.png"),
    pygame.image.load("mudapunch2.png"),
    pygame.image.load("mudapunch3.png"),
    pygame.image.load("mudapunch4.png"),
    pygame.image.load("mudapunch5.png"),
    pygame.image.load("mudapunch6.png"),
    pygame.image.load("mudapunch7.png"),
    pygame.image.load("mudapunch8.png"),
]

mudapunchleft = [
    pygame.image.load("mudapunchleft.png"),
    pygame.image.load("mudapunchleft2.png"),
    pygame.image.load("mudapunchleft3.png"),
    pygame.image.load("mudapunchleft4.png"),
    pygame.image.load("mudapunchleft5.png"),
    pygame.image.load("mudapunchleft6.png"),
    pygame.image.load("mudapunchleft7.png"),
    pygame.image.load("mudapunchleft8.png"),
    pygame.image.load("mudapunchleft.png"),
    pygame.image.load("mudapunchleft2.png"),
    pygame.image.load("mudapunchleft3.png"),
    pygame.image.load("mudapunchleft4.png"),
    pygame.image.load("mudapunchleft5.png"),
    pygame.image.load("mudapunchleft6.png"),
    pygame.image.load("mudapunchleft7.png"),
    pygame.image.load("mudapunchleft8.png"),
    pygame.image.load("mudapunchleft.png"),
    pygame.image.load("mudapunchleft2.png"),
    pygame.image.load("mudapunchleft3.png"),
    pygame.image.load("mudapunchleft4.png"),
    pygame.image.load("mudapunchleft5.png"),
    pygame.image.load("mudapunchleft6.png"),
    pygame.image.load("mudapunchleft7.png"),
    pygame.image.load("mudapunchleft8.png"),
]

#------------
#rin
rin_right = pygame.image.load("Rinidle.png")
rin_left = pygame.image.load("Rinidleleft.png")
rin = rin_left

rin_hit = [
    pygame.image.load("rin hit.png"),
    pygame.image.load("rin hit2.png"),
    pygame.image.load("rin hit3.png"),
    pygame.image.load("rin hit4.png"),
    pygame.image.load("rin hit5.png"),
    pygame.image.load("rin hit.png"),
    pygame.image.load("rin hit2.png"),
    pygame.image.load("rin hit3.png"),
    pygame.image.load("rin hit4.png"),
    pygame.image.load("rin hit5.png"),
]

rin_hitleft = [
    pygame.image.load("rin hitleft.png"),
    pygame.image.load("rin hitleft2.png"),
    pygame.image.load("rin hitleft3.png"),
    pygame.image.load("rin hitleft4.png"),
    pygame.image.load("rin hitleft5.png"),
    pygame.image.load("rin hitleft.png"),
    pygame.image.load("rin hitleft2.png"),
    pygame.image.load("rin hitleft3.png"),
    pygame.image.load("rin hitleft4.png"),
    pygame.image.load("rin hitleft5.png"),
]

#jumps
rinjump = [
    pygame.image.load("rinjump.png"),
    pygame.image.load("rinjump2.png"),
    pygame.image.load("rinjump3.png"),
    pygame.image.load("rinjump4.png"),
    pygame.image.load("rinjump5.png"),
    pygame.image.load("rinjump6.png"),
    pygame.image.load("rinjump7.png"),
    pygame.image.load("rinjump8.png"),
    pygame.image.load("rinjump.png"),
    pygame.image.load("rinjump2.png"),
    pygame.image.load("rinjump3.png"),
    pygame.image.load("rinjump4.png"),
    pygame.image.load("rinjump5.png"),
    pygame.image.load("rinjump6.png"),
    pygame.image.load("rinjump7.png"),
    pygame.image.load("rinjump8.png"),
]

rinjumpleft = [
    pygame.image.load("rinjumpleft.png"),
    pygame.image.load("rinjumpleft2.png"),
    pygame.image.load("rinjumpleft3.png"),
    pygame.image.load("rinjumpleft4.png"),
    pygame.image.load("rinjumpleft5.png"),
    pygame.image.load("rinjumpleft6.png"),
    pygame.image.load("rinjumpleft7.png"),
    pygame.image.load("rinjumpleft8.png"),
    pygame.image.load("rinjumpleft.png"),
    pygame.image.load("rinjumpleft2.png"),
    pygame.image.load("rinjumpleft3.png"),
    pygame.image.load("rinjumpleft4.png"),
    pygame.image.load("rinjumpleft5.png"),
    pygame.image.load("rinjumpleft6.png"),
    pygame.image.load("rinjumpleft7.png"),
    pygame.image.load("rinjumpleft8.png"),
]

#movement
rinfall = [
    pygame.image.load("rinfall.png"),
    pygame.image.load("rinfall.png"),
    pygame.image.load("rinfall.png"),
]

rinfallleft = [
    pygame.image.load("rinfallleft.png"),
    pygame.image.load("rinfallleft.png"),
    pygame.image.load("rinfallleft.png"),
]

rinwalkRight = [
    pygame.image.load("rinwalk.png"),
    pygame.image.load("rinwalk2.png"),
    pygame.image.load("rinwalk3.png"),
    pygame.image.load("rinwalk4.png"),
    pygame.image.load("rinwalk5.png"),
    pygame.image.load("rinwalk6.png"),
    pygame.image.load("rinwalk7.png"),
]

rinwalkLeft = [
    pygame.image.load("rinwalkleft.png"),
    pygame.image.load("rinwalkleft2.png"),
    pygame.image.load("rinwalkleft3.png"),
    pygame.image.load("rinwalkleft4.png"),
    pygame.image.load("rinwalkleft5.png"),
    pygame.image.load("rinwalkleft6.png"),
    pygame.image.load("rinwalkleft7.png"),
]

rindance=[pygame.image.load("rindace.png"),pygame.image.load("rindace2.png"),pygame.image.load("rindace3.png"),pygame.image.load("rindace4.png"),pygame.image.load("rindace5.png"),pygame.image.load("rindace6.png"),pygame.image.load("rindace7.png"),pygame.image.load("rindace8.png"),pygame.image.load("rindace9.png"),pygame.image.load("rindace10.png"),pygame.image.load("rindace.png"),pygame.image.load("rindace2.png"),pygame.image.load("rindace3.png"),pygame.image.load("rindace4.png"),pygame.image.load("rindace5.png"),pygame.image.load("rindace6.png"),pygame.image.load("rindace7.png"),pygame.image.load("rindace8.png"),pygame.image.load("rindace9.png"),pygame.image.load("rindace10.png"),pygame.image.load("rindace.png"),pygame.image.load("rindace2.png"),pygame.image.load("rindace3.png"),pygame.image.load("rindace4.png"),pygame.image.load("rindace5.png"),pygame.image.load("rindace6.png"),pygame.image.load("rindace7.png"),pygame.image.load("rindace8.png"),pygame.image.load("rindace9.png"),pygame.image.load("rindace10.png"),pygame.image.load("rindace.png"),pygame.image.load("rindace2.png"),pygame.image.load("rindace3.png"),pygame.image.load("rindace4.png"),pygame.image.load("rindace5.png"),pygame.image.load("rindace6.png"),pygame.image.load("rindace7.png"),pygame.image.load("rindace8.png"),pygame.image.load("rindace9.png"),pygame.image.load("rindace10.png"),pygame.image.load("rindace.png"),pygame.image.load("rindace2.png"),pygame.image.load("rindace3.png"),pygame.image.load("rindace4.png"),pygame.image.load("rindace5.png"),pygame.image.load("rindace6.png"),pygame.image.load("rindace7.png"),pygame.image.load("rindace8.png"),pygame.image.load("rindace9.png"),pygame.image.load("rindace10.png"),pygame.image.load("rindace.png"),pygame.image.load("rindace2.png"),pygame.image.load("rindace3.png"),pygame.image.load("rindace4.png"),pygame.image.load("rindace5.png"),pygame.image.load("rindace6.png"),pygame.image.load("rindace7.png"),pygame.image.load("rindace8.png"),pygame.image.load("rindace9.png"),pygame.image.load("rindace10.png"),pygame.image.load("rindace.png"),pygame.image.load("rindace2.png"),pygame.image.load("rindace3.png"),pygame.image.load("rindace4.png"),pygame.image.load("rindace5.png"),pygame.image.load("rindace6.png"),pygame.image.load("rindace7.png"),pygame.image.load("rindace8.png"),pygame.image.load("rindace9.png"),pygame.image.load("rindace10.png"),pygame.image.load("rindace.png"),pygame.image.load("rindace2.png"),pygame.image.load("rindace3.png"),pygame.image.load("rindace4.png"),pygame.image.load("rindace5.png"),pygame.image.load("rindace6.png"),pygame.image.load("rindace7.png"),pygame.image.load("rindace8.png"),pygame.image.load("rindace9.png"),pygame.image.load("rindace10.png"),]

#projectles
throwanimleft = [
    pygame.image.load("cheerleft.png"),
    pygame.image.load("cheerleft2.png"),
    pygame.image.load("cheerleft3.png"),
    pygame.image.load("cheerleft.png"),
    pygame.image.load("cheerleft2.png"),
    pygame.image.load("cheerleft3.png"),
    pygame.image.load("cheerleft3.png"),
    pygame.image.load("cheerleft3.png"),
    pygame.image.load("cheerleft3.png"),
    pygame.image.load("cheerleft3.png"),
    pygame.image.load("cheerleft3.png"),
    pygame.image.load("cheerleft3.png"),
]

throwanim = [
    pygame.image.load("cheer.png"),
    pygame.image.load("cheer2.png"),
    pygame.image.load("cheer3.png"),
    pygame.image.load("cheer.png"),
    pygame.image.load("cheer2.png"),
    pygame.image.load("cheer3.png"),
    pygame.image.load("cheer3.png"),
    pygame.image.load("cheer3.png"),
    pygame.image.load("cheer3.png"),
    pygame.image.load("cheer3.png"),
    pygame.image.load("cheer3.png"),
    pygame.image.load("cheer3.png"),
]

lastanim=pygame.image.load("cheer3.png")

# rin projectile images
rinprojectile_images = [
    pygame.image.load("lenroadleft.png").convert_alpha(),
    pygame.image.load("lenroadleft2.png").convert_alpha(),
    pygame.image.load("lenroadleft3.png").convert_alpha(),
    pygame.image.load("lenroadleft4.png").convert_alpha(),
    pygame.image.load("lenroadleft5.png").convert_alpha(),
]

rinprojectile_images2 = [
    pygame.image.load("lenroad.png").convert_alpha(),
    pygame.image.load("lenroad2.png").convert_alpha(),
    pygame.image.load("lenroad3.png").convert_alpha(),
    pygame.image.load("lenroad4.png").convert_alpha(),
    pygame.image.load("lenroad5.png").convert_alpha(),
]
# dio projectile images

projectile_images = [
    pygame.image.load("muda_kickleft.png").convert_alpha(),
    pygame.image.load("muda_kickleft2.png").convert_alpha(),
    pygame.image.load("muda_kickleft3.png").convert_alpha(),
    pygame.image.load("muda_kickleft4.png").convert_alpha(),
    pygame.image.load("muda_kickleft5.png").convert_alpha(),
    pygame.image.load("muda_kickleft6.png").convert_alpha(),
    pygame.image.load("muda_kickleft7.png").convert_alpha(),
    pygame.image.load("muda_kickleft8.png").convert_alpha()
]

projectile_images2 = [
    pygame.image.load("muda_kick.png").convert_alpha(),
    pygame.image.load("muda_kick2.png").convert_alpha(),
    pygame.image.load("muda_kick3.png").convert_alpha(),
    pygame.image.load("muda_kick4.png").convert_alpha(),
    pygame.image.load("muda_kick5.png").convert_alpha(),
    pygame.image.load("muda_kick6.png").convert_alpha(),
    pygame.image.load("muda_kick7.png").convert_alpha(),
    pygame.image.load("muda_kick8.png").convert_alpha()
]
#idles
#stnad idle
isr = [
    pygame.image.load("ildezaworld.png"),
    pygame.image.load("ildezaworld2.png"),
    pygame.image.load("ildezaworld3.png"),
    pygame.image.load("ildezaworld4.png"),
    pygame.image.load("ildezaworld5.png"),
    pygame.image.load("ildezaworld6.png"),
    pygame.image.load("ildezaworld7.png"),
    pygame.image.load("ildezaworld8.png"),
]

isl = [
    pygame.image.load("ildezaworldleft.png"),
    pygame.image.load("ildezaworldleft2.png"),
    pygame.image.load("ildezaworldleft3.png"),
    pygame.image.load("ildezaworldleft4.png"),
    pygame.image.load("ildezaworldleft5.png"),
    pygame.image.load("ildezaworldleft6.png"),
    pygame.image.load("ildezaworldleft7.png"),
    pygame.image.load("ildezaworldleft8.png"),
]

standgoneidle = [
    pygame.image.load("invs.png"),
    pygame.image.load("invs.png"),
    pygame.image.load("invs.png"),
    pygame.image.load("invs.png"),
    pygame.image.load("invs.png"),
    pygame.image.load("invs.png"),
    pygame.image.load("invs.png"),
    pygame.image.load("invs.png"),
]

standidle_left = isl
standidle_right = isr

#dio idle
idr = [
    pygame.image.load("dioildeleft.png"),
    pygame.image.load("dioildeleft2.png"),
    pygame.image.load("dioildeleft3.png"),
    pygame.image.load("dioildeleft4.png"),
    pygame.image.load("dioildeleft5.png"),
    pygame.image.load("dioildeleft6.png"),
    pygame.image.load("dioildeleft7.png"),
]

idl = [
    pygame.image.load("dioilde.png"),
    pygame.image.load("dioilde2.png"),
    pygame.image.load("dioilde3.png"),
    pygame.image.load("dioilde4.png"),
    pygame.image.load("dioilde5.png"),
    pygame.image.load("dioilde6.png"),
    pygame.image.load("dioilde7.png"),
]

idle_left = idr
idle_right =idl


diogoneidle = [
    pygame.image.load("invs.png"),
    pygame.image.load("invs.png"),
    pygame.image.load("invs.png"),
    pygame.image.load("invs.png"),
    pygame.image.load("invs.png"),
    pygame.image.load("invs.png"),
    pygame.image.load("invs.png"),
]

#rin idle

irr = [
    pygame.image.load("Rinidle.png"),
    pygame.image.load("Rinidle2.png"),
    pygame.image.load("Rinidle3.png"),
    pygame.image.load("Rinidle4.png"),
    pygame.image.load("Rinidle5.png"),
]

irl = [
    pygame.image.load("Rinidleleft.png"),
    pygame.image.load("Rinidleleft2.png"),
    pygame.image.load("Rinidleleft3.png"),
    pygame.image.load("Rinidleleft4.png"),
    pygame.image.load("Rinidleleft5.png"),
]

rinidle_right=irr
rinidle_left=irl



# effects
hit = [
    pygame.image.load("normalhit5.png"),
    pygame.image.load("normalhit5.png"),
    pygame.image.load("normalhit4.png"),
    pygame.image.load("normalhit4.png"),
    pygame.image.load("normalhit3.png"),
    pygame.image.load("normalhit3.png"),
    pygame.image.load("normalhit2.png"),
    pygame.image.load("normalhit2.png"),
    pygame.image.load("normalhit.png"),
    pygame.image.load("normalhit.png"),
    pygame.image.load("invs.png"),
]

index4=0
index5=0
index8=0
dioreadingleft = [
    pygame.image.load("dioreadingleft.png"),
    pygame.image.load("dioreadingleft2.png"),
    pygame.image.load("dioreadingleft3.png"),
    pygame.image.load("dioreadingleft4.png"),
    pygame.image.load("dioreadingleft5.png"),
    pygame.image.load("dioreadingleft6.png"),
    pygame.image.load("dioreadingleft7.png"),
    pygame.image.load("dioreadingleft8.png"),
    pygame.image.load("dioreadingleft9.png"),
    pygame.image.load("dioreadingleft10.png"),
    pygame.image.load("dioreadingleft11.png"),
    pygame.image.load("dioreadingleft12.png"),
    pygame.image.load("dioreadingleft13.png"),
    pygame.image.load("dioreadingleft14.png"),
    pygame.image.load("dioreadingleft15.png"),
    pygame.image.load("dioreadingleft16.png"),
    pygame.image.load("dioreadingleft17.png"),
    pygame.image.load("dioreadingleft18.png"),
    pygame.image.load("dioreadingleft19.png"),
    pygame.image.load("dioreadingleft20.png"),
    pygame.image.load("dioreadingleft21.png"),
    pygame.image.load("dioreadingleft22.png"),
    pygame.image.load("dioreadingleft23.png"),
    pygame.image.load("dioreadingleft24.png"),
    pygame.image.load("dioreadingleft25.png"),
    pygame.image.load("dioreadingleft26.png"),
    pygame.image.load("dioreadingleft27.png"),
    pygame.image.load("dioreadingleft28.png"),
    pygame.image.load("dioreadingleft29.png"),
    pygame.image.load("dioreadingleft30.png"),
    pygame.image.load("dioreadingleft31.png"),
    pygame.image.load("dioreadingleft32.png"),
    pygame.image.load("dioreadingleft33.png"),
    pygame.image.load("dioreadingleft34.png"),
    pygame.image.load("dioreadingleft35.png"),
    pygame.image.load("dioreadingleft36.png"),
    pygame.image.load("dioreadingleft37.png"),
    pygame.image.load("dioreadingleft38.png"),
    pygame.image.load("dioreadingleft39.png")
]

dioreading = [
    pygame.image.load("dioreading.png"),
    pygame.image.load("dioreading2.png"),
    pygame.image.load("dioreading3.png"),
    pygame.image.load("dioreading4.png"),
    pygame.image.load("dioreading5.png"),
    pygame.image.load("dioreading6.png"),
    pygame.image.load("dioreading7.png"),
    pygame.image.load("dioreading8.png"),
    pygame.image.load("dioreading9.png"),
    pygame.image.load("dioreading10.png"),
    pygame.image.load("dioreading11.png"),
    pygame.image.load("dioreading12.png"),
    pygame.image.load("dioreading13.png"),
    pygame.image.load("dioreading14.png"),
    pygame.image.load("dioreading15.png"),
    pygame.image.load("dioreading16.png"),
    pygame.image.load("dioreading17.png"),
    pygame.image.load("dioreading18.png"),
    pygame.image.load("dioreading19.png"),
    pygame.image.load("dioreading20.png"),
    pygame.image.load("dioreading21.png"),
    pygame.image.load("dioreading22.png"),
    pygame.image.load("dioreading23.png"),
    pygame.image.load("dioreading24.png"),
    pygame.image.load("dioreading25.png"),
    pygame.image.load("dioreading26.png"),
    pygame.image.load("dioreading27.png"),
    pygame.image.load("dioreading28.png"),
    pygame.image.load("dioreading29.png"),
    pygame.image.load("dioreading30.png"),
    pygame.image.load("dioreading31.png"),
    pygame.image.load("dioreading32.png"),
    pygame.image.load("dioreading33.png"),
    pygame.image.load("dioreading34.png"),
    pygame.image.load("dioreading35.png"),
    pygame.image.load("dioreading36.png"),
    pygame.image.load("dioreading37.png"),
    pygame.image.load("dioreading38.png"),
    pygame.image.load("dioreading39.png")
]

yellowhit = [
    pygame.image.load("yellowhit4.png"),
    pygame.image.load("yellowhit3.png"),
    pygame.image.load("yellowhit2.png"),
    pygame.image.load("yellowhit.png"),
    pygame.image.load("invs.png"),
]

rinsuperhit = [
    pygame.image.load("superhit.png"),
    pygame.image.load("superhit2.png"),
    pygame.image.load("superhit3.png"),
    pygame.image.load("superhit4.png"),
    pygame.image.load("superhit5.png"),
    pygame.image.load("superhit6.png"),
    pygame.image.load("superhit7.png"),
    pygame.image.load("superhit8.png"),
    pygame.image.load("superhit9.png"),
    pygame.image.load("superhit10.png"),
    pygame.image.load("superhit11.png"),
    pygame.image.load("superhit12.png"),
    pygame.image.load("superhit13.png"),
    pygame.image.load("superhit14.png"),
    pygame.image.load("superhit15.png"),
    pygame.image.load("superhit16.png"),
    pygame.image.load("superhit17.png"),
    pygame.image.load("superhit18.png"),
    pygame.image.load("superhit19.png"),
    pygame.image.load("superhit20.png"),
    pygame.image.load("superhit21.png"),
    pygame.image.load("superhit22.png"),
    pygame.image.load("superhit23.png"),
    pygame.image.load("superhit24.png"),
    pygame.image.load("superhit25.png"),
    pygame.image.load("invs.png"),
]

superhitmuiscnote = [
    pygame.image.load("invs.png"),
    pygame.image.load("superhitmuiscnote.png"),
    pygame.image.load("superhitmuiscnote2.png"),
    pygame.image.load("superhitmuiscnote3.png"),
    pygame.image.load("superhitmuiscnote4.png"),
    pygame.image.load("superhitmuiscnote5.png"),
    pygame.image.load("superhitmuiscnote6.png"),
    pygame.image.load("superhitmuiscnote7.png"),
    pygame.image.load("superhitmuiscnote8.png"),
    pygame.image.load("superhitmuiscnote9.png"),
    pygame.image.load("superhitmuiscnote10.png"),
    pygame.image.load("superhitmuiscnote11.png"),
    pygame.image.load("superhitmuiscnote12.png"),
    pygame.image.load("superhitmuiscnote13.png"),
    pygame.image.load("superhitmuiscnote14.png"),
    pygame.image.load("superhitmuiscnote15.png"),
    pygame.image.load("superhitmuiscnote16.png"),
    pygame.image.load("superhitmuiscnote17.png"),
    pygame.image.load("superhitmuiscnote18.png"),
    pygame.image.load("superhitmuiscnote19.png"),
    pygame.image.load("superhitmuiscnote20.png"),
    pygame.image.load("superhitmuiscnote21.png"),
    pygame.image.load("superhitmuiscnote22.png"),
    pygame.image.load("superhitmuiscnote23.png"),
    pygame.image.load("superhitmuiscnote24.png"),
    pygame.image.load("invs.png")
]

aroundsuper = [
    pygame.image.load("invs.png"),
    pygame.image.load("aroundsuper.png"),
    pygame.image.load("aroundsuper2.png"),
    pygame.image.load("aroundsuper3.png"),
    pygame.image.load("aroundsuper4.png"),
    pygame.image.load("aroundsuper5.png"),
    pygame.image.load("aroundsuper6.png"),
    pygame.image.load("aroundsuper7.png"),
    pygame.image.load("aroundsuper8.png"),
    pygame.image.load("aroundsuper9.png"),
    pygame.image.load("aroundsuper10.png"),
    pygame.image.load("aroundsuper11.png"),
    pygame.image.load("aroundsuper12.png"),
    pygame.image.load("aroundsuper13.png"),
    pygame.image.load("aroundsuper14.png"),
    pygame.image.load("aroundsuper15.png"),
    pygame.image.load("aroundsuper16.png"),
    pygame.image.load("aroundsuper17.png"),
    pygame.image.load("aroundsuper18.png"),
    pygame.image.load("aroundsuper19.png"),
    pygame.image.load("aroundsuper20.png"),
    pygame.image.load("aroundsuper21.png"),
    pygame.image.load("aroundsuper22.png"),
    pygame.image.load("aroundsuper23.png"),
    pygame.image.load("aroundsuper24.png"),
    pygame.image.load("aroundsuper25.png"),
    pygame.image.load("aroundsuper26.png"),
    pygame.image.load("aroundsuper27.png"),
    pygame.image.load("aroundsuper28.png"),
    pygame.image.load("aroundsuper29.png"),
    pygame.image.load("aroundsuper30.png"),
    pygame.image.load("aroundsuper31.png"),
    pygame.image.load("aroundsuper32.png"),
    pygame.image.load("aroundsuper33.png"),
    pygame.image.load("aroundsuper34.png"),
    pygame.image.load("aroundsuper35.png"),
    pygame.image.load("aroundsuper36.png"),
    pygame.image.load("aroundsuper37.png"),
    pygame.image.load("aroundsuper38.png"),
    pygame.image.load("aroundsuper39.png"),
    pygame.image.load("aroundsuper40.png"),
    pygame.image.load("invs.png"),
]

# var
x, y = 50, 580
vel = 10
isjump = False
jumpcount = 13
left, right = False, False
walkcount = 0
index2 = 0
playing = False
index = 0
index6=0
jumping_animation = False
falling = False
stand_animation = False
superdioanim=False
stand_super=False
timedver = 0
idle_count = 0
standidle_count=0
index3=0
spawncount=0
dioanim_animation=False
diostand=False
index13=0
index14=0
rinfrezze=False
# player2 Rin
rinx,riny = 1750, 540
rinisjump=False
index7=0
rinleft, rinright = False, False
rinwalkcount =0
rinjumpcount = 13
rinfalling = False
rinidle_count = 0
hit_animation=False
rinindex = 0
rinindex2 = 0
rinindex3=0
rinplaying=False
rinjumping_animation=False
numberofhits= 1
throwanim_count=0
index7=0
index9=0
index10=0
index11=0
index12=0
rinthrowanimation=False
rinsuper_animation=False

# health 
BLUE =(145,206,250)
WHITE = (255, 255, 255)
NONE2= (0, 0, 0,255)
GREEN = (76, 175, 80)
YELLOW = (255, 235, 59)
ORANGE = (230, 126, 34)
RED = (244, 67, 54)
RED2=(220,20,60)
diohealth = 900
rinhealth = 900  
max_health = 900
damage_health1 = 900  
damage_health2 = 900 
DAMAGE_RED = (200, 0, 0)  
font = pygame.font.SysFont("Comic Sans MS", 20)

def draw_rounded_rect(surface, color, rect, radius):
    pygame.draw.rect(surface, color, rect, border_radius=radius)


def draw_diohealth_bar(health,damage_health):
    global NONE2

    draw_rounded_rect(win, NONE2, (5, 5, max_health, 20), 10)
    
    if damage_health > health:
        draw_rounded_rect(win, DAMAGE_RED, (5, 5, damage_health, 20), 10)

  
    if health >= 450:
        color = GREEN
    elif health >= 225:
        color = YELLOW
    elif health >= 127:
        color = ORANGE
    else:
        color = RED
    

    draw_rounded_rect(win, color, (5, 5, health, 20), 10)
    

    health_text = str(health) + "/" + str(max_health)
    health_surface = font.render(health_text, True, WHITE)
    name_surface = font.render("Dio Brando", True, BLUE)
    win.blit(name_surface, (30, 25))
    win.blit(health_surface, (175, 20))


def draw_rinhealth_bar(health,damage_health):
    global NONE2
 
    draw_rounded_rect(win, NONE2, (width - max_health - 5, 5, max_health, 20), 10)
    if damage_health > health:
        draw_rounded_rect(win, DAMAGE_RED, (width - damage_health - 5, 5, damage_health, 20), 10)
    
   
    if health >= 450:
        color = GREEN
    elif health >= 225:
        color = YELLOW
    elif health >= 127:
        color = ORANGE
    else:
        color = RED
    

    draw_rounded_rect(win, color, (width - health - 5, 5, health, 20), 10)
    
 
    health_text = str(health) + "/" + str(max_health)
    health_surface = font.render(health_text, True, WHITE)
    name_surface = font.render("Rin Kagamine", True, RED2)
    
    win.blit(name_surface, (width - 160, 25))
    win.blit(health_surface, (width - 300, 20))

draw_diohealth_bar(diohealth,damage_health1)
draw_rinhealth_bar(rinhealth,damage_health2)
# projectile class 
class Projectile:
    global stand,rinhitbox,diostand
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.image_index = 0
        self.hitbox2 = pygame.Rect(self.x, self.y, 402, 348) 
        self.active = True


    def move(self):
        global stand, standleft,numberofhits,diostand,isl,isr,standgoneidle,standidle_left,standidle_right,spawn
        standleft = standgone
        stand = standgone
        standidle_left=standgoneidle
        standidle_right=standgoneidle
        self.x += 15 if self.direction else -15
        self.hitbox2.topleft = (self.x, self.y) 

        if self.x < -50 or self.x > 1900:
            spawn.play()
            standleft = pygame.image.load("zaworldleft.png")
            stand = pygame.image.load("zaworldstand.png")
            standidle_left=isl
            standidle_right=isr
            numberofhits= 0
            diostand= False
            return False
        spawn.stop()
        return True

    def draw(self, win):
        global standleft,rinhitbox,diostand,spawn
        diostand=True
        if self.active:
            
            if self.image_index < len(projectile_images):
                win.blit(projectile_images[self.image_index], (self.x, self.y))
                pygame.draw.rect(win, (0, 0, 0,128), self.hitbox2, 1)  
                self.image_index = (self.image_index + 1) % len(projectile_images)
                pygame.display.update()
        else:
            if self.hitbox2.colliderect(rinhitbox):
                print("Dio has hit")
                self.active = False
                return True  
            return False
    
    def hit2(self):
        global rinhitbox,numberofhits,diostand,hit,riny,rinx,index4,hitsound,rinhealth
       
        rinhitbox = (rinx, riny, 150, 414)  

        if self.hitbox2.colliderect(rinhitbox):
            win.blit(hit[index4], (rinx-225, riny-130))
            pygame.display.update()
            index4 = (index4 + 1) % len(hit)
            hitsound.play()
            rinhealth -= 3
            rinhealth = max(0, rinhealth) 
    
            print("Dio has hit"+ str(numberofhits))
            hitsound.play(loops=-1)
            numberofhits+= 1
  
            
            return True 
        index4=0
        hitsound.stop()
        return False

class Projectile2:
    global stand,standleft,rinhitbox,standidle_left
    def __init__(self, x, y, direction2):
        self.x = x
        self.y = y
        self.direction2 = direction2
        self.image_index2 = 0
        self.hitbox2 = pygame.Rect(self.x, self.y, 402, 348)  
        self.active = True

    def move2(self):
        global stand,standleft,numberofhits,diostand,standidle_left,standidle_right,isl,isr,standgoneidle,spawn
        stand = standgone
        standleft = standgone
        standidle_left=standgoneidle
        standidle_right=standgoneidle
        self.x += 15 if self.direction2 else -15
        self.hitbox2.topleft = (self.x, self.y) 

        if self.x < -50 or self.x > 1900:
            spawn.play()
            stand = pygame.image.load("zaworldstand.png")
            standleft = pygame.image.load("zaworldleft.png")
            standidle_left=isl
            standidle_right=isr
            numberofhits= 0
            diostand= False

    
            return False
        spawn.stop()
        return True

    def draw2(self, win):
        global stand,rinhitbox,diostand
        diostand= True
        if self.active:
            
            if self.image_index2 < len(projectile_images2):
                win.blit(projectile_images2[self.image_index2], (self.x, self.y))
                pygame.draw.rect(win, (0, 0, 0,128), self.hitbox2, 1)  
                self.image_index2 = (self.image_index2 + 1) % len(projectile_images2)
                pygame.display.update()
        else:
            if self.hitbox2.colliderect(rinhitbox):
                print("Dio has hit")
                hitsound.play(loops=-1)
                self.active = False
                return True  
            hitsound.stop()
            return False

    def hit2(self):
        global rinhitbox,numberofhits,diostand,rinx,riny,hit,index4,hitsound,rinhealth
        
        rinhitbox = (rinx, riny, 150, 414) 

        if self.hitbox2.colliderect(rinhitbox):
            win.blit(hit[index4], (rinx-225, riny-130))
            pygame.display.update()
            index4 = (index4 + 1) % len(hit)
            rinhealth -= 3
            rinhealth = max(0, rinhealth) 
            
            print("Dio has hit"+ str(numberofhits))
            hitsound.play(loops=-1)
            numberofhits+= 1

            #I think she hit 40 times
            return True  
        index4=0
        hitsound.stop()
        return False



class rinProjectile:
    global stand
    def __init__(self, rinx, reny, rendirection):
        self.renx = rinx
        self.reny = reny-35
        self.rendirection = rendirection
        self.renimage_index = 0
        self.renhitbox2 = pygame.Rect(self.renx, self.reny, 432, 484)  
        self.active = True
 

    def move(self):
        global numberofhits
        
        self.renx += 15 if self.rendirection else -15
        self.renhitbox2.topleft = (self.renx, self.reny) 

        if self.renx < -50 or self.renx > 1900:
            numberofhits= 0

            return False
        return True

    def draw(self, win):
        if self.active:
            if self.renimage_index < len(rinprojectile_images):
                win.blit(rinprojectile_images[self.renimage_index], (self.renx, self.reny))
                pygame.draw.rect(win, (0, 0, 0,128), self.renhitbox2, 1) 
                self.renimage_index = (self.renimage_index + 1) % len(rinprojectile_images)
                pygame.display.update()
        else:
            if self.renhitbox2.colliderect(hitbox2):
                print("rin has hit")
                
                self.active = False
                return True 
            return False

    
    def hit(self):
        global hitbox2,numberofhits,hit,x,y,index4,rinhitsound,diohealth
       
        hitbox2 = pygame.Rect(x, y, 170, 378)  

        if self.renhitbox2.colliderect(hitbox2):
            
            print("rin has hit"+ str(numberofhits))
            diohealth -= 3
            diohealth = max(0, diohealth) 
            
            rinhitsound.play()
            numberofhits+= 1
            win.blit(hit[index4], (x-225, y-130))
            pygame.display.update()
            index4 = (index4 + 1) % len(hit)
            #I think she hit 40 times
            return True  
        return False
class rinProjectile2:
    global hitbox2

    def __init__(self, rinx, riny, rindirection2,):
        global hitbox2
        self.rinx = rinx
        self.riny = riny-35
        self.rindirection2 = rindirection2
        self.image_index2 = 0
        self.renhitbox2 = pygame.Rect(self.rinx, self.riny, 432, 484)  
        self.active = True
        

 

    def move2(self):
        global numberofhits
        if not self.active:  
            return True 
        self.rinx += 15 if self.rindirection2 else -15
        self.renhitbox2.topleft = (self.rinx, self.riny)  
        if self.rinx < -50 or self.rinx > 1900:
            numberofhits= 0

            return False
        return True

    def draw2(self, win):
        global index4,hit,x,y,rinhitsound,diohealth
        if self.active:
            if self.image_index2 < len(rinprojectile_images2):
                win.blit(rinprojectile_images2[self.image_index2], (self.rinx, self.riny))
                pygame.draw.rect(win, (0, 0, 0,128), self.renhitbox2, 1) 
                self.image_index2 = (self.image_index2 + 1) % len(rinprojectile_images2)
                
                pygame.display.update()
        else:
            if self.renhitbox2.colliderect(hitbox2):
                print("rin has hit")
                diohealth -= 3
                diohealth = max(0, diohealth) 
                rinhitsound.play()
                self.active = False
                win.blit(hit[index4], (x-225, y-130))
                pygame.display.update()
                index4 = (index4 + 1) % len(hit)
                return True 
            return False


    def hit(self):
        global hitbox2,numberofhits,index4,hit,rinhitsound,diohealth
        
        hitbox2 = pygame.Rect(x, y, 170, 378) 

        if self.renhitbox2.colliderect(hitbox2):
            
            print("rin has hit"+ str(numberofhits))
            diohealth -= 5
            diohealth = max(0, diohealth) 
            win.blit(hit[index4], (x-225, y-130))
            rinhitsound.play()
            numberofhits+= 1
            index4 = (index4 + 1) % len(hit)
            #I think she hit 40 times
            return True  
        index4=0
        return False
   



projectiles = []
projectiles2 = []
rinprojectiles = []
rinprojectiles2 = []
rinpic= standgone
spire_image = standgone
dio=standgone
projectile2 = Projectile2(999, 999, char == char_right)
rinprojectile2 = rinProjectile2(999,999, rin == rin_right)
rinprojectile = rinProjectile(999,999, rin == rin_right)

def check_collision(rect1, rect2):

    x1, y1, width1, height1 = rect1
    x2, y2, width2, height2 = rect2
    

    if (x1 < x2 + width2 and x1 + width1 > x2 and
        y1 < y2 + height2 and y1 + height1 > y2):
        return True 
    return False  

def check():
    global numberofhits,hitboxstand,rinhitbox,riny,rinx,hit,index4,rinhealth
    pygame.display.update()

    if check_collision(hitboxstand,rinhitbox):
        hitsound.play()
        win.blit(hit[index4], (rinx-225, riny-130))
        
        pygame.display.update()
        
        index4 = (index4 + 1) % len(hit)

        
        
        numberofhits += 1
        print("Dio has hit"+ str(numberofhits))
        rinhealth -= 1
        rinhealth = max(0, rinhealth) 
        time.sleep(0.05) 




def check2():
    global numberofhits,hitboxstand,rinhitbox,riny,rinx,hit,index4,rinhealth,rinfrezze
    pygame.display.update()

    if check_collision(hitboxstandleft,rinhitbox):
        hitsound.play()
        win.blit(hit[index4], (rinx-225, riny-130))
        pygame.display.update()
        index4 = (index4 + 1) % len(hit)
        
        numberofhits += 1
        rinhealth -= 1
        rinhealth = max(0, rinhealth) 
        print("Dio has hit"+ str(numberofhits))

        time.sleep(0.05) 




def update_stand_image():
    global standidle_left, standidle_count, standidle_right, index13, stand_animation, char, char_right, char_left
    global spire_image, index3, stand, standleft, diostand, numberofhits, rinhitbox, hitboxstand, hitboxstandleft,index2,muitairhit
    global idle_count  

    if stand_animation:
        if not diostand:
            muitairhit.play()
      
            if char == char_left:

                win.blit(standkickleft[index2], (x - 350, y)) 
                pygame.draw.rect(win, (0, 0, 0,128), hitboxstandleft, 1)  
                check2()
                pygame.display.update()

         
            elif char == char_right:

                win.blit(standkick[index2], (x + 170, y)) 
                pygame.draw.rect(win, (0, 0, 0,128), hitboxstand, 1) 
                check()
                pygame.display.update()

      
            index2 = (index2 + 1) % len(standkick)

        else:
            pygame.draw.rect(win, (0, 0, 0,128), rinhitbox, 1)


        if index2 == 0:
            stand_animation = False 
            standleft = pygame.image.load("zaworldleft.png")
            standidle_left = isl
            stand = pygame.image.load("zaworldstand.png")
            standidle_right = isr
            numberofhits = 0
            muitairhit.stop()
            pygame.display.update()
    

    pygame.display.update()

def check3():
    global numberofhits,mudapunchhit,rinhitbox,riny,rinx,hit,index4,rinhealth
    pygame.display.update()

    if check_collision(mudapunchhit,rinhitbox):
        hitsound.play()
        win.blit(hit[index4], (rinx-225, riny-130))
        
        pygame.display.update()
        
        index4 = (index4 + 1) % len(hit)

        
        
        numberofhits += 1
        print("Dio has hit"+ str(numberofhits))
        rinhealth -= 1
        rinhealth = max(0, rinhealth) 
        time.sleep(0.05) 




def check4():
    global numberofhits,mudapunchhitleft,rinhitbox,riny,rinx,hit,index4,rinhealth,rinfrezze
    pygame.display.update()

    if check_collision(mudapunchhitleft,rinhitbox):
        hitsound.play()
        win.blit(hit[index4], (rinx-225, riny-130))
        pygame.display.update()
        index4 = (index4 + 1) % len(hit)
        
        numberofhits += 1
        rinhealth -= 1
        rinhealth = max(0, rinhealth) 
        
        print("Dio has hit"+ str(numberofhits))
        time.sleep(0.05)



def update_stand_super():
    global standidle_left, standidle_count, standidle_right, index2, stand_animation, char, char_right, char_left
    global spire_image, index3, stand, standleft, diostand, numberofhits, rinhitbox, mudapunchhit, mudapunchhitleft,stand_super,index13,muitairhit
    global idle_count,rinfrezze  

    if stand_super:
        if not diostand:
            muitairhit.play()
       
            if char == char_left:

                win.blit(mudapunchleft[index13], (x - 500, y-100))  
                pygame.draw.rect(win, (0, 0, 0,128), mudapunchhitleft, 1) 
                check4()
                pygame.display.update()

      
            elif char == char_right:

                win.blit(mudapunching[index13], (x + 170, y-100))  
                pygame.draw.rect(win, (0, 0, 0,128), mudapunchhit, 1)  
                check3()
                pygame.display.update()

            index13 = (index13 + 1) % len(mudapunching)

        else:
            pygame.draw.rect(win, (0, 0, 0,128), rinhitbox, 1)

   
        if index13 == 0:
            stand_super = False 
            standleft = pygame.image.load("zaworldleft.png")
            standidle_left = isl
            stand = pygame.image.load("zaworldstand.png")
            standidle_right = isr
            numberofhits = 0
            muitairhit.stop()
            rinfrezze=False
            pygame.display.update()
    

    pygame.display.update()

def update_dioanim_image():
    global  dioanim_animation, char, char_right, char_left,spire_image,index3

    if dioanim_animation:

        if char == char_left:


            win.blit(dioanimleft[index3], (x , y))
        else:

            win.blit(dioanim[index3], (x , y))

 
        index3 = (index3 + 1) % len(dioanim)  

        if index3 == 0:

            dioanim_animation = False 
  

            pygame.display.update()

def update_jump_image():
    global index, playing, jumping_animation, char_right, char_left,diogoneidle,idle_right,idle_left,index6

    if playing:
        if char == char_right: 

            
            win.blit(jump[index], (x, y))
            index = (index + 1) % len(jump)
            if index == 0:  
                playing = jumping_animation = False

                win.blit(fall[2], (x, y))
               

        else:
            win.blit(jumpleft[index], (x, y))
            index = (index + 1) % len(jumpleft)
            if index == 0:  
                playing = jumping_animation = False

                win.blit(fallleft[2], (x, y))
            
#rin
def rinupdate_jump_image():
    global rinindex, rinplaying, rinjumping_animation, rin_right, rin_left 
    if rinplaying: 
        if rin == rin_right:  
            win.blit(rinjump[rinindex], (rinx, riny))
            rinindex = (rinindex + 1) % len(rinjump)
            if rinindex == 0:  
                rinplaying = rinjumping_animation = False
                win.blit(rinfall[2], (rinx, riny)) 
        else: 
            win.blit(rinjumpleft[rinindex], (rinx, riny))
            rinindex = (rinindex + 1) % len(rinjumpleft)
            if rinindex == 0:  
                rinplaying = rinjumping_animation = False
                win.blit(rinfallleft[2], (rinx, riny)) 

def rinupdate_throwanim_image():
    global rinindex3, rinthrowanimation, rin, rin_right, rin_left, last_frame_update_time

    animation_delay = 50

    current_time = pygame.time.get_ticks()
    if current_time - last_frame_update_time >= animation_delay:
        last_frame_update_time = current_time  

        if rinthrowanimation:
            lastanim = pygame.image.load("cheer3.png")
            
 
            if rin == rin_left:
                win.blit(throwanimleft[rinindex3], (rinx, riny))
            else:
                win.blit(throwanim[rinindex3], (rinx, riny))

      
            rinindex3 = (rinindex3 + 1) % len(throwanim)

  
            if rinindex3 == 0:
                rinthrowanimation = False
                win.blit(lastanim, (rinx, riny))
                lastanim = standgone
            
        


            pygame.display.update()

def rincheck():
    global numberofhits,hitboxstand,rinhitbox,riny,rinx,yellowhit,index8,diohealth


    if check_collision(rinhitboxpunch,hitbox):
        rinhitsound.play()
        win.blit(yellowhit[index8], (x-225, y-130))
        
        pygame.display.update()
        
        index8 = (index8 + 1) % len(yellowhit)

        
        
        numberofhits += 1
        print("Rin has hit"+ str(numberofhits))
        diohealth -= 1
        diohealth = max(0, diohealth) 
        time.sleep(0.05) 

def rincheck2():
    global numberofhits,hitboxstand,rinhitbox,riny,rinx,yellowhit,index8,diohealth

    if check_collision(rinhitboxpunchleft,hitbox):
        rinhitsound.play()
        win.blit(yellowhit[index8], (x-225, y-130))
        
        pygame.display.update()
        
        index8 = (index8 + 1) % len(yellowhit)
        diohealth -= 1
        diohealth = max(0, diohealth) 
        
        
        numberofhits += 1
        print("Rin has hit"+ str(numberofhits))
        time.sleep(0.05) 

def rincheck3():
    global numberofhits,hitboxstand,rinhitbox,riny,rinx,rinsuperhit,index10,rinsuperhitbox,hitbox,index11,diohealth,damage_health1,damage_health2

    if check_collision(rinsuperhitbox,hitbox):
        rinhitsound.play()
        win.blit(rinsuperhit[index10], (x-125, y-130))
        win.blit(superhitmuiscnote[index11], (x, y))
        pygame.display.update()
        
        index10 = (index10 + 2) % len(rinsuperhit)
        index11 = (index11 + 2) % len(superhitmuiscnote)

        diohealth -= 1
        diohealth = max(0, diohealth)


        
        
        numberofhits += 1
        print("Rin has hit"+ str(numberofhits))



def update_rin_hit():
    global hit_animation,numberofhits,rinx,riny,index7,rin_left,rin_right,rin
    

    

    if hit_animation:

        if rin == rin_left:
            win.blit(rin_hitleft[index7], (rinx-150 , riny))  
            pygame.draw.rect(win, (0, 0, 0, 128), rinhitboxpunchleft, 1)  
            rincheck2()


    
        elif rin == rin_right:
            win.blit(rin_hit[index7], (rinx+50 , riny)) 
            pygame.draw.rect(win, (0, 0, 0, 128), rinhitboxpunch, 1) 
            rincheck()


        index7 = (index7 + 1) % len(rin_hitleft)

    pygame.draw.rect(win, (0, 0, 0, 128), rinhitbox, 1)

    if index7 == 0:
        hit_animation = False 
        numberofhits = 0
        pygame.display.update()

def update_rin_super():
    global rinsuper_animation,numberofhits,rinx,riny,index9,rin_left,rin_right,rin,index12,damage_health1,damage_health2,diohealth,rinhealth

    
    
    

    if rinsuper_animation:
  
        if rin == rin_left:
            win.blit(aroundsuper[index12], (rinx-350 , riny))
            win.blit(rindance[index9], (rinx , riny))
           
            pygame.draw.rect(win, (0, 0, 0, 128), rinsuperhitbox, 1)  
            rincheck3()
        elif rin == rin_right:
            win.blit(aroundsuper[index12], (rinx-350 , riny))
            win.blit(rindance[index9], (rinx , riny))  

            pygame.draw.rect(win, (0, 0, 0, 128), rinsuperhitbox, 1) 
            rincheck3()
        time.sleep(0.05)   
        index9 = (index9 + 1) % len(rindance)
        index12 = (index12 + 1) % len(aroundsuper)




    if index9 == 0:
        rinsuper_animation = False 
        numberofhits = 0
        mm.set_volume(1)
        pygame.display.update()


def redraw_game_window():
    global rinfrezze,timedver,index14,superdioanim,index14,damage_health2,damage_health1,mudapunchhit,mudapunchhitleft,index13,stand_super,rinhealth,diohealth,index9,rinsuper_animation,hit_animation,standidle_count,walkcount, idle_count, left, right, jumping_animation, spire_image, hitbox,rin,rinx,riny,rinidle_count,rinidle_right,rinidle_left,rinwalkcount,rinpic,rinhitbox,throwanim_count,dioanim_animation,hitboxstand,hitboxstandleft,rinhitboxpunch,rinhitboxpunchleft,rinsuperhitbox
    win.blit(bg, (0, 1))

    if damage_health1 > diohealth:
        damage_health1 -= 1  
    if damage_health2 > rinhealth:
        damage_health2 -= 1  
    draw_diohealth_bar(diohealth,damage_health1)
    draw_rinhealth_bar(rinhealth,damage_health2)
    #dio
    if jumping_animation:
        update_jump_image()  

    elif falling:
        if char == char_right:
            win.blit(fall[2], (x, y)) 
            
        else:
            win.blit(fallleft[2], (x, y))  

    elif stand_animation:
        if diostand==False:
            if char == char_left:
                win.blit(standkickleft[index2], (x - 350, y))
                win.blit(idle_left[idle_count // 10 % len(idle_left)], (x, y))   




            else:
                      
                win.blit(idle_right[idle_count // 10 % len(idle_right)], (x, y))

            
                win.blit(standkick[index2], (x + 170, y))
            idle_count += 1
    elif superdioanim:
        rinfrezze=True
        if char == char_right:
            win.blit(dioreading[index14], (x, y))
            index14 = (index14 + 1) % len(dioreading)
        else:
            win.blit(dioreadingleft[index14], (x, y))
            index14 = (index14 + 1) % len(dioreading)

        if index14==0:
            superdioanim=False          
            time.sleep(1)
            stand_super = True
            
            index13 = 0
            if timedver <= 0:
                muda.stop()
                muda.play()
            timedver = (timedver + 1) % 7
            
            if timedver ==1:
                timedver=0

    elif stand_super:
        if diostand==False:
            if char == char_left:
                win.blit(mudapunchleft[index13], (x - 500, y-100)) 
                win.blit(idle_left[idle_count // 10 % len(idle_left)], (x, y))   




            else:
                      
                win.blit(idle_right[idle_count // 10 % len(idle_right)], (x, y))

            
                win.blit(mudapunching[index13], (x + 170, y-100))
            idle_count += 1


    
        
    

            
    elif dioanim_animation:
        if char == char_left:
            win.blit(dioanimleft[index3], (x , y))

        else:
            win.blit(dioanim[index3], (x , y))

    elif left or right:
        if left:
            win.blit(walkLeft[walkcount // 10 % len(walkLeft)], (x, y))
            
 


        elif right:
            win.blit(walkRight[walkcount // 10 % len(walkRight)], (x, y))
 



        walkcount += 1
        

    
    else:


        # dio idle animation
        if char == char_right:
            win.blit(idle_right[idle_count // 10 % len(idle_right)], (x, y))
            win.blit(standidle_right[standidle_count // 10 % len(standidle_right)], (x+170, y-40))
            
                
        else:
            win.blit(idle_left[idle_count // 10 % len(idle_left)], (x, y))   
            win.blit(standidle_left[standidle_count // 10 % len(standidle_left)], (x-250, y-40))   
                    
            
        idle_count += 1
        standidle_count += 1

        
    #rin
        
    if rinjumping_animation:
        rinupdate_jump_image()  
    elif rinfalling:
        if rin == rin_right:
            win.blit(rinfall[2], (rinx, riny))  
            
        else:
            win.blit(rinfallleft[2], (rinx, riny))  
    
    elif rinsuper_animation:
        win.blit(aroundsuper[index12], (rinx-350 , riny))
        win.blit(rindance[index9], (rinx , riny))

 

    elif hit_animation:
        if rin==rin_left:
            win.blit(rin_hitleft[index7], (rinx -150, riny))
        else:
            win.blit(rin_hit[index7], (rinx+50 , riny))
    

    
    elif rinthrowanimation:  
        if rin == rin_left:
            win.blit(throwanimleft[rinindex3], (rinx, riny))
        else:
            win.blit(throwanim[rinindex3], (rinx, riny))

    elif rinleft or rinright :
        if rinleft:
            win.blit(rinwalkLeft[rinwalkcount // 10 % len(rinwalkLeft)], (rinx, riny))

        elif rinright:
            win.blit(rinwalkRight[rinwalkcount // 10 % len(rinwalkRight)], (rinx, riny))

        rinwalkcount += 1
    

   
    else:
        if rin == rin_right:
            win.blit(rinidle_right[rinidle_count // 10 % len(rinidle_right)], (rinx, riny))

        else:
            win.blit(rinidle_left[rinidle_count // 10 % len(rinidle_left)], (rinx, riny))

        rinidle_count += 1



    # draw projectiles
    for projectile in projectiles:
        projectile.draw(win)
    for projectile2 in projectiles2:
        projectile2.draw2(win)
    
    # hits
    for projectile2 in projectiles2:
        projectile2.hit2()
    
    
    for projectile in projectiles:
        projectile.hit2()
    # rin
    # drawsss
    for rinprojectile in rinprojectiles:
        rinprojectile.draw(win)
    for rinprojectile2 in rinprojectiles2:
        rinprojectile2.draw2(win)
  

    
    #hits
    for rinprojectile2 in rinprojectiles2:
        rinprojectile2.hit()
    
    
    for rinprojectile in rinprojectiles:
        rinprojectile.hit()

  
    hitbox = (x, y, 170, 378)
    #imagesize 264 424
    hitboxstand = (x+200, y, 266, 439)
    hitboxstandleft = (x-250, y, 266, 430)
    #imagesize 606.504
    mudapunchhit=  (x + 170, y-100,608,510)
    mudapunchhitleft=(x - 500, y-100,608,510)
    #diostand 168.372 of imagesize x+2 y+6
    rinhitbox = (rinx, riny, 150, 414)
    rinhitboxpunch = (rinx+50, riny, 270, 490)
    rinhitboxpunchleft = (rinx-150, riny, 270, 478)
    rinsuperhitbox=(0,0,1900, 950)
    #rin stand 148.408 of imagesize x+2 y+6
    win.blit(rinpic, (rinx, riny))
    win.blit(dio, (x, y))
    pygame.draw.rect(win, (0, 0, 0, 128), hitbox, 1)
    pygame.draw.rect(win, (0, 0, 0, 1), rinhitbox, 1)

    pygame.display.update()




#main
run = True
while run:
    if diohealth==0:
        print("\n")
        print("\n")
        print(BOLD4+BLUE4 + "Dio has LOST"+RESET)
        print("\n")
        print(BOLD4+RED4 + "Rin has WON"+RESET)
        print("\n")
        print("\n")
        run = False
    
    if rinhealth==0:
        print("\n")
        print("\n")
        print(BOLD4+BLUE4 + "Rin has LOST"+RESET)
        print("\n")
        print(BOLD4+RED4 + "Dio has WON"+RESET)
        print("\n")
        print("\n")
        run = False


    
    if damage_health1 > diohealth:
        damage_health1 -= 1  
    if damage_health2 > rinhealth:
        damage_health2 -= 1  
    
    draw_diohealth_bar(diohealth,damage_health1)
    draw_rinhealth_bar(rinhealth,damage_health2)
    clock.tick(37)
    last_frame_update_time = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

   

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not isjump and not jumping_animation:
                isjump = True
                playing = jumping_animation = True
                index = 0

                
            if event.key == pygame.K_f and not stand_animation and not diostand:
                if char == char_left:
                    standleft = standgone
                    standidle_left=standgoneidle
                    """pygame.draw.rect(win, (0, 0, 0,128),  hitboxstandleft, 1)"""
                else:
                    
                    stand = standgone
                    standidle_right= standgoneidle
                
                stand_animation = True
                index2 = 0
                
                if timedver <= 0:
                    muda.stop()
                    muda.play()
                timedver = (timedver + 1) % 7
                
                if timedver ==1:
                    timedver=0
            
            if event.key == pygame.K_r and not stand_super and not diostand:
                if char == char_left:
                    standleft = standgone
                    standidle_left=standgoneidle

                    """pygame.draw.rect(win, (0, 0, 0,128),  mudapunchhitleft, 1)"""
                else:
                    
                    stand = standgone
                    standidle_right= standgoneidle

                superintro.play()
                superdioanim=True
                



            
            if event.key == pygame.K_q and not hit_animation :


                hit_animation = True
                index7 = 0
            
            if event.key == pygame.K_c and not rinsuper_animation :
                """pygame.draw.rect(win, (0, 0, 0, 128),  rinsuperhitbox, 1)"""

                rinsuper_animation = True
                index9=0
                index12=0
                rindancesong.play()
                mm.set_volume(0.5)
 
                

            if event.key == pygame.K_e and len(projectiles2) == 0 and len(projectiles) == 0 and not dioanim_animation:
                dioanim_animation=True
                index3=0
                diothrow.play()
  
                if char == char_right:
                    projectile2 = Projectile2(x + 250, y + 20, char == char_right)
                    stand = standgone
                    standidle_right= standgoneidle
                else:
                    projectile = Projectile(x - 250, y + 20, char == char_right)
                    hitbox2 = (x , y, 170, 378)

                    standleft = standgone
                    standidle_left=standgoneidle
                    
                    projectiles.append(projectile)
                    standleft = pygame.image.load("zaworldleft.png")
                    standidle_left=isl
                    stand= pygame.image.load("zaworldstand.png")
                    standidle_right=isr
                projectiles2.append(projectile2)
            

            if event.key == pygame.K_z and len(rinprojectiles2) == 0 and len(rinprojectiles) == 0 and not rinthrowanimation:
                rinindex3=0
                rinthrowanimation= True
                rinthrowsound.play()
  

                if rin == rin_right:

                    rinprojectile2 = rinProjectile2(rinx + 250, riny - 35, rin == rin_right)

                else:
                    rinprojectile = rinProjectile(rinx - 250, riny - 35, rin == rin_right)
                    
                rinprojectiles.append(rinprojectile)

                rinprojectiles2.append(rinprojectile2)
                

            if not rinprojectile2.active:  
                rinprojectile2.reset(rinx + 250 if rin == rin_right else rinx - 250, riny - 35, rin == rin_right)

        if event.type == pygame.KEYUP and event.key == pygame.K_f:
            hitsound.stop()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left, right = True, False
        char = char_left

    elif keys[pygame.K_RIGHT] and x < width - 64 - vel:
        x += vel
        right, left = True, False
        char = char_right
 

    else:
        left = right = False
        walkcount = 0

    if not isjump:
        if keys[pygame.K_UP] and not jumping_animation:
            isjump = True
    else:
        if jumpcount >= -13:
            y -= (jumpcount ** 2) * 0.5 * (1 if jumpcount > 0 else -1)
            falling = jumpcount < 0
            jumpcount -= 1
        else:
            isjump = False
            jumpcount = 13
            falling = False
    
    if keys[pygame.K_d]and rinx < width - 64 - vel and rinfrezze==False:
        rinx += vel
        rinright, rinleft = True, False
        rin = rin_right
    elif keys[pygame.K_a] and rinx > vel and rinfrezze==False:
        rinx -= vel
        rinleft, rinright = True, False
        rin = rin_left
    else:
        rinleft = rinright = False
        rinwalkcount = 0
    if not rinisjump:
        if keys[pygame.K_w] and not rinjumping_animation and rinfrezze==False:
            rinisjump = True

    else:
        if rinjumpcount >= -13:
            riny -= (rinjumpcount ** 2) * 0.5 * (1 if rinjumpcount > 0 else -1)
            rinfalling = rinjumpcount < 0
            rinjumpcount -= 1
        else:
            rinisjump = False
            rinjumpcount = 13
            rinfalling = False

    hitbox = (x , y, 170, 378)  
    rinhitbox = (rinx, riny, 150, 414)

    projectiles = [p for p in projectiles if p.move()]
    projectiles2 = [p2 for p2 in projectiles2 if p2.move2()]
    #rin
    rinprojectiles = [p for p in rinprojectiles if p.move()]
    rinprojectiles2 = [p2 for p2 in rinprojectiles2 if p2.move2()]

    if playing:
        update_jump_image()
    if rinplaying:
        rinupdate_jump_image()
    if stand_animation:

        update_stand_image()
    if hit_animation:
        update_rin_hit()
    if rinsuper_animation:
        update_rin_super()

    if rinthrowanimation:
        rinupdate_throwanim_image()
    if dioanim_animation:
        update_dioanim_image()
    if stand_super:
        update_stand_super()

    

    redraw_game_window()

 
    pygame.draw.rect(win, (0, 0, 0,128), hitbox, 1)
    pygame.draw.rect(win, (0, 0, 0,128), rinhitbox, 1)


 

pygame.quit()
sys.exit()