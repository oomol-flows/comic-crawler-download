from oocana import Context
import os
import requests
from urllib.parse import unquote, urlparse

#region generated meta
import typing
class Inputs(typing.TypedDict):
    item: typing.Any
    save_dir: str | None
class Outputs(typing.TypedDict):
    item: typing.Any
#endregion

def main(params: Inputs, context: Context) -> Outputs:
    url = params.get("item")
    save_dir = params.get("save_dir")
    if save_dir is None:
        save_dir = context.session_dir
    image_path = download_image(url, save_dir)

    return {"item": image_path}

def download_image(url, save_dir='images'):
    """
    下载图片并保存为URL中的文件名
    
    参数:
        url (str): 图片的URL
        save_dir (str): 保存目录，默认为当前目录下的images文件夹
    """
    # 创建保存目录（如果不存在）
    os.makedirs(save_dir, exist_ok=True)
    
    try:
        # 发送HTTP GET请求
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功
        
        # 从URL中提取文件名
        parsed_url = urlparse(url)
        filename = unquote(os.path.basename(parsed_url.path))
        
        # 如果URL中没有文件名，使用默认名
        if not filename:
            filename = "downloaded_image.jpg"
        
        # 构建保存路径
        save_path = os.path.join(save_dir, filename)
        
        # 保存图片
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"图片已保存至: {save_path}")
        return save_path
    
    except Exception as e:
        print(f"下载失败: {e}")
        return None