import pyvista as pv
import numpy as np
from vtkmodules.vtkFiltersModeling import vtkRotationalExtrusionFilter
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import vtkPolyData, vtkCellArray
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersGeneral import vtkTransformPolyDataFilter  # CORRECTO

# Crear perfil tobera (x, r)
x = np.linspace(0, 1.0, 100)
r = np.piecewise(x,
    [x < 0.4, (x >= 0.4) & (x <= 0.6), x > 0.6],
    [lambda x: 0.3 - 0.2 * (x / 0.4),
     0.1,
     lambda x: 0.1 + 0.4 * ((x - 0.6) / 0.4)]
)

# Convertir perfil a vtkPoints (como línea en XY para rotar en Z)
vtk_points = vtkPoints()
lines = vtkCellArray()
for i in range(len(x)):
    vtk_points.InsertNextPoint(x[i], r[i], 0)  # (x, r, 0)

    if i > 0:
        lines.InsertNextCell(2)
        lines.InsertCellPoint(i - 1)
        lines.InsertCellPoint(i)

profile = vtkPolyData()
profile.SetPoints(vtk_points)
profile.SetLines(lines)

# Si quieres rotar el perfil para usar otro eje, puedes aplicar transformación
# Por ejemplo, para rotar el perfil y usar eje X:
# transform = vtkTransform()
# transform.RotateY(90)  # rota 90 grados para poner eje X en Z
# transformFilter = vtkTransformPolyDataFilter()
# transformFilter.SetInputData(profile)
# transformFilter.SetTransform(transform)
# transformFilter.Update()
# profile = transformFilter.GetOutput()

# Extrusión rotacional alrededor del eje Z (default)
extrude = vtkRotationalExtrusionFilter()
extrude.SetInputData(profile)
extrude.SetResolution(180)
extrude.SetAngle(360)
extrude.Update()

# Convertir resultado a PyVista
revolved = pv.wrap(extrude.GetOutput())

# Mostrar
plotter = pv.Plotter()
plotter.add_mesh(revolved, color='lightblue', show_edges=True)
plotter.add_axes()
plotter.show()
