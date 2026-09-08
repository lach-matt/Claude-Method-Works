"""k_inf of the design fuel salt at a stated fissile fraction.

    fissile fraction of heavy metal   0.10000
    UCl3 mol fraction                 0.18910
    density                           3.3000 g/cm3
    temperature                       900 K
    Cl-37 enrichment                  0.990

REFLECTIVE ON EVERY SURFACE: this is an infinite medium and the
number wanted is k_inf. No geometry, no leakage, no reflector, no
blanket -- none of the places two calculations differ for reasons
that are not the question.

    one-group prediction, registered in advance: k_inf = 1.0894
"""
import openmc

salt = openmc.Material(name='NaCl-UCl3 fuel salt')
salt.add_nuclide('Cl35', 2.39006801e-04, 'ao')
salt.add_nuclide('Cl37', 2.36616733e-02, 'ao')
salt.add_nuclide('Na23', 1.40626889e-02, 'ao')
salt.add_nuclide('Pu239', 3.27933041e-04, 'ao')
salt.add_nuclide('U238', 2.95139737e-03, 'ao')
salt.set_density('sum')
salt.temperature = 900.0
materials = openmc.Materials([salt]); materials.export_to_xml()

# a box with reflective faces is an infinite medium
L = 50.0
box = openmc.model.RectangularParallelepiped(
    -L, L, -L, L, -L, L, boundary_type='reflective')
cell = openmc.Cell(fill=salt, region=-box)
openmc.Geometry([cell]).export_to_xml()

settings = openmc.Settings()
settings.run_mode = 'eigenvalue'
settings.particles = 100000
settings.batches = 250
settings.inactive = 50
settings.temperature = {'method': 'interpolation'}
settings.export_to_xml()

openmc.run()
