import logging
import shutil


logger = logging.getLogger("ms_word_image_compressor")


class ZipSaver:
    def __init__(
        self, folder_path: str, path_to_save: str, extension: str | None = None
    ) -> None:
        self.folder_path = folder_path
        self.path_to_save = (
            path_to_save if not extension else path_to_save + "." + extension
        )

    def save(self) -> None:
        logger.debug(f"[Saver] Saving file to {self.path_to_save}")
        result_filename = shutil.make_archive(
            self.path_to_save, "zip", self.folder_path
        )
        filename = ".".join(result_filename.split(".")[:-1])

        logger.debug(f"[Saver] Saved file to {result_filename} sucessfully!")

        shutil.move(result_filename, filename)

        logger.debug(
            f"[Saver] Renamed file from {result_filename} to {filename} sucessfully!"
        )
