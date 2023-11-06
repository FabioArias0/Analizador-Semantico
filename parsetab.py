
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN DIVIDE ID MINUS NUM PLUS TIMES\n    statement : ID ASSIGN expression\n    \n    expression : expression PLUS term\n               | expression MINUS term\n               | term\n    \n    term : term TIMES factor\n         | term DIVIDE factor\n         | factor\n    \n    factor : NUM\n    \n    factor : ID\n    '
    
_lr_action_items = {'ID':([0,3,9,10,11,12,],[2,4,4,4,4,4,]),'$end':([1,4,5,6,7,8,13,14,15,16,],[0,-9,-1,-4,-7,-8,-2,-3,-5,-6,]),'ASSIGN':([2,],[3,]),'NUM':([3,9,10,11,12,],[8,8,8,8,8,]),'TIMES':([4,6,7,8,13,14,15,16,],[-9,11,-7,-8,11,11,-5,-6,]),'DIVIDE':([4,6,7,8,13,14,15,16,],[-9,12,-7,-8,12,12,-5,-6,]),'PLUS':([4,5,6,7,8,13,14,15,16,],[-9,9,-4,-7,-8,-2,-3,-5,-6,]),'MINUS':([4,5,6,7,8,13,14,15,16,],[-9,10,-4,-7,-8,-2,-3,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([3,],[5,]),'term':([3,9,10,],[6,13,14,]),'factor':([3,9,10,11,12,],[7,7,7,15,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> ID ASSIGN expression','statement',3,'p_statement_assign','main.py',54),
  ('expression -> expression PLUS term','expression',3,'p_expression_binop','main.py',60),
  ('expression -> expression MINUS term','expression',3,'p_expression_binop','main.py',61),
  ('expression -> term','expression',1,'p_expression_binop','main.py',62),
  ('term -> term TIMES factor','term',3,'p_term_binop','main.py',74),
  ('term -> term DIVIDE factor','term',3,'p_term_binop','main.py',75),
  ('term -> factor','term',1,'p_term_binop','main.py',76),
  ('factor -> NUM','factor',1,'p_factor_num','main.py',88),
  ('factor -> ID','factor',1,'p_factor_id','main.py',94),
]
