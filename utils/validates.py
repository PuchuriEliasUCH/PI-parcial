import click
from .json_manager import read_data


def validar_codigo(ctx, param, value):
    codigos = [x['codigo'] for x in read_data()['productos']]

    try:
        value = int(value)
    except ValueError:
        raise click.BadParameter("Debes ingresar únicamente números")

    if value in codigos:
        raise click.BadParameter("Este producto ya está registrado")

    return value


def validar_existencia(ctx, param, value):
    prod = False

    for i in read_data()['productos']:
        if i['codigo'] == int(value):
            prod = True
            break

    if not prod:
        raise click.BadParameter("Este producto no está registrado")
    else:
        return value
