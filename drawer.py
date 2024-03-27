import common
import PIL, PIL.Image, PIL.ImageDraw
import typing

def border_block_texture(ctx: common.McContext, name: str, color: str) -> None:
    # read image
    img: PIL.Image.Image = ctx.read_texture(name)
    # check image size
    (x, y) = img.size
    assert(x == 16 and y == 16)
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
    (x, y) = example.size
    assert(x == 16 and y == 16)
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
