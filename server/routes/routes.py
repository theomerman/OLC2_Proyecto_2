from flask import Blueprint, request, jsonify
from controllers.compiler.parser import Parser
from controllers.environment.environment import Environment
from controllers.environment.ast import Ast
from controllers.environment.error import Error
from controllers.environment.symbol import Symbol
from controllers.expressions.primitive import Primitive
from controllers.environment.generator import Generator

routes = Blueprint("routes", __name__)


# receive code from client
@routes.route("/sendCode", methods=["POST"])
def sendCode():
    data = request.get_json()
    # data = data.get("code")
    data = data["code"]

    env = Environment(None, "global")
    ast = Ast()
    gen = Generator()
    parser = None
    parser = Parser()


    instuctions = parser.parse(data)
    for intruction in instuctions:
        intruction.run(ast, env, gen)
    errors = serialize_errors(ast.errors)
    ast.symbol_table.insert(0, [env.id, env.table])

    # table = serialize_symbol_table([env.id,env.table])
    table = serialize(ast.symbol_table)

    # print(env.interfaces)
    # for item in env.interfaces:
    #     print(item)

    try:
        return jsonify(
            {
                "console": gen.get_full_code(),
                "errors": errors,
                "table": table,
            }
        )
    except Exception as e:
        print(e)
        return jsonify(
            {
                "console": ast.console,
                "errors": errors,
                "table": [],
            }
        )


def serialize_errors(_errors: list[Error]):
    errors = []
    for error in _errors:
        errors.append(
            {
                "description": error.description,
                "env": error.env,
                "type": error.type,
                "line": error.line,
                "column": error.column,
            }
        )
    return errors


def serialize(tables: list[list]):
    tb = []
    for table in tables:
        tb += (serialize_symbol_table(table))
    # print(tb)
    return tb


def serialize_symbol_table(symbol_table: list):
    keys = symbol_table[1].keys()
    table = []
    for key in keys:
        if type(symbol_table[1][key]) == Symbol:
            tmp = symbol_table[1][key].value
            if type(tmp) == str or type(tmp) == int or type(tmp) == float or type(tmp) == bool:
                table.append(
                    {
                        "id": key,
                        "env": symbol_table[0],
                        "value": symbol_table[1][key].value,
                        "type": symbol_table[1][key].type.name,
                        "line": symbol_table[1][key].line,
                        "column": symbol_table[1][key].col,
                    }
                )
            else:
                table.append(
                    {
                        "id": key,
                        "env": symbol_table[0],
                        "value": "Objeto",
                        "type": symbol_table[1][key].type.name,
                        "line": symbol_table[1][key].line,
                        "column": symbol_table[1][key].col,
                    }
                )
        elif type(symbol_table[1][key]) == Primitive:

            tmp = symbol_table[1][key].value
            if type(tmp) == str or type(tmp) == int or type(tmp) == float or type(tmp) == bool:
                table.append(
                    {
                        "id": key,
                        "env": symbol_table[0],
                        "value": symbol_table[1][key].value,
                        "type": symbol_table[1][key].type.name,
                        "line": symbol_table[1][key].line,
                        "column": symbol_table[1][key].column,
                    }
                )
            else:
                table.append(
                    {
                        "id": key,
                        "env": symbol_table[0],
                        "value": "Objeto",
                        "type": symbol_table[1][key].type.name,
                        "line": symbol_table[1][key].line,
                        "column": symbol_table[1][key].column,
                    }
                )
        else:
            table.append(
                {
                    "id": key,
                    "env": symbol_table[0],
                    "value": "Objeto",
                    "type": symbol_table[1][key].type.name,
                    "line": symbol_table[1][key].line,
                    "column": symbol_table[1][key].column,
                }
            )

    return table
