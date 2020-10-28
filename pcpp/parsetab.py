
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCPP_COMMAleftCPP_QUESTIONCPP_COLONleftCPP_LOGICALORleftCPP_LOGICALANDleftCPP_BARleftCPP_HATleftCPP_AMPERSANDleftCPP_EQUALITYCPP_INEQUALITYleftCPP_LESSCPP_LESSEQUALCPP_GREATERCPP_GREATEREQUALleftCPP_LSHIFTCPP_RSHIFTleftCPP_PLUSCPP_MINUSleftCPP_STARCPP_FSLASHCPP_PERCENTrightUPLUSUMINUSCPP_EXCLAMATIONCPP_TILDECPP_AMPERSAND CPP_BAR CPP_CHAR CPP_COLON CPP_COMMA CPP_EQUALITY CPP_EXCLAMATION CPP_FSLASH CPP_GREATER CPP_GREATEREQUAL CPP_HAT CPP_ID CPP_INEQUALITY CPP_INTEGER CPP_LESS CPP_LESSEQUAL CPP_LOGICALAND CPP_LOGICALOR CPP_LPAREN CPP_LSHIFT CPP_MINUS CPP_PERCENT CPP_PLUS CPP_QUESTION CPP_RPAREN CPP_RSHIFT CPP_STAR CPP_TILDEexpression : CPP_INTEGERexpression : CPP_CHARexpression : CPP_LPAREN expression CPP_RPARENexpression : CPP_PLUS expression %prec UPLUSexpression : CPP_MINUS expression %prec UMINUS\n    expression : CPP_EXCLAMATION expression\n              | CPP_TILDE expression\n    \n    expression : expression CPP_STAR expression\n              | expression CPP_FSLASH expression\n              | expression CPP_PERCENT expression\n              | expression CPP_PLUS expression\n              | expression CPP_MINUS expression\n              | expression CPP_LSHIFT expression\n              | expression CPP_RSHIFT expression\n              | expression CPP_LESS expression\n              | expression CPP_LESSEQUAL expression\n              | expression CPP_GREATER expression\n              | expression CPP_GREATEREQUAL expression\n              | expression CPP_EQUALITY expression\n              | expression CPP_INEQUALITY expression\n              | expression CPP_AMPERSAND expression\n              | expression CPP_HAT expression\n              | expression CPP_BAR expression\n              | expression CPP_LOGICALAND expression\n              | expression CPP_LOGICALOR expression\n              | expression CPP_COMMA expression\n    expression : expression CPP_QUESTION expression CPP_COLON expressionexpression : CPP_ID CPP_LPAREN expression CPP_RPARENexpression : CPP_ID'
    
_lr_action_items = {'CPP_ID':([0,2,3,5,7,9,10,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,59,],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]),'CPP_LSHIFT':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,15,-6,-4,15,-5,-7,15,-3,-13,15,15,15,15,-10,15,15,15,-11,15,-9,15,15,-12,-8,15,15,15,-14,-28,15,]),'CPP_LESSEQUAL':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,16,-6,-4,16,-5,-7,16,-3,-13,-16,-18,16,16,-10,16,16,16,-11,16,-9,16,16,-12,-8,16,-17,-15,-14,-28,16,]),'CPP_GREATEREQUAL':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,17,-6,-4,17,-5,-7,17,-3,-13,-16,-18,17,17,-10,17,17,17,-11,17,-9,17,17,-12,-8,17,-17,-15,-14,-28,17,]),'CPP_LOGICALOR':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,18,-6,-4,18,-5,-7,18,-3,-13,-16,-18,-25,-24,-10,-21,18,-23,-11,-20,-9,-19,-22,-12,-8,18,-17,-15,-14,-28,18,]),'CPP_LOGICALAND':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,19,-6,-4,19,-5,-7,19,-3,-13,-16,-18,19,-24,-10,-21,19,-23,-11,-20,-9,-19,-22,-12,-8,19,-17,-15,-14,-28,19,]),'CPP_EXCLAMATION':([0,2,3,5,7,9,10,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,59,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'CPP_PERCENT':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,20,-6,-4,20,-5,-7,20,-3,20,20,20,20,20,-10,20,20,20,20,20,-9,20,20,20,-8,20,20,20,20,-28,20,]),'CPP_AMPERSAND':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,21,-6,-4,21,-5,-7,21,-3,-13,-16,-18,21,21,-10,-21,21,21,-11,-20,-9,-19,21,-12,-8,21,-17,-15,-14,-28,21,]),'CPP_QUESTION':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,22,-6,-4,22,-5,-7,22,-3,-13,-16,-18,-25,-24,-10,-21,22,-23,-11,-20,-9,-19,-22,-12,-8,22,-17,-15,-14,-28,-27,]),'CPP_BAR':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,23,-6,-4,23,-5,-7,23,-3,-13,-16,-18,23,23,-10,-21,23,-23,-11,-20,-9,-19,-22,-12,-8,23,-17,-15,-14,-28,23,]),'$end':([1,4,6,8,11,12,14,35,37,38,39,40,41,42,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,0,-6,-4,-5,-7,-3,-13,-16,-18,-25,-24,-10,-21,-23,-11,-20,-9,-19,-22,-12,-8,-26,-17,-15,-14,-28,-27,]),'CPP_PLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[3,-29,3,3,-2,3,-1,3,24,3,3,-6,-4,24,-5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,-7,24,-3,24,24,24,24,24,-10,24,24,24,-11,24,-9,24,24,-12,-8,24,24,24,24,-28,3,24,]),'CPP_INEQUALITY':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,25,-6,-4,25,-5,-7,25,-3,-13,-16,-18,25,25,-10,25,25,25,-11,-20,-9,-19,25,-12,-8,25,-17,-15,-14,-28,25,]),'CPP_CHAR':([0,2,3,5,7,9,10,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,59,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'CPP_LPAREN':([0,1,2,3,5,7,9,10,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,59,],[5,10,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'CPP_FSLASH':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,26,-6,-4,26,-5,-7,26,-3,26,26,26,26,26,-10,26,26,26,26,26,-9,26,26,26,-8,26,26,26,26,-28,26,]),'CPP_INTEGER':([0,2,3,5,7,9,10,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,59,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'CPP_EQUALITY':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,27,-6,-4,27,-5,-7,27,-3,-13,-16,-18,27,27,-10,27,27,27,-11,-20,-9,-19,27,-12,-8,27,-17,-15,-14,-28,27,]),'CPP_HAT':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,28,-6,-4,28,-5,-7,28,-3,-13,-16,-18,28,28,-10,-21,28,28,-11,-20,-9,-19,-22,-12,-8,28,-17,-15,-14,-28,28,]),'CPP_MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[7,-29,7,7,-2,7,-1,7,29,7,7,-6,-4,29,-5,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-7,29,-3,29,29,29,29,29,-10,29,29,29,-11,29,-9,29,29,-12,-8,29,29,29,29,-28,7,29,]),'CPP_STAR':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,30,-6,-4,30,-5,-7,30,-3,30,30,30,30,30,-10,30,30,30,30,30,-9,30,30,30,-8,30,30,30,30,-28,30,]),'CPP_COMMA':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,31,-6,-4,31,-5,-7,31,-3,-13,-16,-18,-25,-24,-10,-21,31,-23,-11,-20,-9,-19,-22,-12,-8,-26,-17,-15,-14,-28,-27,]),'CPP_GREATER':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,32,-6,-4,32,-5,-7,32,-3,-13,-16,-18,32,32,-10,32,32,32,-11,32,-9,32,32,-12,-8,32,-17,-15,-14,-28,32,]),'CPP_RSHIFT':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,34,-6,-4,34,-5,-7,34,-3,-13,34,34,34,34,-10,34,34,34,-11,34,-9,34,34,-12,-8,34,34,34,-14,-28,34,]),'CPP_LESS':([1,4,6,8,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,33,-6,-4,33,-5,-7,33,-3,-13,-16,-18,33,33,-10,33,33,33,-11,33,-9,33,33,-12,-8,33,-17,-15,-14,-28,33,]),'CPP_COLON':([1,4,6,11,12,14,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,-6,-4,-5,-7,-3,-13,-16,-18,-25,-24,-10,-21,59,-23,-11,-20,-9,-19,-22,-12,-8,-26,-17,-15,-14,-28,-27,]),'CPP_TILDE':([0,2,3,5,7,9,10,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,59,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'CPP_RPAREN':([1,4,6,11,12,13,14,35,36,37,38,39,40,41,42,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,60,],[-29,-2,-1,-6,-4,37,-5,-7,58,-3,-13,-16,-18,-25,-24,-10,-21,-23,-11,-20,-9,-19,-22,-12,-8,-26,-17,-15,-14,-28,-27,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,3,5,7,9,10,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,59,],[8,11,12,13,14,35,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> CPP_INTEGER','expression',1,'p_expression_number','evaluator.py',396),
  ('expression -> CPP_CHAR','expression',1,'p_expression_character','evaluator.py',400),
  ('expression -> CPP_LPAREN expression CPP_RPAREN','expression',3,'p_expression_group','evaluator.py',404),
  ('expression -> CPP_PLUS expression','expression',2,'p_expression_uplus','evaluator.py',408),
  ('expression -> CPP_MINUS expression','expression',2,'p_expression_uminus','evaluator.py',412),
  ('expression -> CPP_EXCLAMATION expression','expression',2,'p_expression_unop','evaluator.py',417),
  ('expression -> CPP_TILDE expression','expression',2,'p_expression_unop','evaluator.py',418),
  ('expression -> expression CPP_STAR expression','expression',3,'p_expression_binop','evaluator.py',430),
  ('expression -> expression CPP_FSLASH expression','expression',3,'p_expression_binop','evaluator.py',431),
  ('expression -> expression CPP_PERCENT expression','expression',3,'p_expression_binop','evaluator.py',432),
  ('expression -> expression CPP_PLUS expression','expression',3,'p_expression_binop','evaluator.py',433),
  ('expression -> expression CPP_MINUS expression','expression',3,'p_expression_binop','evaluator.py',434),
  ('expression -> expression CPP_LSHIFT expression','expression',3,'p_expression_binop','evaluator.py',435),
  ('expression -> expression CPP_RSHIFT expression','expression',3,'p_expression_binop','evaluator.py',436),
  ('expression -> expression CPP_LESS expression','expression',3,'p_expression_binop','evaluator.py',437),
  ('expression -> expression CPP_LESSEQUAL expression','expression',3,'p_expression_binop','evaluator.py',438),
  ('expression -> expression CPP_GREATER expression','expression',3,'p_expression_binop','evaluator.py',439),
  ('expression -> expression CPP_GREATEREQUAL expression','expression',3,'p_expression_binop','evaluator.py',440),
  ('expression -> expression CPP_EQUALITY expression','expression',3,'p_expression_binop','evaluator.py',441),
  ('expression -> expression CPP_INEQUALITY expression','expression',3,'p_expression_binop','evaluator.py',442),
  ('expression -> expression CPP_AMPERSAND expression','expression',3,'p_expression_binop','evaluator.py',443),
  ('expression -> expression CPP_HAT expression','expression',3,'p_expression_binop','evaluator.py',444),
  ('expression -> expression CPP_BAR expression','expression',3,'p_expression_binop','evaluator.py',445),
  ('expression -> expression CPP_LOGICALAND expression','expression',3,'p_expression_binop','evaluator.py',446),
  ('expression -> expression CPP_LOGICALOR expression','expression',3,'p_expression_binop','evaluator.py',447),
  ('expression -> expression CPP_COMMA expression','expression',3,'p_expression_binop','evaluator.py',448),
  ('expression -> expression CPP_QUESTION expression CPP_COLON expression','expression',5,'p_expression_conditional','evaluator.py',494),
  ('expression -> CPP_ID CPP_LPAREN expression CPP_RPAREN','expression',4,'p_expression_function_call','evaluator.py',506),
  ('expression -> CPP_ID','expression',1,'p_expression_identifier','evaluator.py',513),
]