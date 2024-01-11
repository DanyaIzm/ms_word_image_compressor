import shutil


class ZipSaver:
    def __init__(
        self, folder_path: str, path_to_save: str, extension: str | None = None
    ) -> None:
        self.folder_path = folder_path
        self.path_to_save = (
            path_to_save if not extension else path_to_save + "." + extension
        )

    def save(self) -> None:
        result_filename = shutil.make_archive(
            self.path_to_save, "zip", self.folder_path
        )
        filename = ".".join(result_filename.split(".")[:-1])

        shutil.move(result_filename, filename)
