#Live code demo snippets

#snippet I

flowable = Flowable((Mm(0), Mm(0)), None, Mm(500), Mm(30), Mm(10))

staff = Staff((Mm(0), Mm(0)), flowable, Mm(500))
unit = staff.unit
clef = Clef(ZERO, staff, "treble")
KeySignature(ZERO, staff, "g_major")
center = unit(15)

#snippet II

n1 = Chordrest(ZERO, staff, ["c"], (1, 8))
n2 = Chordrest(Mm(35), staff, ["e"], (2, 16))
n3 = Chordrest(Mm(50), staff, ["g"], (3, 4))
n4 = Chordrest(Mm(65), staff, ["a"], (4, 2))




#snippet III

n1.noteheads[0].brush = Brush("#ffff00")
n2.noteheads[0].brush = Brush("#ffff00")
n3.noteheads[0].brush = Brush("#ffff00")
n4.noteheads[0].brush = Brush("#ffff00")


#snippet IV

def refresh_func(sun):
    #start = time.time()
    #while time.time() < start + 5:
        n1.x = center + Mm(math.sin((4*sun)) * 10)
        n2.x = center + Mm(math.sin((sun / 2) + 1) * 12)
        n3.x = center + Mm(math.sin((sun / 2) + 1.7) * 7)
        n4.x = center + Mm(math.sin((sun / 2) + 2.3) * 15)

neoscore.show(refresh_func)


#snippet V

def refresh_func1(sun):
    #start = time.time()
    #while time.time() < start + 5:
        n1.x = center + Mm(math.sin((10*sun)) * 10)
        n2.x = center + Mm(math.sin((10*sun) + 1) * 12)
        n3.x = center + Mm(math.sin((10*sun) + 1.7) * 7)
        n4.x = center + Mm(math.sin((10* sun) + 2.3) * 15)

neoscore.show(refresh_func1)

#snippet VI

def refresh_func2(sun):
    #start = time.time()
    #while time.time() < start + 5:
        n1.x = center + Mm(math.sin((50*sun)) * 10)
        n2.x = center + Mm(math.sin((50*sun) + 1) * 12)
        n3.x = center + Mm(math.sin((50*sun) + 1.7) * 7)
        n4.x = center + Mm(math.sin((50* sun) + 2.3) * 15)

neoscore.show(refresh_func2)


#snippet VII

n1.remove()
n2.remove()
n3.remove()
n4.remove()

#n5 = Path.ellipse((Mm(-45), Mm(10)), None, Mm(-2), Mm(-2), "#ffff00")
#n6 = Path.ellipse((Mm(100), Mm(10)), None, Mm(-2), Mm(-2), "#ffff00")
#n7 = Path.ellipse((Mm(0), Mm(-20)), None, Mm(-2), Mm(-2), "#ffff00")
n8 = Path.ellipse((Mm(0), Mm(20)), None, Mm(-2), Mm(-2), "#ffff00")
n9 = Path.ellipse((Mm(10), Mm(30)), None, Mm(-2), Mm(-2), "#ffff00")
n10 = Path.ellipse((Mm(20), Mm(50)), None, Mm(-2), Mm(-2), "#ffff00")
n11 = Path.ellipse((Mm(30), Mm(60)), None, Mm(-2), Mm(-2), "#ffff00")
#n12 = Path.ellipse((Mm(50), Mm(60)), None, Mm(-2), Mm(-2), "#ffff00")
n13 = Path.ellipse((Mm(65), Mm(65)), None, Mm(-2), Mm(-2), "#ffff00")
#n14 = Path.ellipse((Mm(70), Mm(75)), None, Mm(-2), Mm(-2), "#ffff00")
#n15 = Path.ellipse((Mm(55), Mm(60)), None, Mm(-2), Mm(-2), "#ffff00")
n16 = Path.ellipse((Mm(35), Mm(70)), None, Mm(-2), Mm(-2), "#ffff00")
#n17 = Path.ellipse((Mm(63), Mm(70)), None, Mm(-2), Mm(-2), "#ffff00")
n18 = Path.ellipse((Mm(65), Mm(75)), None, Mm(-2), Mm(-2), "#ffff00")
