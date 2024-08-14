import pytest
from pint import UnitRegistry
from wqunits import load_units, load_molar_mass


def test_load_units_and_convertion():
    ureg = UnitRegistry()
    load_units(ureg=ureg)

    assert ((1 * ureg.mg_per_g).to(
        ureg.ug_per_g
    ) == 1000 * ureg.ug_per_g)

    m3_per_h = 1 * ureg.m3_per_h
    m3_per_d = m3_per_h.to(ureg.m3_per_d)

    assert m3_per_d.magnitude == pytest.approx(24)


def test_load_molar_mass():

    assert load_molar_mass('H') == 1.00794
    assert load_molar_mass('He') == 4.002602
    assert load_molar_mass('Li') == 6.941
