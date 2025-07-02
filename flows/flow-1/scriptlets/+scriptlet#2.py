from oocana import Context
import os

#region generated meta
import typing
class Inputs(typing.TypedDict):
    name: str
    save_dir: str
class Outputs(typing.TypedDict):
    file_path: str | None
#endregion

def main(params: Inputs, context: Context) -> Outputs:

    file_name = params.get("name")
    save_dir = params.get("save_dir")
    file_path = os.path.join(save_dir, file_name)

    return {"file_path": file_path}
