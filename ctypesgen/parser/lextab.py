# lextab.py. This file automatically created by PLY (version 2.2). Don't edit!
_lextokens = {
    "HEADER_NAME": None,
    "IDENTIFIER": None,
    "PP_NUMBER": None,
    "CHARACTER_CONSTANT": None,
    "STRING_LITERAL": None,
    "OTHER": None,
    "PTR_OP": None,
    "INC_OP": None,
    "DEC_OP": None,
    "LEFT_OP": None,
    "RIGHT_OP": None,
    "LE_OP": None,
    "GE_OP": None,
    "EQ_OP": None,
    "NE_OP": None,
    "AND_OP": None,
    "OR_OP": None,
    "MUL_ASSIGN": None,
    "DIV_ASSIGN": None,
    "MOD_ASSIGN": None,
    "ADD_ASSIGN": None,
    "SUB_ASSIGN": None,
    "LEFT_ASSIGN": None,
    "RIGHT_ASSIGN": None,
    "AND_ASSIGN": None,
    "XOR_ASSIGN": None,
    "OR_ASSIGN": None,
    "PERIOD": None,
    "ELLIPSIS": None,
    "LPAREN": None,
    "NEWLINE": None,
    "PP_DEFINE": None,
    "PP_DEFINE_NAME": None,
    "PP_DEFINE_MACRO_NAME": None,
    "PP_MACRO_PARAM": None,
    "PP_STRINGIFY": None,
    "PP_IDENTIFIER_PASTE": None,
    "PP_END_DEFINE": None,
}
_lexreflags = 0
_lexliterals = ""
_lexstateinfo = {"INITIAL": "inclusive", "DEFINE": "exclusive"}
_lexstatere = {
    "INITIAL": [
        (
            '(?P<t_ANY_directive>\\#\\s+(\\d+)\\s+"([^"]+)"[ \\d]*\\n)|(?P<t_ANY_punctuator>(\\.\\.\\.|\\+\\+|\\|\\||>>=|<<=|\\+=|\\*=|\\^=|\\|=|-=|/=|%=|&=|>>|<<|--|->|&&|<=|>=|==|!=|<:|:>|<%|%>|\\)|\\[|\\.|\\+|\\*|\\^|\\||\\?|;|{|}|,|:|=|]|&|!|~|-|/|%|<|>))',
            [
                None,
                ("t_ANY_directive", "ANY_directive"),
                None,
                None,
                ("t_ANY_punctuator", "ANY_punctuator"),
            ],
        ),
        (
            "(?P<t_INITIAL_identifier>[a-zA-Z_]([a-zA-Z_]|[0-9])*)",
            [None, ("t_INITIAL_identifier", "INITIAL_identifier")],
        ),
        (
            "(?P<t_ANY_float>(?P<p1>[0-9]+)?(?P<dp>[.]?)(?P<p2>(?(p1)[0-9]*|[0-9]+))(?P<exp>(?:[Ee][+-]?[0-9]+)?)(?P<suf>([FflL]|D[FDL]|[fF]\\d+x?)?)(?!\\w))",
            [None, ("t_ANY_float", "ANY_float"), None, None, None, None, None],
        ),
        (
            "(?P<t_ANY_int>(?P<p1>(?:0x[a-fA-F0-9]+)|(?:[0-9]+))(?P<suf>[uUlL]*))",
            [None, ("t_ANY_int", "ANY_int"), None, None],
        ),
        (
            "(?P<t_ANY_character_constant>L?'(\\\\.|[^\\\\'])+')|(?P<t_ANY_string_literal>L?\"(\\\\.|[^\\\\\"])*\")|(?P<t_ANY_lparen>\\()|(?P<t_INITIAL_newline>\\n)|(?P<t_INITIAL_pp_define>\\#define)",
            [
                None,
                ("t_ANY_character_constant", "ANY_character_constant"),
                None,
                ("t_ANY_string_literal", "ANY_string_literal"),
                None,
                ("t_ANY_lparen", "ANY_lparen"),
                ("t_INITIAL_newline", "INITIAL_newline"),
                ("t_INITIAL_pp_define", "INITIAL_pp_define"),
            ],
        ),
    ],
    "DEFINE": [
        (
            '(?P<t_ANY_directive>\\#\\s+(\\d+)\\s+"([^"]+)"[ \\d]*\\n)|(?P<t_ANY_punctuator>(\\.\\.\\.|\\+\\+|\\|\\||>>=|<<=|\\+=|\\*=|\\^=|\\|=|-=|/=|%=|&=|>>|<<|--|->|&&|<=|>=|==|!=|<:|:>|<%|%>|\\)|\\[|\\.|\\+|\\*|\\^|\\||\\?|;|{|}|,|:|=|]|&|!|~|-|/|%|<|>))',
            [
                None,
                ("t_ANY_directive", "ANY_directive"),
                None,
                None,
                ("t_ANY_punctuator", "ANY_punctuator"),
            ],
        ),
        (
            "(?P<t_DEFINE_identifier>[a-zA-Z_]([a-zA-Z_]|[0-9])*)",
            [None, ("t_DEFINE_identifier", "DEFINE_identifier")],
        ),
        (
            "(?P<t_ANY_float>(?P<p1>[0-9]+)?(?P<dp>[.]?)(?P<p2>(?(p1)[0-9]*|[0-9]+))(?P<exp>(?:[Ee][+-]?[0-9]+)?)(?P<suf>([FflL]|D[FDL]|[fF]\\d+x?)?)(?!\\w))",
            [None, ("t_ANY_float", "ANY_float"), None, None, None, None, None],
        ),
        (
            "(?P<t_ANY_int>(?P<p1>(?:0x[a-fA-F0-9]+)|(?:[0-9]+))(?P<suf>[uUlL]*))",
            [None, ("t_ANY_int", "ANY_int"), None, None],
        ),
        (
            "(?P<t_ANY_character_constant>L?'(\\\\.|[^\\\\'])+')|(?P<t_ANY_string_literal>L?\"(\\\\.|[^\\\\\"])*\")|(?P<t_ANY_lparen>\\()|(?P<t_DEFINE_newline>\\n)|(?P<t_DEFINE_pp_param_op>(\\#\\#)|(\\#))",
            [
                None,
                ("t_ANY_character_constant", "ANY_character_constant"),
                None,
                ("t_ANY_string_literal", "ANY_string_literal"),
                None,
                ("t_ANY_lparen", "ANY_lparen"),
                ("t_DEFINE_newline", "DEFINE_newline"),
                ("t_DEFINE_pp_param_op", "DEFINE_pp_param_op"),
            ],
        ),
    ],
}
_lexstateignore = {"INITIAL": " \t\x0b\x0c\r", "DEFINE": " \t\x0b\x0c\r"}
_lexstateerrorf = {"INITIAL": "t_INITIAL_error", "DEFINE": "t_DEFINE_error"}
