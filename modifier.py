import common, drawer
import typing, enum

#region Drawer Wrapper

def border_block(ctx: common.McContext, name: str, color: str) -> None:
    with common.ImgContext.from_existing(ctx, name, name) as imgctx:
        drawer.border(imgctx, color)

def colorful_border_block(ctx: common.McContext, name: str) -> None:
    with common.ImgContext.from_existing(ctx, name, None) as refctx:
        with common.ImgContext.from_empty(ctx, (16, 16), name) as imgctx:
            drawer.colorful_border(imgctx, refctx)

def snowflake_overlay_block(ctx: common.McContext, name: str) -> None:
    with common.ImgContext.from_existing(ctx, name, name) as imgctx:
        drawer.snowflake_overlay(imgctx)

def grass_border_block(ctx: common.McContext, name: str,
                left_height: int, right_height: int,
                top_color: str | None, bottom_color: str | None,
                is_dirt_path: bool) -> None:
    with common.ImgContext.from_existing(ctx, name, name) as imgctx:
        drawer.grass_border(imgctx, left_height, right_height, top_color, bottom_color, is_dirt_path)

#endregion

def common_ore(ctx: common.McContext, name: str, color: str, deepslate_color: str | None = None) -> None:
    if deepslate_color is None:
        deepslate_color = color

    border_block(ctx, name, color)
    border_block(ctx, f'deepslate_{name}', deepslate_color)

def door(ctx: common.McContext, name: str) -> None:
    # create texture
    with common.ImgContext.from_existing(ctx, f'{name}_top', f'{name}_top_open') as imgtop:
        with common.ImgContext.from_existing(ctx, f'{name}_bottom', f'{name}_bottom_open') as imgbottom:
            drawer.door_border(imgtop, imgbottom)

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
def tree(ctx: common.McContext, tree_name: str, color_tuple: TreeBlockColors_t, tree_type: TreeType) -> None:
    """
    color_tuple = tuple(log_color, log_top_color, stripped_log_color, stripped_log_top_color, planks_color), 
    None if this log do not need process.
    """
    # get wood tail
    tree_tail: str = tree_type.value

    # log
    if color_tuple[0] is not None:
        border_block(ctx, f'{tree_name}_{tree_tail}', color_tuple[0])
    # log top
    if color_tuple[1] is not None:
        border_block(ctx, f'{tree_name}_{tree_tail}_top', color_tuple[1])
    # stripped log
    if color_tuple[2] is not None:
        border_block(ctx, f'stripped_{tree_name}_{tree_tail}', color_tuple[2])
    # stripped log top
    if color_tuple[3] is not None:
        border_block(ctx, f'stripped_{tree_name}_{tree_tail}_top', color_tuple[3])
    # planks
    if color_tuple[4] is not None:
        border_block(ctx, f'{tree_name}_planks', color_tuple[4])

def prepare_tree_leaves(ctx: common.McContext) -> None:
    # generate 2 leaves overlay
    # create leaves level with 7 different level
    for i in range(1, 8, 1):
        with common.ImgContext.from_empty(ctx, (32, 32), f'leaves_level_{i}') as imgctx:
            drawer.leaves_level(imgctx, i)
    # create leaves persistent
    for is_persistent in (True, False):
        with common.ImgContext.from_empty(ctx, (32, 32), f'leaves_persistent_{"on" if is_persistent else "off"}') as imgctx:
            drawer.leaves_persistent(imgctx, is_persistent)

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
    for i in range(1, 8, 1):
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
        border_block(ctx, name, color)

def infested_stone(ctx: common.McContext, name: str, color: str, is_deepslate: bool) -> None:
    # decide how many texture we need to process
    proc_tex: tuple[str, ...]
    if is_deepslate: proc_tex = (name, f'{name}_top')
    else: proc_tex = (name, )

    # create infested block texture from normal one
    for tex_name in proc_tex:
        with common.ImgContext.from_existing(ctx, tex_name, f'infested_{tex_name}') as imgctx:
            drawer.border(imgctx, color)

    # decide how many models we need to process
    proc_model: tuple[str, ...]
    if is_deepslate: proc_model = (name, f'{name}_mirrored')
    else: proc_model = (name, )
    # create infested model from original one
    for model_name in proc_model:
        model: dict[str, typing.Any] = ctx.read_model(model_name)
        # replace all values in texture field
        model_textures: dict[str, str] = model['textures']
        for k, v in model_textures.items():
            # try match any modified texture name and rectify it
            for tex_name in proc_tex:
                if v == f'minecraft:block/{tex_name}':
                    model_textures[k] = f'minecraft:block/infested_{tex_name}'
                    break
        ctx.write_model(f'infested_{model_name}', model)

    # modify infested blockstate
    blockstate: dict[str, typing.Any] = ctx.read_blockstate(f'infested_{name}')
    variants: dict[str, typing.Any] = blockstate['variants']
    # iterate varients list to get all dict which need to be processed
    extracted_dict: list[dict[str, typing.Any]] = []
    for k, v in variants.items():
        if type(v) == list:
            extracted_dict.extend(typing.cast(list[dict[str, typing.Any]], v))
        else:
            extracted_dict.append(typing.cast(dict[str, typing.Any], v))
    # replace extracted dict model one by one
    for unit in extracted_dict:
        # try match model name
        for model_name in proc_model:
            if unit['model'] == f'minecraft:block/{model_name}':
                unit['model'] = f'minecraft:block/infested_{model_name}'
                break
    # save blockstate
    ctx.write_blockstate(f'infested_{name}', blockstate)
