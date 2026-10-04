from pathlib import Path
S=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text(encoding='utf-8')
def test_public_surface():
 for name in ['open_throttle','request_action','advance_epoch','close_throttle','get_throttle','list_throttles']:assert f'def {name}' in S
def test_consensus_binds_state_fields():
 for value in ['category','canonical_intent','equivalent_prior_indexes','complete equivalent-index set','run_nondet_unsafe']:assert value in S
def test_guards_and_determinism():
 for value in ['DENIED_DUPLICATE','DENIED_QUOTA','APPROVED','authorized agent','expired active epoch']:assert value in S
def test_pinned_runner():assert S.startswith('# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }')
