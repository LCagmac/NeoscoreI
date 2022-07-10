#Starter Code
import neoscore
import math
from threading import Timer
import time
import random
from random import *
import threading
#from helpers import render_example
from neoscore.core import neoscore
from neoscore.core.flowable import Flowable
from neoscore.core.units import ZERO, Mm
from neoscore.western.clef import Clef
from neoscore.western.duration import Duration
from neoscore.western.key_signature import KeySignature
from neoscore.western.notehead import Notehead
from neoscore.western.staff import Staff
from neoscore.western.chordrest import Chordrest
from neoscore.core.color import ColorDef
from neoscore.core.color import Color
from neoscore.core.path import Path
from neoscore.core.brush import Brush
from neoscore.core.neoscore import set_background_brush

neoscore.setup()

flowable = Flowable((Mm(0), Mm(0)), None, Mm(500), Mm(30), Mm(10))

staff = Staff((Mm(0), Mm(0)), flowable, Mm(500))
unit = staff.unit
clef = Clef(ZERO, staff, "treble")
KeySignature(ZERO, staff, "g_major")
center = unit(15)

n1 = Chordrest(ZERO, staff, ["c"], (1, 8))
n2 = Chordrest(Mm(35), staff, ["e"], (2, 16))
n3 = Chordrest(Mm(50), staff, ["g"], (3, 4))
n4 = Chordrest(Mm(65), staff, ["a"], (4, 2))




#snippet III

n1.noteheads[0].brush = Brush("#000000")
n2.noteheads[0].brush = Brush("#000000")
n3.noteheads[0].brush = Brush("#000000")
n4.noteheads[0].brush = Brush("#000000")

colorselect = [	"#f5f5f5", "ebebeb", "e0e0e0", "d6d6d6", "cccccc", "c2c2c2", "b8b8b8", "adadad", "a3a3a3", "999999", "858585",
"7a7a7a", "707070", "666666", "5c5c5c", "525252", "474747", "3d3d3d", "333333", "292929", "1f1f1f", "141414", "0a0a0a", "000000"]

#snippet VI

def colorchange0():
    brush = set_background_brush(colorselect[0])

def colorchange1():
    brush1 = set_background_brush(colorselect[1])
def colorchange2():
    brush2 = set_background_brush(colorselect[2])

def colorchange3():
    brush3 = set_background_brush(colorselect[3])

def colorchange4():
    brush4 = set_background_brush(colorselect[4])
def colorchange5():
    brush5 = set_background_brush(colorselect[5])

def colorchange6():
    brush6 = set_background_brush(colorselect[6])

def colorchange7():
    brush7 = set_background_brush(colorselect[7])
def colorchange8():
    brush8 = set_background_brush(colorselect[8])

def colorchange9():
    brush9 = set_background_brush(colorselect[9])

def colorchange10():
    brush10 = set_background_brush(colorselect[10])

def colorchange11():
    brush11 = set_background_brush(colorselect[11])


def colorchange12():
    brush12 = set_background_brush(colorselect[12])

def colorchange13():
    brush13 = set_background_brush(colorselect[13])

def colorchange14():
    brush14 = set_background_brush(colorselect[14])

def colorchange15():
    brush15 = set_background_brush(colorselect[15])

def colorchange16():
    brush16 = set_background_brush(colorselect[16])

def colorchange17():
    brush17 = set_background_brush(colorselect[17])

def colorchange18():
    brush18 = set_background_brush(colorselect[18])

def colorchange19():
    brush19 = set_background_brush(colorselect[19])

def colorchange20():
    brush20 = set_background_brush(colorselect[20])

def colorchange21():
    brush21 = set_background_brush(colorselect[21])

def colorchange22():
    brush22 = set_background_brush(colorselect[22])

def colorchange23():
    brush23 = set_background_brush(colorselect[23])





t = threading.Timer(1, colorchange0)
t1 = threading.Timer(2, colorchange1)
t2 = threading.Timer(3, colorchange2)
t3 = threading.Timer(4, colorchange3)
t4 = threading.Timer(5, colorchange4)
t5 = threading.Timer(6, colorchange5)
t6 = threading.Timer(7, colorchange6)
t7 = threading.Timer(8, colorchange7)
t8 = threading.Timer(9, colorchange8)
t9 = threading.Timer(10, colorchange9)
t10 = threading.Timer(11, colorchange10)
t11 = threading.Timer(12, colorchange11)
t12 = threading.Timer(13, colorchange12)
t13 = threading.Timer(14, colorchange13)
t14 = threading.Timer(15, colorchange14)
t15 = threading.Timer(16, colorchange15)
t16 = threading.Timer(17, colorchange16)
t17 = threading.Timer(18, colorchange17)
t18 = threading.Timer(19, colorchange18)
t19 = threading.Timer(20, colorchange19)
t20 = threading.Timer(21, colorchange20)
t21 = threading.Timer(22, colorchange21)
t22 = threading.Timer(23, colorchange22)
t23 = threading.Timer(24, colorchange23)

neoscore.show()
