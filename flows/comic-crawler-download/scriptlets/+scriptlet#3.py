from oocana import Context
import os

#region generated meta
import typing
class Inputs(typing.TypedDict):
    name: str
    save_dir: str
class Outputs(typing.TypedDict):
    pack_path: str | None
#endregion

def main(params: Inputs, context: Context) -> Outputs:
    name = params.get("name")
    save_dir = params.get("save_dir")
    pack_path = os.path.join(save_dir, name) if name and save_dir else None

    return { "pack_path": pack_path }