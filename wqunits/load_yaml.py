import yaml
import os
from pathlib import Path
from pint import UnitRegistry

root_dir: Path = os.path.dirname(__file__)


def load_units(ureg: UnitRegistry) -> None:
    """
    Load unit definitions from a YAML file into a Pint UnitRegistry.

    Parameters:
        ureg (UnitRegistry): An instance of Pint's UnitRegistry.
    """
    yaml_file = os.path.join(root_dir, 'libs/wqunits-pint.yaml')

    with open(yaml_file, 'r') as file:
        units_data = yaml.safe_load(file)

    for unit_name, unit_info in units_data.get('Units', {}).items():
        definition = unit_info['definition']
        aliases = unit_info.get('aliases', [])

        if aliases:
            alias_str = " = " + " = ".join(aliases)
        else:
            alias_str = ""

        pint_definition = f"{unit_name} = {definition}{alias_str}"
        ureg.define(pint_definition)


def load_molar_mass(element_symbol: str) -> float | None:
    """
    Reads the molar mass of a particular element from a YAML file.

    The yaml file wit the molar mass data comes 
    from https://github.com/watersync/molecular-data.

    Parameters:
        element_symbol (str): The symbol of the element to 
            look up (e.g., 'H' for Hydrogen).

    Returns:
        float: The molar mass of the element, or None if the element is not found.
    """

    elements_data: Path = os.path.join(root_dir, 'libs/elements.yaml')

    with open(elements_data, 'r') as file:
        elements = yaml.safe_load(file)

    for element in elements:
        if element['symbol'].lower() == element_symbol.lower():
            return element['mass']
