import PIL, PIL.Image
import json, re, os, typing

class McContext():
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

    def __validate_src_path(self) -> None:
        assert(os.path.isdir(os.path.join(self.__mSrcPath, 'assets/minecraft/blockstates')))
        assert(os.path.isdir(os.path.join(self.__mSrcPath, 'assets/minecraft/models/block')))
        assert(os.path.isdir(os.path.join(self.__mSrcPath, 'assets/minecraft/textures/block')))

    def __layout_dst_path(self) -> None:
        os.makedirs(os.path.join(self.__mDstPath, 'assets/minecraft/blockstates'), exist_ok=True)
        os.makedirs(os.path.join(self.__mDstPath, 'assets/minecraft/models/block'), exist_ok=True)
        os.makedirs(os.path.join(self.__mDstPath, 'assets/minecraft/textures/block'), exist_ok=True)


    def get_mc_ver(self) -> int:
        return self.__mVer
    
    def get_src_custom(self, path: str) -> str:
        return os.join(self.__mSrcPath, 'assets/minecraft', path)
    
    def get_dst_custom(self, path: str) -> str:
        return os.join(self.__mDstPath, 'assets/minecraft', path)


    def read_blockstate(self, name: str) -> typing.Any:
        return load_json(os.path.join(self.__mSrcPath, 'assets/minecraft/blockstates', name + '.json'))
    
    def read_model(self, name: str) -> typing.Any:
        return load_json(os.path.join(self.__mSrcPath, 'assets/minecraft/models/block', name + '.json'))
    
    def read_texture(self, name: str) -> PIL.Image.Image:
        path: str = os.path.join(self.__mSrcPath, 'assets/minecraft/textures/block', name + '.png')
        return PIL.Image.open(path)

    def write_blockstate(self, name: str, payload: typing.Any) -> None:
        return save_json(os.path.join(self.__mDstPath, 'assets/minecraft/blockstates', name + '.json'), payload)
    
    def write_model(self, name: str, payload: typing.Any) -> None:
        return save_json(os.path.join(self.__mDstPath, 'assets/minecraft/models/block', name + '.json'), payload)
    
    def write_texture(self, name: str, img: PIL.Image.Image) -> None:
        path: str = os.path.join(self.__mDstPath, 'assets/minecraft/textures/block', name + '.png')
        img.save(path)

def load_json(json_path: str) -> typing.Any:
    with open(json_path, 'r', encoding='utf-8') as fs:
        return json.load(fs)

def save_json(json_path: str, payload: typing.Any) -> None:
    with open(json_path, 'w', encoding='utf-8') as fs:
        json.dump(payload, fs, indent=2)    # mojang use indent=2 json

g_HexColorRegex: re.Pattern = re.compile(r'^#[0-9a-f]{6}$')
def resolve_hex_color(hex_color: str) -> tuple[int, int, int]:
    hex_color = hex_color.lower()
    
    if g_HexColorRegex.match(hex_color) is None:
        raise Exception('invalid hex color string')
    return (
        int(hex_color[1:3], base=16),
        int(hex_color[3:5], base=16),
        int(hex_color[5:7], base=16),
    )
