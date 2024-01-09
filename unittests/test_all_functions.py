from cytools import Polytope, Cone, fetch_polytopes

# Here we simply run most functions with most parameter combinations to see if anything crashes

print("Testing polytope functions...")
p = Polytope([[0],[1]])
p = Polytope([[1,1],[2,1]])
p = next(fetch_polytopes(dim=5, h11=100, lattice="N"))
p = next(fetch_polytopes(h11=11, h21=491, lattice="N"))
poly_pts = p.points()
for b in ["ppl", "qhull", "palp"]:
    print(f"Testing {b} backend...")
    p = Polytope(poly_pts, backend=b)
    p.__repr__()
    p == p
    p != p
    hash(p)
    p.minkowski_sum(p)
    p.is_linearly_equivalent(p)
    p.is_affinely_equivalent(p)
    p.ambient_dim()
    p.dim()
    p.is_solid()
    p._pts_saturated()
    p.points()
    p.interior_points()
    p.boundary_points()
    p.points_interior_to_facets()
    p.boundary_points_not_interior_to_facets()
    p.points_not_interior_to_facets()
    p.clear_cache()
    p.points(as_indices=True)
    p.interior_points(as_indices=True)
    p.boundary_points(as_indices=True)
    p.points_interior_to_facets(as_indices=True)
    p.boundary_points_not_interior_to_facets(as_indices=True)
    p.points_not_interior_to_facets(as_indices=True)
    p.is_reflexive()
    p.hpq(0,0,lattice="N")
    p.hpq(0,1,lattice="N")
    p.hpq(1,1,lattice="N")
    p.hpq(1,2,lattice="N")
    p.hpq(2,2,lattice="N")
    p.hpq(0,0,lattice="M")
    p.hpq(0,1,lattice="M")
    p.hpq(1,1,lattice="M")
    p.hpq(1,2,lattice="M")
    p.hpq(2,2,lattice="M")
    p.h11(lattice="N")
    p.h21(lattice="N")
    p.h22(lattice="N")
    p.h31(lattice="N")
    p.h11(lattice="M")
    p.h21(lattice="M")
    p.h22(lattice="M")
    p.h31(lattice="M")
    p.chi(lattice="N")
    p.chi(lattice="M")
    p.clear_cache()
    p._faces4d()
    p.clear_cache()
    p.faces()
    p.clear_cache()
    p.faces(2)
    p.facets()
    p.vertices()
    p.clear_cache()
    p.dual()
    p.is_favorable(lattice="N")
    p.is_favorable(lattice="M")
    p.glsm_charge_matrix()
    p.glsm_charge_matrix(include_points_interior_to_facets=True)
    p.glsm_charge_matrix(include_origin=False, include_points_interior_to_facets=True)
    p.glsm_linear_relations()
    p.glsm_linear_relations(include_points_interior_to_facets=True)
    p.glsm_linear_relations(include_origin=False, include_points_interior_to_facets=True)
    p.glsm_basis()
    p.glsm_basis(include_points_interior_to_facets=True)
    p.glsm_basis(include_origin=False, include_points_interior_to_facets=True)
    p.volume()
    p.points_to_indices(p.boundary_points()[0])
    p.points_to_indices(p.boundary_points())
    p.normal_form(backend="palp")
    p.normal_form(affine_transform=True)
    g = p.random_triangulations_fast(N=2, c=1, seed=0)
    next(g)
    next(g)
    g = p.random_triangulations_fair(N=2, seed=0)
    next(g)
    next(g)
    p.all_triangulations()
    p.automorphisms()
    p.automorphisms(square_to_one=True)
    p.find_2d_reflexive_subpolytopes()

print("Testing triangulation functions...")
p = Polytope(poly_pts)
for b in ["cgal", "qhull", "topcom"]:
    print(f"Testing {b} backend...")
    p.triangulate(backend=b)
    p.triangulate(backend=b, make_star=False)
    p.triangulate(backend=b, include_points_interior_to_facets=True)
    p.triangulate(backend=b, make_star=False)
    p.triangulate(backend=b, heights=[-9.2,2.7,2.7,4.5,4.6,5.4,2.2,-0.5,-2.2,-1.7,-2.8,-1.7,-2.5,-1.5,-1.2,1.2], verbosity=0)
    p.triangulate(backend=b, heights=[10,2,2,4,4,5,2,0,-2,-1,-2,-1,-2,-1,-1,1], verbosity=0)
    t = p.triangulate(backend=b, simplices=[[0,1,3,4,5],[0,1,3,4,15],[0,1,3,5,15],[0,1,4,5,13],[0,1,4,13,15],[0,1,5,11,13],[0,1,5,11,14],[0,1,5,14,15],[0,1,6,7,9],[0,1,6,7,11],[0,1,6,9,11],[0,1,7,8,9],[0,1,7,8,11],[0,1,8,9,10],[0,1,8,10,11],[0,1,9,10,13],[0,1,9,11,13],[0,1,10,11,12],[0,1,10,12,13],[0,1,11,12,14],[0,1,12,13,14],[0,1,13,14,15],[0,2,3,4,5],[0,2,3,4,15],[0,2,3,5,15],[0,2,4,5,13],[0,2,4,13,15],[0,2,5,11,13],[0,2,5,11,14],[0,2,5,14,15],[0,2,6,7,9],[0,2,6,7,11],[0,2,6,9,11],[0,2,7,8,9],[0,2,7,8,11],[0,2,8,9,10],[0,2,8,10,11],[0,2,9,10,13],[0,2,9,11,13],[0,2,10,11,12],[0,2,10,12,13],[0,2,11,12,14],[0,2,12,13,14],[0,2,13,14,15]])
    t.__repr__()
    t == t
    t != t
    hash(t)
    t.polytope()
    t.points()
    t.points_to_indices(t.points()[0])
    t.points_to_indices(t.points())
    t.simplices()
    t.dim()
    t.is_fine()
    t.is_regular()
    t.is_star()
    t.is_valid()
    t.gkz_phi()
    t.random_flips(2)
    t.neighbor_triangulations()
    t.sr_ideal()
    t.secondary_cone()
    t.is_equivalent(t)
    t.automorphism_orbit()

print("Testing ToricVariety functions...")
t = p.triangulate()
tv = t.get_toric_variety()
tv.__repr__()
tv == tv
tv != tv
hash(tv)
tv.canonical_divisor_is_smooth()
tv.curve_basis()
tv.dim()
tv.divisor_basis()
tv.effective_cone()
tv.fan_cones()
tv.get_cy()
tv.is_compact()
tv.is_smooth()
tv.prime_toric_divisors()

print("Testing CalabiYau functions...")
t = p.triangulate()
cy = t.get_cy()
cy.__repr__()
cy == cy
cy != cy
hash(cy)
cy.is_trivially_equivalent(cy)
cy.triangulation()
cy.polytope()
cy.ambient_dim()
cy.dim()
cy.hpq(1,1)
cy.h11()
cy.h12()
cy.h13()
cy.chi()
cy.glsm_charge_matrix()
cy.glsm_linear_relations()
cy.divisor_basis()
cy.set_divisor_basis(cy.divisor_basis())
cy.set_curve_basis(cy.divisor_basis())
cy.toric_mori_cone(in_basis=False)
cy.toric_mori_cone(in_basis=True)
cy.clear_cache()
cy.toric_kahler_cone()
cy.intersection_numbers(in_basis=False)
cy.intersection_numbers(in_basis=True)
cy.intersection_numbers(in_basis=False, zero_as_anticanonical=True)
cy.second_chern_class(in_basis=False)
cy.second_chern_class(in_basis=True)
cy.is_smooth()
cy.toric_effective_cone()
d = cy.toric_kahler_cone().tip_of_stretched_cone(1)
cy.compute_cy_volume(d)
cy.compute_divisor_volumes(d)
cy.compute_kappa_matrix(d)
cy.compute_kappa_vector(d)
cy.compute_inverse_kahler_metric(d)
cy.compute_kahler_metric(d)

print("Testing Cone functions...")
c = cy.toric_mori_cone(in_basis=True)
c.__repr__()
c == c
c != c
hash(c)
c.ambient_dim()
c.dim()
c.dual()
c.extremal_rays()
c.find_grading_vector()
c.find_interior_point()
c.dual().find_interior_point()
c.find_lattice_points(min_points=100)
c.hilbert_basis()
c.hyperplanes()
c.intersection(c)
c.is_pointed()
c.is_simplicial()
c.is_smooth()
c.is_solid()
c.rays()
c.tip_of_stretched_cone(1)
