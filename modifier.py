import common, drawer
import typing

def overworld_ore(ctx: common.McContext, name: str, color: str, deepslate_color: str | None = None) -> None:
    if deepslate_color is None:
        deepslate_color = color

    drawer.border_block_texture(ctx, name, color)
    drawer.border_block_texture(ctx, 'deepslate_' + name, deepslate_color)

def redstone_door(ctx: common.McContext, name: str) -> None:
    # create texture
    drawer.border_door_block_texture(ctx, name)

    # change open door model
    # no need to modify blockstate
    for half in ('top', 'bottom'):
        for hinge in ('left', 'right'):
            # build model name
            door_part: str = f'{name}_{half}_{hinge}_open'
            # load model for open door
            model: dict[str, typing.Any] = ctx.read_model(door_part)
            # modify texture to point them into our created new open door texture
            model['textures']['bottom'] = f'minecraft:block/{name}_bottom_open'
            model['textures']['top'] = f'minecraft:block/{name}_top_open'
            # save it
            ctx.write_model(door_part, model)

