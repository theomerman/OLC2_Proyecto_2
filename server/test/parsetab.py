
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSDIVIDE EQUALS LPAREN MINUS NUMBER PLUS RPAREN TIMESstatement : expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : NUMBER'
    
_lr_action_items = {'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[3,7,3,3,-8,3,3,3,3,-6,7,-2,-3,-4,-5,-7,]),'LPAREN':([0,3,4,6,7,8,9,],[4,4,4,4,4,4,4,]),'NUMBER':([0,3,4,6,7,8,9,],[5,5,5,5,5,5,5,]),'$end':([1,2,5,10,12,13,14,15,16,],[0,-1,-8,-6,-2,-3,-4,-5,-7,]),'PLUS':([2,5,10,11,12,13,14,15,16,],[6,-8,-6,6,-2,-3,-4,-5,-7,]),'TIMES':([2,5,10,11,12,13,14,15,16,],[8,-8,-6,8,8,8,-4,-5,-7,]),'DIVIDE':([2,5,10,11,12,13,14,15,16,],[9,-8,-6,9,9,9,-4,-5,-7,]),'RPAREN':([5,10,11,12,13,14,15,16,],[-8,-6,16,-2,-3,-4,-5,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,3,4,6,7,8,9,],[2,10,11,12,13,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expr','calc.py',61),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','calc.py',72),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','calc.py',73),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','calc.py',74),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','calc.py',75),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','calc.py',91),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','calc.py',100),
  ('expression -> NUMBER','expression',1,'p_expression_number','calc.py',104),
]
