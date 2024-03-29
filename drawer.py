import common
import PIL, PIL.Image, PIL.ImageDraw
import typing

def _check_size(img: PIL.Image.Image, expected_size: tuple[int, int]) -> None:
    (x, y) = img.size
    if not (x == expected_size[0] and y == expected_size[1]):
        raise Exception('assert minecraft texture size failed')

def border_block_texture(ctx: common.McContext, name: str, color: str) -> None:
    # read image and check
    img: PIL.Image.Image = ctx.read_texture(name)
    _check_size(img, (16, 16))
    # create sketchpad and draw
    sketchpad = PIL.ImageDraw.Draw(img)
    # draw rectangle
    sketchpad.rectangle(
        (0, 0, 15, 15),
        fill=None,
        outline=common.resolve_hex_color(color),
        width=1
    )
    # save result
    ctx.write_texture(name, img)

g_ColorfulBorderBlockTextureMeta: typing.Any = {"animation": {"frametime": 5}}
def colorful_border_block_texture(ctx: common.McContext, name: str) -> None:
    # read image and check size
    example: PIL.Image.Image = ctx.read_texture(name)
    _check_size(example, (16, 16))
    # create a new image and paste example double
    img: PIL.Image.Image = PIL.Image.new(example.mode, (16, 32))
    img.paste(example, (0, 0))
    img.paste(example, (0, 16))
    # create sketchpad and write boundary
    sketchpad = PIL.ImageDraw.Draw(img)
    sketchpad.rectangle(
        (0, 0, 15, 15),
        fill=None,
        outline=common.resolve_hex_color('#18ff00'),
        width=1
    )
    sketchpad.rectangle(
        (0, 16, 15, 31),
        fill=None,
        outline=common.resolve_hex_color('#00ffc6'),
        width=1
    )
    # save it
    ctx.write_texture(name, img)

    # create animation meta file
    ctx.write_texture_meta(name, g_ColorfulBorderBlockTextureMeta)

def border_door_block_texture(ctx: common.McContext, name: str) -> None:
    # proc top and bottom respectively
    for is_top in (True, False):
        # load images
        door_part: str = name + ('_top' if is_top else '_bottom')
        img: PIL.Image.Image = ctx.read_texture(door_part)
        _check_size(img, (16, 16))
        # decide drawing lines coord point first
        route: tuple[tuple[int, int], ...]
        if is_top:
            route = ((1, 14), (1, 1), (14, 1), (14, 14))
        else:
            route = ((1, 1), (1, 14), (14, 14), (14, 1))
        # create sketchpad and draw left and right ring first
        sketchpad = PIL.ImageDraw.Draw(img)
        sketchpad.line(
            route,
            fill=common.resolve_hex_color('#df0906'),
            width=1,
            joint=None
        )
        # save it as new file
        ctx.write_texture(door_part + '_open', img)

