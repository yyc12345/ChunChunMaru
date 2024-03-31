import common, drawer
import typing, enum

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

TreeBlockColors_t = tuple[str | None, str | None, str | None, str | None, str | None]
class TreeType(enum.Enum):
    Overworld = 'log'
    Nether = 'stem'
    Bamboo = 'block'
def tree_block(ctx: common.McContext, name: str, color_tuple: TreeBlockColors_t, tree_type: TreeType) -> None:
    """
    color_tuple = tuple(log_color, log_top_color, stripped_log_color, stripped_log_top_color, planks_color), 
    None if this log do not need process.
    """
    # get wood tail
    wood_tail: str = tree_type.value

    # log
    if color_tuple[0] is not None:
        drawer.border_block_texture(ctx, f'{name}_{wood_tail}', color_tuple[0])
    # log top
    if color_tuple[1] is not None:
        drawer.border_block_texture(ctx, f'{name}_{wood_tail}_top', color_tuple[1])
    # stripped log
    if color_tuple[2] is not None:
        drawer.border_block_texture(ctx, f'stripped_{name}_{wood_tail}', color_tuple[2])
    # stripped log top
    if color_tuple[3] is not None:
        drawer.border_block_texture(ctx, f'stripped_{name}_{wood_tail}_top', color_tuple[3])
    # planks
    if color_tuple[4] is not None:
        drawer.border_block_texture(ctx, f'{name}_planks', color_tuple[4])

def prepare_tree_leaves(ctx: common.McContext) -> None:
    # generate 2 leaves overlay
    drawer.generate_leaves_level(ctx)
    drawer.generate_leaves_persistent(ctx)

    # generate leaves overlay used models
    # todo...

def tree_leaves(ctx: common.McContext, name: str) -> None:
    pass
