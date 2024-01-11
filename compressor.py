import logging
import os
from typing import List

from PIL import Image

logger = logging.getLogger("ms_word_image_compressor")


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
                logger.debug(f"[Compressor] Skipping file {image_name}")
                continue

            file_size = os.path.getsize(image_path)

            if file_size <= self.ignore_less_than:
                file_size_in_kb = file_size // 1024
                logger.debug(
                    f"[Compressor] No need to compress image {image_name} because size is {file_size_in_kb}"
                )
                continue

            logger.debug(f"[Compressor] Compressing file {image_name}")

            with Image.open(image_path) as pil_image:
                width, height = pil_image.size
                pil_image = pil_image.resize((width // 2, height // 2))
                pil_image.save(image_path, optimize=True, quality=self.quality)

            logger.debug(
                f"[Compressor] File {image_name} has been sucessfully compressed!"
            )
