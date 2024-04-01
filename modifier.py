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
def tree_block(ctx: common.McContext, tree_name: str, color_tuple: TreeBlockColors_t, tree_type: TreeType) -> None:
    """
    color_tuple = tuple(log_color, log_top_color, stripped_log_color, stripped_log_top_color, planks_color), 
    None if this log do not need process.
    """
    # get wood tail
    tree_tail: str = tree_type.value

    # log
    if color_tuple[0] is not None:
        drawer.border_block_texture(ctx, f'{tree_name}_{tree_tail}', color_tuple[0])
    # log top
    if color_tuple[1] is not None:
        drawer.border_block_texture(ctx, f'{tree_name}_{tree_tail}_top', color_tuple[1])
    # stripped log
    if color_tuple[2] is not None:
        drawer.border_block_texture(ctx, f'stripped_{tree_name}_{tree_tail}', color_tuple[2])
    # stripped log top
    if color_tuple[3] is not None:
        drawer.border_block_texture(ctx, f'stripped_{tree_name}_{tree_tail}_top', color_tuple[3])
    # planks
    if color_tuple[4] is not None:
        drawer.border_block_texture(ctx, f'{tree_name}_planks', color_tuple[4])

def prepare_tree_leaves(ctx: common.McContext) -> None:
    # generate 2 leaves overlay
    drawer.generate_leaves_level(ctx)
    drawer.generate_leaves_persistent(ctx)

    # generate general leaves overlay models
    # every single levaes level should inherit this model
    # prepare model data first
    payload: typing.Any = {
        "parent": "block/block",
        "textures": {
            "particle": "#all"
        },
        "elements": [{
            "from": [4, 4, -0.1],
            "to": [12, 12, 16.1],
            "faces": {
                "north": {
                    "texture": "#all",
                    "cullface": "north"
                },
                "south": {
                    "texture": "#all",
                    "cullface": "south"
                }
            }
        }, {
            "from": [-0.1, 4, 4],
            "to": [16.1, 12, 12],
            "faces": {
                "west": {
                    "texture": "#all",
                    "cullface": "west"
                },
                "east": {
                    "texture": "#all",
                    "cullface": "east"
                }
            }
        }, {
            "from": [4, -0.1, 4],
            "to": [12, 16.1, 12],
            "faces": {
                "down": {
                    "texture": "#all",
                    "cullface": "down"
                },
                "up": {
                    "texture": "#all",
                    "cullface": "up"
                }
            }
        }]
    }
    # write into files for level and presistent
    ctx.write_model('leaves_level', payload)
    ctx.write_model('leaves_persistent', payload)

    # write 1-7 tree levels model
    for i in range(7):
        # adjust to 1 based
        i += 1
        payload = {
            "parent": "minecraft:block/leaves_level",
            "textures": {
                "all": f"minecraft:block/leaves_level_{i}"
            }
        }
        ctx.write_model(f'leaves_level_{i}', payload)
    # write persistent
    for is_persistent in (True, False):
        payload = {
            "parent": "minecraft:block/leaves_persistent",
            "textures": {
                "all": f"minecraft:block/leaves_persistent_{'on' if is_persistent else 'off'}"
            }
        }
        ctx.write_model(f"leaves_persistent_{'on' if is_persistent else 'off'}", payload)

def tree_leaves(ctx: common.McContext, tree_name: str, color: str | None) -> None:
    # build name
    name: str = f'{tree_name}_leaves'
    # write blockstates
    blockstate_payload: typing.Any = {
        "multipart": [	
            {   "apply": { "model": f"minecraft:block/{name}" } },
            {   "when": { "distance": "1" },
                "apply": { "model": "minecraft:block/leaves_level_1" }
            },
            {   "when": { "distance": "2" },
                "apply": { "model": "minecraft:block/leaves_level_2" }
            },
            {   "when": { "distance": "3" },
                "apply": { "model": "minecraft:block/leaves_level_3" }
            },
            {   "when": { "distance": "4" },
                "apply": { "model": "minecraft:block/leaves_level_4" }
            },
            {   "when": { "distance": "5" },
                "apply": { "model": "minecraft:block/leaves_level_5" }
            },
            {   "when": { "distance": "6" },
                "apply": { "model": "minecraft:block/leaves_level_6" }
            },
            {   "when": { "distance": "7" },
                "apply": { "model": "minecraft:block/leaves_level_7" }
            },	
            {   "when": { "persistent": "true" },
                "apply": { "model": "minecraft:block/leaves_persistent_on" }
            },
            {   "when": { "persistent": "false" },
                "apply": { "model": "minecraft:block/leaves_persistent_off" }
            }
        ]
    }
    ctx.write_blockstate(name, blockstate_payload)

    # we use vanilla tree model (actually combined with our level overlay)
    # so no need to change model
    # adding border for tree texture is enough
    if color is not None:
        drawer.border_block_texture(ctx, name, color)
