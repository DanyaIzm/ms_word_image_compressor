import logging
import os
import shutil
from zipfile import ZipFile

logger = logging.getLogger("ms_word_image_compressor")


class ZipExtracter:
    def __init__(
        self, filepath: str, extract_path: str = os.path.join(".", "extracted")
    ) -> None:
        self.filepath = filepath
        self.extract_path = extract_path

    def extract(self) -> None:
        with ZipFile(self.filepath, mode="r") as read_file:
            logger.debug(f"[Extractor] Extracting file {self.filepath}")
            read_file.extractall(self.extract_path)

    def clear(self) -> None:
        logger.debug("[Extractor] Removing temporary folder")
        shutil.rmtree(self.extract_path)

    def get_extract_path(self) -> str:
        return self.extract_path
