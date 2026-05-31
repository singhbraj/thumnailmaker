from imagekitio import ImageKit

from config import IMAGEKIT_PRIVATE_KEY, IMAGEKIT_PUBLIC_KEY, IMAGEKIT_URL_ENDPOINT

imagekit = ImageKit(
    private_key=IMAGEKIT_PRIVATE_KEY
)

def upload_file(file_bytes:bytes, file_name:str, folder:str, content_type:str="image/png")->str:
    """Upload a file to imagekit and return the CDN URL"""
    result  = imagekit.files.upload(
    file=(file_bytes,file_name,content_type),
    file_name=file_name,
    is_private_file=False,
    use_unique_file_name=True,
    folder=folder,
)
    
    return result.url

def get_variants(base_url:str)->dict:
    """ Returns 3 sizes of the image variants URLs using imagekit transformations. """
    return {
        "youtube": f"{base_url}?tr=w-1280,h-720,c-maintain_ratio,fo-auto",
        "shorts": f"{base_url}?tr=w-1080,h-1920,c-maintain_ratio,fo-auto",
        "youtube": f"{base_url}?tr=w-1280,h-1080,c-maintain_ratio,fo-auto",
    }
    
    