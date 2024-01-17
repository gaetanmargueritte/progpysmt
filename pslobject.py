from typing import Dict, List, Tuple, Set
from pysmt.exceptions import PysmtSyntaxError

class Method:
    def __init__(self, name: str , signature: str) -> None:
        self.name = name
        self.signature = signature

    def __str__(self) -> str:
        return "%s (%s)"%(self.name, self.signature)

class PSLObject:
    def __init__(self) -> None:
        self.logics: List[str] = []
        self.type: str = None
        self.pbe: List[Tuple[List[str], str]] = []
        self.func_name: str = None
        self.constraints: List[str] = []
        self.check: bool = False
        self.solution: str = None
        self.constants: Dict[str, Set[str]] = {}
        self.grammar_interpretation: Dict[str, List[str|Method]] = {}

    def format_logics(self, elements: List[str]) -> None:
        res = []
        opened = False
        logic = ""
        args = []
        for e in elements:
            if e == "(":
                if opened: raise PysmtSyntaxError("Unexpected token %s of command set-logic" % e)
                opened = True
            elif e == ")":
                if not opened: raise PysmtSyntaxError("Unexpected token %s of command set-logic" % e)
                opened = False
            else:
                if logic == "":
                    logic = e
                else:
                    args.append(e)
            if not opened:
                res.append((logic, args))
                logic = ""
                args = []
        self.logics = res

