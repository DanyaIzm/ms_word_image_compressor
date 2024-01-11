import os
from typing import List
from PIL import Image


class ImageCompressor:
    def __init__(
        self,
        images_folder: str,
        ignore_less_than: int,
        filetypes: List[str] = ["png"],
        quality: int = 50,
    ) -> None:
        self.images_folder = images_folder
        self.filetypes = filetypes
        self.quality = quality
        self.ignore_less_than = ignore_less_than

    def compress(self) -> None:
        for image_name in os.listdir(self.images_folder):
            image_path = os.path.join(self.images_folder, image_name)

            if image_path.split(".")[-1] not in self.filetypes:
                continue

            file_size = os.path.getsize(image_path)

            if file_size <= self.ignore_less_than:
                continue

            with Image.open(image_path) as pil_image:
                width, height = pil_image.size
                pil_image = pil_image.resize((width // 2, height // 2))
                pil_image.save(image_path, optimize=True, quality=self.quality)
