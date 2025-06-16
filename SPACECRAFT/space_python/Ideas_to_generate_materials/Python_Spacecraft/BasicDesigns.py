import cadquery as cq
#Primitives.basic construction scripts cones, cubes to build something bigger, spaceship,satellite
# create 4 small square bumps on a larger base plate:
#notes, basics
# this workplane is centered at x=0.5,y=0.5, the center of the upper face
s = Workplane().box(1, 1, 1).faces(">Z").workplane()

s = s.center(-0.5, -0.5)  # move the center to the corner
t = s.circle(0.25).extrude(0.2)
assert t.faces().size() == 9  # a cube with a cylindrical nub at the top right corner

# make a single box with lower left corner at origin
s = Workplane().box(1, 2, 3, centered=False)
s = (
    Workplane()
    .box(4, 4, 0.5)
    .faces(">Z")
    .workplane()
    .rect(3, 3, forConstruction=True)
    .vertices()
    .box(0.25, 0.25, 0.25, combine=True)
)
s = (
    Workplane()
    .box(2, 4, 0.5)
    .faces(">Z")
    .workplane()
    .rect(1.5, 3.5, forConstruction=True)
    .vertices()
    .cboreHole(0.125, 0.25, 0.125, depth=None)
)
result = cq.Workplane("XY" ).box(3, 3, 3)
result = cq.Solid.makeCone(3, 1, 3)

#cylinder
result = cq.Workplane("XY" ).cylinder(3, 2)
s = Workplane(Plane.XY())
sPnts = [
    (2.75, 1.5),
    (2.5, 1.75),
    (2.0, 1.5),
    (1.5, 1.0),
    (1.0, 1.25),
    (0.5, 1.0),
    (0, 1.0),
]
r = s.lineTo(3.0, 0).lineTo(3.0, 1.0).spline(sPnts).close()
r = r.extrude(0.5)
# drill a hole in the side
c = Workplane().box(1, 1, 1).faces(">Z").workplane().circle(0.25).cutThruAll()

# now cut it in half sideways
c = c.faces(">Y").workplane(-0.5).split(keepTop=True)
#Workplane.sphere

result = cq.Workplane("XY" ).sphere(3)
#Solid.makeSphere

result = cq.Solid.makeSphere(3, angleDegrees1 = -90, angleDegrees2 =90, angleDegrees3 = 360)
#Solid.makeTorus
result = cq.Solid.makeTorus(3, 1.5)
#Workplane.wedge
result = cq.Workplane("XY" ).wedge(3,3,3,1.5,1.5,1.5,1.5)
CQ(aCube).faces(DirectionMinMaxSelector((0, 0, 1), True))
CQ(aCube).faces(">Z")

# make a single box with lower left corner at origin
s = Workplane().box(1, 2, 3, centered=False)
# create 4 small square bumps on a larger base plate:
s = (
    Workplane()
    .box(4, 4, 0.5)
    .faces(">Z")
    .workplane()
    .rect(3, 3, forConstruction=True)
    .vertices()
    .box(0.25, 0.25, 0.25, combine=True)
)

s = (
    Workplane()
    .box(2, 4, 0.5)
    .faces(">Z")
    .workplane()
    .rect(1.5, 3.5, forConstruction=True)
    .vertices()
    .cboreHole(0.125, 0.25, 0.125, depth=None)
)

# this workplane is centered at x=0.5,y=0.5, the center of the upper face
s = Workplane().box(1, 1, 1).faces(">Z").workplane()

s = s.center(-0.5, -0.5)  # move the center to the corner
t = s.circle(0.25).extrude(0.2)
assert t.faces().size() == 9  # a cube with a cylindrical nub at the top right corner

s = Workplane("XY").box(1, 1, 1).faces("+Z").chamfer(0.1)
s = Workplane("XY").box(1, 1, 1).faces("+Z").chamfer(0.2, 0.1)
s = Workplane().rect(4.0, 4.0, forConstruction=True).vertices().circle(0.25)
s = Workplane().lineTo(1, 0).lineTo(1, 1).close().extrude(0.2)
#arc
result = cq.Sketch().arc((0,3), (1.5,1.5), (0,0))
result = cq.Sketch().circle(4)
result = cq.Sketch().ellipse(4,5)
# this workplane is centered at x=0.5,y=0.5, the center of the upper face
s = Workplane().box(1, 1, 1).faces(">Z").workplane()

s = s.center(-0.5, -0.5)  # move the center to the corner
t = s.circle(0.25).extrude(0.2)
assert t.faces().size() == 9  # a cube with a cylindrical nub at the top right corner
s = Workplane("XY").box(1, 1, 1).faces("+Z").chamfer(0.1)
s = Workplane().rect(4.0, 4.0, forConstruction=True).vertices().circle(0.25)
s = Workplane().circle(2.0).circle(1.0)
s = Workplane().lineTo(1, 0).lineTo(1, 1).close().extrude(0.2)

# The dimensions of the box. These can be modified rather than changing the
# object's code directly.
length = 80.0
height = 60.0
thickness = 10.0
center_hole_dia = 22.0

# Create a box based on the dimensions above and add a 22mm center hole
result = (
    cq.Workplane("XY")
    .box(length, height, thickness)
    .faces(">Z")
    .workplane()
    .hole(center_hole_dia)
)
result = (
    cq.Workplane("front")
    .lineTo(2.0, 0)
    .lineTo(2.0, 1.0)
    .threePointArc((1.0, 1.5), (0.0, 1.0))
    .close()
    .extrude(0.25)
)

#Solid.makeCone
result = cq.Solid.makeCone(3, 1, 3)
result = cq.Workplane("XY" ).rect(3, 3).twistExtrude(2,45)
result = (
    cq.Workplane("XY")
    .box(10,10,5)
    .faces(">Z")
    .cboreHole(2,4,1.5)
)

result = (
    cq.Workplane("front")
    .box(3.0, 4.0, 0.25)
    .pushPoints([(0, 0.75), (0, -0.75)])
    .polygon(6, 1.0)
    .cutThruAll()
)

(L, H, W, t) = (100.0, 20.0, 20.0, 1.0)
pts = [
    (0, H / 2.0),
    (W / 2.0, H / 2.0),
    (W / 2.0, (H / 2.0 - t)),
    (t / 2.0, (H / 2.0 - t)),
    (t / 2.0, (t - H / 2.0)),
    (W / 2.0, (t - H / 2.0)),
    (W / 2.0, H / -2.0),
    (0, H / -2.0),
]
result = cq.Workplane("front").polyline(pts).mirrorY().extrude(L)
result = (
    cq.Workplane("XY")
    .box(10,10,5)
    .faces(">Z")
    .cskHole(2, 4, 82, depth=None)
)

result = cq.Solid.makeSphere(3, angleDegrees1 = -90, angleDegrees2 =90, angleDegrees3 = 360)
result = cq.Solid.makeTorus(3, 1.5)

result = cq.Sketch().circle(4)
result = cq.Sketch().ellipse(4,5)
#poligons optional GPT
pts = [(0,0),(0,4),(2,3) ,(4,4), (4,0)]
result = cq.Sketch().polygon(pts)
result = cq.Sketch().rect(4,4)

result = cq.Workplane("XY" ).circle(3)
result = cq.Edge.makeCircle(3)

result = cq.Workplane("XY" ).ellipse(3,4)
result = cq.Edge.makeEllipse(3,4)

s = (
    Workplane()
    .box(2, 4, 0.5)
    .faces(">Z")
    .workplane()
    .rect(1.5, 3.5, forConstruction=True)
    .vertices()
    .cskHole(0.125, 0.25, 82, depth=None)
)