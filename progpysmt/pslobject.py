from typing import Dict, List, Tuple, Set, Any
from progpysmt.exceptions import PysmtSyntaxError


class Method:
    def __init__(self, name: str, signature: str) -> None:
        self.name = name
        self.signature = signature

    def __str__(self) -> str:
        return "%s (%s)" % (self.name, self.signature)


class Constraint:
    def __init__(self, var: Dict[str, str], const: Dict[str, Set[str]]) -> None:
        self.table_of_symbols: Dict[str, List[Any]] = {}
        for v in var:
            self.table_of_symbols[v] = None
        for c in const:
            for v in const[c]:
                self.table_of_symbols[v] = v
        self.pbe: Dict[str, Any] = {}


class PSLObject:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self.logics: List[str] = []
        self.type: str = None
        self.pbe: List[Tuple[List[str], str]] = []
        self.func_name: str = None
        self.constraints_syntax: List[str] = []
        self.check: bool = False
        self.solution: str = None
        self.constants: Dict[str, Set[str]] = {}
        self.grammar_interpretation: Dict[str, List[str | Method]] = {}
        self.variables: Dict[str, str] = {}
        self.constraints: List[Constraint] = []
        self.smtlogic: str = ""
        self.methods: Dict[Tuple(str, str), str] = {}

    def format_logics(self, elements: List[str]) -> None:
        res = []
        opened = False
        logic = ""
        args = []
        for e in elements:
            if e == "(":
                if opened:
                    raise PysmtSyntaxError(
                        "Unexpected token %s of command set-logic" % e
                    )
                opened = True
            elif e == ")":
                if not opened:
                    raise PysmtSyntaxError(
                        "Unexpected token %s of command set-logic" % e
                    )
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
