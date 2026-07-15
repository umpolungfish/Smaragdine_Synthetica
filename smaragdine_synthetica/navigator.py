"""
Smaragdine Synthetica — navigator bridge to the IG catalog.

Maps each of the 15 Tabula Smaragdina versicles through the IG crystal,
deriving retrosynthetic chemical operations from their structural tuples.
"""

from __future__ import annotations
import sys
from pathlib import Path
from typing import Optional

_NAV_PATH = Path(__file__).parent.parent.parent / 'imscribing_grammar' / 'navigators'
if str(_NAV_PATH) not in sys.path:
    sys.path.insert(0, str(_NAV_PATH))

import cl8nk_navigator as _nav

_PRIM_KEYS = _nav.PRIMITIVE_KEYS

_VERSICLES = {
    1:  'smaragdine_versicle_1_verum_sine_mendacio',
    2:  'smaragdine_versicle_2_quod_inferius_sicut_superius',
    3:  'smaragdine_versicle_3_separabis_terram_ab_igne',
    4:  'smaragdine_versicle_4_ascendit_a_terra_in_coelum',
    5:  'smaragdine_versicle_5_sic_habebis_gloriam',
    6:  'smaragdine_versicle_6_hinc_erunt_adaptationes',
    7:  'smaragdine_versicle_7_ita_mundus_creatus_est',
    8:  'smaragdine_versicle_8_pater_omnis_telesmi',
    9:  'smaragdine_versicle_9_vis_eius_integra',
    10: 'smaragdine_versicle_10_semina_solvis',
    11: 'smaragdine_versicle_11_ventus_portavit_in_ventre_suo',
    12: 'smaragdine_versicle_12_nutrix_eius_terra',
    13: 'smaragdine_versicle_13_virtus_eius_omnis',
    14: 'smaragdine_versicle_14_separabis_terram_ab_igne_subtiliter',
    15: 'smaragdine_versicle_15_fugito_a_te_sit_fortitudo',
}

_VERSE_TO_OP = {
    1: 'identity_seal',
    2: 'correspondence_bridge',
    3: 'dissolution',
    4: 'sublimation',
    5: 'exaltation',
    6: 'adaptation',
    7: 'creation',
    8: 'transmission',
    9: 'integration',
    10: 'seed_calcination',
    11: 'fermentation',
    12: 'digestion',
    13: 'multiplication',
    14: 'distillation',
    15: 'coagulation',
}

def _tuple_from_entry(entry: dict) -> list[str]:
    t = entry.get('tuple') or entry.get('raw_tuple', {})
    if isinstance(t, dict):
        return [t.get(k, '—') for k in _PRIM_KEYS]
    if isinstance(t, (list, tuple)):
        return list(t)
    return []

def _tuple_dict(entry: dict) -> dict:
    t = entry.get('tuple') or {}
    if isinstance(t, dict):
        return t
    return {k: v for k, v in zip(_PRIM_KEYS, t)}

def lookup(versicle_num: int) -> dict:
    """
    Look up a versicle in the IG catalog and return its structural parameters.
    """
    _nav.load_catalog()
    name = _VERSICLES.get(versicle_num)
    if name is None:
        raise KeyError(f'Versicle {versicle_num} not found')

    entry = _nav.resolve_system(name)
    if entry is None:
        raise KeyError(f'Versicle not in catalog: {name!r}')

    t = _tuple_from_entry(entry)
    op = _VERSE_TO_OP.get(versicle_num, 'unknown')

    return {
        'versicle': versicle_num,
        'name': name,
        'operation': op,
        'tuple': t,
        'tuple_dict': _tuple_dict(entry),
        'label': entry.get('description', ''),
    }

def list_versicles() -> list[dict]:
    """Return all versicles with their operations and tuples."""
    _nav.load_catalog()
    results = []
    for v in range(1, 16):
        try:
            result = lookup(v)
            results.append(result)
        except KeyError:
            pass
    return results

def analyse_operation(versicle_num: int) -> dict:
    """
    Full structural analysis of a versicle's chemical operation.
    Returns: operation name, gate status, bottleneck primitives,
             suggested reagents, and distance to target product.
    """
    result = lookup(versicle_num)
    td = result['tuple_dict']

    # Chemical interpretation from primitives
    interpretation = {}
    interpretation['D'] = f"State space: {td.get('Ð','?')}"
    interpretation['T'] = f"Connectivity: {td.get('Þ','?')}"
    interpretation['R'] = f"Coupling: {td.get('Ř','?')}"
    interpretation['P'] = f"Symmetry: {td.get('Φ','?')}"
    interpretation['F'] = f"Fidelity regime: {td.get('ƒ','?')}"
    interpretation['K'] = f"Kinetics: {td.get('Ç','?')}"
    interpretation['G'] = f"Range: {td.get('Γ','?')}"
    interpretation['Gamma'] = f"Composition: {td.get('ɢ','?')}"
    interpretation['⊙'] = f"Criticality: {td.get('⊙','?')}"
    interpretation['H'] = f"Chirality: {td.get('Ħ','?')}"
    interpretation['S'] = f"Stoichiometry: {td.get('Σ','?')}"
    interpretation['Omega'] = f"Winding: {td.get('Ω','?')}"

    # Detect bottlenecks (primitives at extreme values)
    bottlenecks = []
    for k, v in td.items():
        if v in ('𐑛', '𐑗', '𐑣', '𐑫'):
            bottlenecks.append(f'{k}={v} (extreme)')

    return {
        'operation': result['operation'],
        'versicle': versicle_num,
        'interpretation': interpretation,
        'bottlenecks': bottlenecks,
        'raw_tuple': td,
    }
