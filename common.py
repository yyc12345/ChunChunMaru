'''
The module providing common functions and classes used by other modules
'''

import PIL, PIL.Image
import json, re, os, typing

class McContext():
    __cBlockstatePath: typing.ClassVar[str] = 'assets/minecraft/blockstates'
    __cModelPath: typing.ClassVar[str] = 'assets/minecraft/models/block'
    __cTexturePath: typing.ClassVar[str] = 'assets/minecraft/textures/block'

    __mSrcPath: str
    __mDstPath: str
    __mVer: int

    def __init__(self, src_path: str, dst_path: str, ver: int) -> None:
        # set essential value
        self.__mSrcPath = src_path
        self.__mDstPath = dst_path
        self.__mVer = ver
        # validate src path
        self.__validate_src_path()
        # set dst path layout
        self.__layout_dst_path()
        # set res pack info
        self.__deploy_res_pack_info()

    def __validate_src_path(self) -> None:
        assert(os.path.isdir(os.path.join(self.__mSrcPath, self.__cBlockstatePath)))
        assert(os.path.isdir(os.path.join(self.__mSrcPath, self.__cModelPath)))
        assert(os.path.isdir(os.path.join(self.__mSrcPath, self.__cTexturePath)))

    def __layout_dst_path(self) -> None:
        os.makedirs(os.path.join(self.__mDstPath, self.__cBlockstatePath), exist_ok=True)
        os.makedirs(os.path.join(self.__mDstPath, self.__cModelPath), exist_ok=True)
        os.makedirs(os.path.join(self.__mDstPath, self.__cTexturePath), exist_ok=True)

    def __deploy_res_pack_info(self) -> None:
        # write package info
        payload: typing.Any = {
            "pack": {
                "pack_format": self.__mVer,
                "description": "ChunChunMaru Resource Package"
            }
        }
        save_json(os.path.join(self.__mDstPath, 'pack.mcmeta'), payload)

        # set package icon
        # todo...

    def get_mc_ver(self) -> int:
        return self.__mVer

    def get_src_path(self, *args: str) -> str:
        return os.path.join(self.__mSrcPath, *args)

    def get_dst_path(self, *args: str) -> str:
        return os.path.join(self.__mDstPath, *args)


    def read_blockstate(self, name: str) -> typing.Any:
        return load_json(self.get_src_path(self.__cBlockstatePath, name + '.json'))

    def read_model(self, name: str) -> typing.Any:
        return load_json(self.get_src_path(self.__cModelPath, name + '.json'))

    def read_texture(self, name: str) -> PIL.Image.Image:
        return PIL.Image.open(self.get_src_path(self.__cTexturePath, name + '.png'))

    def read_texture_meta(self, name: str) -> typing.Any:
        return load_json(self.get_src_path(self.__cTexturePath, name + '.png.mcmeta'))


    def write_blockstate(self, name: str, payload: typing.Any) -> None:
        save_json(self.get_dst_path(self.__cBlockstatePath, name + '.json'), payload)

    def write_model(self, name: str, payload: typing.Any) -> None:
        save_json(self.get_dst_path(self.__cModelPath, name + '.json'), payload)

    def write_texture(self, name: str, img: PIL.Image.Image) -> None:
        img.save(self.get_dst_path(self.__cTexturePath, name + '.png'))

    def write_texture_meta(self, name: str, payload: typing.Any) -> None:
        save_json(self.get_dst_path(self.__cTexturePath, name + '.png.mcmeta'), payload)

class ImgContext():
    __mCtx: McContext
    __mOutputName: str | None
    __mIsValid: bool

    __mImg: PIL.Image.Image
    __mImgMeta: typing.Any | None

    def __init__(self, ctx: McContext, img: PIL.Image.Image, img_meta: typing.Any | None, output_img_name: str | None) -> None:
        """
        Do no call this function directly.
        You should get instance by calling class methods
        """
        self.__mCtx = ctx
        self.__mOutputName = output_img_name

        self.__mImg = img
        self.__mImgMeta = img_meta

        self.__mIsValid = True

    @classmethod
    def from_empty(cls, ctx: McContext, size: tuple[int, int], output_img_name: str | None):
        # create image
        img = PIL.Image.new('RGBA', size, resolve_hex_alpha_color('#00000000'))
        # return instance
        return cls(ctx, img, None, output_img_name)

    @classmethod
    def from_existing(cls, ctx: McContext, input_img_name: str, output_img_name: str | None):
        # load image
        img = ctx.read_texture(input_img_name)
        # try loading image meta
        try: img_meta = ctx.read_texture_meta(input_img_name)
        except: img_meta = None
        # return instance
        return cls(ctx, img, img_meta, output_img_name)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.dispose()
    
    def dispose(self) -> None:
        if self.__mIsValid:
            # if need to save image, save it
            if self.__mOutputName is not None:
                # save image
                self.__mCtx.write_texture(self.__mOutputName, self.__mImg)
                # save image meta if existing
                if self.__mImgMeta is not None:
                    self.__mCtx.write_texture_meta(self.__mOutputName, self.__mImgMeta)

            # free image
            self.__mImg.close()
            # mark as invalid
            self.__mIsValid = False

    def __check_validation(self) -> None:
        if not self.__mIsValid:
            raise Exception('call a invalid ImgContext')

    def get_image(self) -> PIL.Image.Image:
        """
        Return the **reference** to loaded image.

        Please note that you can not replace image located in this class
        because this class will free it in future.
        If you really want to replace it with a new image, you should resize, clear it and 
        paste your image in this instance, rather than directly replace it.
        """
        self.__check_validation()
        return self.__mImg
    
    def get_image_meta(self) -> typing.Any | None:
        """
        Return the **reference** to the loaded image meta data.
        If no meta data, this function will return None.
        
        Please note that this image returns is reference.
        It means that it will return a reference to meta dict if existing.
        All operations (update, clear and etc) on return value will be 
        directly reflected in the instance holded by this context.
        """
        self.__check_validation()
        return self.__mImgMeta
    
    def set_image_meta(self, data: typing.Any | None) -> None:
        """
        Set image meta data for this context as the reference.
        Or you can set None to remove existing meta.

        Please note that your passed data is by reference.
        It means that you should not change it after calling this method
        until this context is disposed. Otherwise the written image meta
        will not be same one when you calling this method.
        """
        self.__check_validation()
        self.__mImgMeta = data

def load_json(json_path: str) -> typing.Any:
    with open(json_path, 'r', encoding='utf-8') as fs:
        return json.load(fs)

def save_json(json_path: str, payload: typing.Any) -> None:
    with open(json_path, 'w', encoding='utf-8') as fs:
        json.dump(payload, fs, indent=2)    # mojang use indent=2 json

g_HexColorRegex: re.Pattern = re.compile(r'^#[0-9a-f]{6}$')
def resolve_hex_color(hex_color: str) -> tuple[int, int, int]:
    """
    hex color format: '#rrggbb'
    """
    hex_color = hex_color.lower()

    if g_HexColorRegex.match(hex_color) is None:
        raise Exception('invalid hex color string')
    return (
        int(hex_color[1:3], base=16),
        int(hex_color[3:5], base=16),
        int(hex_color[5:7], base=16),
    )

g_HexAlphaColorRegex: re.Pattern = re.compile(r'^#[0-9a-f]{8}$')
def resolve_hex_alpha_color(hex_color: str) -> tuple[int, int, int, int]:
    """
    hex color format: '#rrggbbaa'
    for alpha, 0x00 means full transparent, 0xff means opaque.
    """
    hex_color = hex_color.lower()

    if g_HexAlphaColorRegex.match(hex_color) is None:
        raise Exception('invalid hex alpha color string')
    return (
        int(hex_color[1:3], base=16),
        int(hex_color[3:5], base=16),
        int(hex_color[5:7], base=16),
        int(hex_color[7:9], base=16),
    )